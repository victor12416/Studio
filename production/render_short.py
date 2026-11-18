#!/usr/bin/env python3
"""Studio TEST_ONLY renderer. Offline espeak-ng voice and FFmpeg; no publishing."""
import argparse
import json
import re
import shutil
import subprocess
import tempfile
import wave
from pathlib import Path

def run(argv):
    subprocess.run(argv, check=True)

def ass_time(seconds):
    n = round(seconds * 100)
    h, n = divmod(n, 360000)
    m, n = divmod(n, 6000)
    s, n = divmod(n, 100)
    return f"{h}:{m:02d}:{s:02d}.{n:02d}"

def escaped_ass(s):
    # Input is ordinary text, not ASS markup.
    s = re.sub(r"[{}\\]", "", s)
    words = s.split()
    if len(s) > 27 and len(words) >= 4:
        split = min(range(2, len(words)), key=lambda k: abs(len(" ".join(words[:k])) - len(" ".join(words[k:]))))
        return " ".join(words[:split]) + r"\N" + " ".join(words[split:])
    return s

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--fixture", type=Path, default=Path("production/fixtures/missing_medal.json"))
    p.add_argument("--gameplay", type=Path, help="Your owned/licensed Minecraft recording; if omitted renders a clearly labelled placeholder.")
    p.add_argument("--output", type=Path, default=Path("output/missing_medal_PROTOTYPE.mp4"))
    p.add_argument("--width", type=int, default=1080)
    p.add_argument("--height", type=int, default=1920)
    p.add_argument("--fps", type=int, default=24)
    args = p.parse_args()
    if args.width < 320 or args.height < 480:
        p.error("Choose a sensible vertical video size.")
    for app in ("ffmpeg", "ffprobe", "espeak-ng"):
        if not shutil.which(app):
            raise SystemExit(f"Missing {app}. Install ffmpeg and espeak-ng.")
    fixture = json.loads(args.fixture.read_text(encoding="utf-8"))
    cues = fixture["cues"]
    narration = fixture["narration"].strip()
    if not cues or any(not isinstance(c, str) or not c.strip() for c in cues):
        raise ValueError("Nonempty text captions required.")
    if " ".join(cues) != narration:
        raise ValueError("Caption reconstruction differs from verified source narration.")
    if args.gameplay and not args.gameplay.is_file():
        raise FileNotFoundError("Gameplay path not found: " + str(args.gameplay))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="studio_render_") as folder:
        tmp = Path(folder)
        pcm = bytearray()
        segments = []
        sr = channels = width = None
        # Each caption phrase gets its OWN synthesized waveform. Actual audio
        # sample lengths, not estimated source timestamps, set cue boundaries.
        for i, cue in enumerate(cues):
            f = tmp / f"phrase_{i:03d}.wav"
            run(["espeak-ng", "-v", "en-us", "-s", "147", "-w", str(f), cue])
            with wave.open(str(f), "rb") as w:
                spec = (w.getframerate(), w.getnchannels(), w.getsampwidth())
                if sr is None:
                    sr, channels, width = spec
                if spec != (sr, channels, width):
                    raise ValueError("espeak-ng audio format changed between phrases")
                start = len(pcm) / (sr * channels * width)
                pcm.extend(w.readframes(w.getnframes()))
                end = len(pcm) / (sr * channels * width)
                segments.append((start, end, cue))
                # Tiny natural phrase break, accounted for in the caption end.
                pcm.extend(b"\x00" * (round(sr * 0.045) * channels * width))
        wavpath = tmp / "voice.wav"
        with wave.open(str(wavpath), "wb") as w:
            w.setnchannels(channels); w.setsampwidth(width); w.setframerate(sr)
            w.writeframes(bytes(pcm))
        total = len(pcm) / (sr * channels * width)
        ass = tmp / "captions.ass"
        style = (
            "[Script Info]\nScriptType: v4.00+\nPlayResX: 1080\nPlayResY: 1920\n"
            "WrapStyle: 2\nScaledBorderAndShadow: yes\n"
            "[V4+ Styles]\n"
            "Format: Name,Fontname,Fontsize,PrimaryColour,SecondaryColour,OutlineColour,BackColour,"
            "Bold,Italic,Underline,StrikeOut,ScaleX,ScaleY,Spacing,Angle,BorderStyle,Outline,Shadow,"
            "Alignment,MarginL,MarginR,MarginV,Encoding\n"
            "Style: Caption,DejaVu Sans,76,&H00FFFFFF,&H00FFFFFF,&H00000000,&H55000000,"
            "1,0,0,0,100,100,0,0,1,6,2,2,90,90,370,1\n"
            "[Events]\n"
            "Format: Layer,Start,End,Style,Name,MarginL,MarginR,MarginV,Effect,Text\n"
        )
        ass.write_text(style + "".join(
            f"Dialogue: 0,{ass_time(start)},{ass_time(end)},Caption,,0,0,0,,{escaped_ass(cue)}\n"
            for start, end, cue in segments
        ), encoding="utf-8")
        vf = f"fps={args.fps},scale={args.width}:{args.height}:force_original_aspect_ratio=increase,crop={args.width}:{args.height},setsar=1,subtitles={ass.as_posix()}"
        if args.gameplay:
            inp = ["-stream_loop", "-1", "-i", str(args.gameplay)]
        else:
            inp = ["-f", "lavfi", "-i", f"color=c=0x152239:s={args.width}x{args.height}:r={args.fps}"]
            # Clearly marked synthetic background so it cannot be mistaken for Minecraft.
            vf += ",drawtext=text='TEST PROTOTYPE - GAMEPLAY NOT SUPPLIED':fontcolor=yellow:fontsize=35:borderw=3:bordercolor=black:x=(w-text_w)/2:y=220"
        ffmpeg = [
            "ffmpeg", "-hide_banner", "-loglevel", "error", "-y",
            *inp, "-i", str(wavpath), "-map", "0:v:0", "-map", "1:a:0",
            "-vf", vf, "-c:v", "libx264", "-preset", "veryfast",
            "-crf", "24", "-pix_fmt", "yuv420p", "-r", str(args.fps),
            "-c:a", "aac", "-b:a", "128k", "-t", str(total),
            "-movflags", "+faststart", str(args.output)
        ]
        run(ffmpeg)
        if not args.output.is_file() or args.output.stat().st_size == 0:
            raise RuntimeError("Rendering produced no MP4.")
        info = {
            "test_only": True, "original_script_source": fixture["source"],
            "caption_cues": len(cues), "narration_words": len(narration.split()),
            "measured_synthesized_audio_seconds": round(total, 3),
            "gameplay_provided": bool(args.gameplay),
            "frame_size": [args.width, args.height],
            "output": str(args.output),
            "limitations": "Offline synthesized voice and phrase-level timing; no human audio QC, no verified Minecraft asset licenses, no upload or publishing."
        }
        report = args.output.with_suffix(".json")
        report.write_text(json.dumps(info, indent=2) + "\n", encoding="utf-8")
        print(json.dumps(info, indent=2))
        if not (45 <= total <= 70):
            print(f"WARNING: duration {total:.1f}s outside the 45–70 second creative target. Review delivery and voice speed.")

if __name__ == "__main__":
    main()
