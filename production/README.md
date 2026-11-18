# STUDIO — Video Renderer Prototype (NOT PUBLISHED)

**Status:** TEST_ONLY technical implementation, awaiting independent review and owner approval to activate. Neither a real Minecraft Short nor a production release. Real research STUDIO-R001 remains REVISIONS REQUIRED.

## What this is

This branch adds a repeatable offline renderer for a **demonstration**, using the **independently PASS_TEST synthetic script** from [PR #12](https://github.com/victor12416/Studio/pull/12#issuecomment-6974520566), head `723912d2c1dfea4eb24a533be3ec055017daf390`.

Files:
- `production/fixtures/missing_medal.json` — exact approved-for-test 133-word narration plus 32 verbatim caption cues. Check against source script/caption plan at pinned SHA; no other story substitutions.
- `production/render_short.py` — uses **espeak-ng offline TTS**, calculates caption boundaries from the resulting waveform for each phrase, writes ASS captions and renders with **FFmpeg**.
- `.github/workflows/studio-video-prototype.yml` — **manual GitHub Actions dispatch only**, no scheduled task, webhooks, uploads, publishing or posting to social platforms. Generates an MP4 and JSON report as a downloadable **Actions artifact** retained for seven days.

## Limits and rights

- **No Minecraft footage has been supplied.** When no gameplay file is passed, the output uses a solid background with an obvious visible label: `TEST PROTOTYPE - GAMEPLAY NOT SUPPLIED`. This can test the video render but is **not** a finished Minecraft gameplay Short and must never be presented as one.
- To produce an actual Minecraft-background test, the owner must supply footage they created or have legal permission to reuse. Put a properly authorized MP4 under `production/assets/` and specify the relative path in the workflow input. Do not commit assets without rights/approval. A recording is not included in this branch.
- espeak-ng is free and offline but **robotic**, not a finished professional narration voice. No claims about TTS consent/quality, pacing or accessibility are made.
- Caption timing is computed from synthesized audio **per cue**. It is closer to sync than estimated 0–60s cue timings but is **not word-level forced alignment**. A human must listen and inspect before calling them synchronized.
- No performance claims, metric collection, ads, YouTube API, TikTok API, publishing tokens or auto-upload routines are included.
- The final speech duration will be **measured after generating audio**, not forced to the original hypothetical 60 seconds. A warning reports if actual audio falls outside 45–70 seconds.
- A playable MP4 only proves a **single technical smoke test**, not reliability, content-market fit, viewer retention or rights clearance.

## How the owner can test it (AFTER branch review and merge/approval)

1. Open GitHub repository `victor12416/Studio`.
2. Select **Actions** → **Studio TEST ONLY - Render Video Prototype** → **Run workflow**.
3. Leave `gameplay_path` blank to render a clearly labelled **placeholder prototype**. To test with owned Minecraft video, enter a validated relative path like `production/assets/parkour.mp4`, after that file exists in the checkout.
4. Open the completed Actions run; download **studio-missing-medal-TEST_ONLY** from Artifacts. It contains `missing_medal_TEST_ONLY.mp4` and `missing_medal_TEST_ONLY.json`.
5. Review actual sound, all 32 captions and legibility on a phone, visible gameplay rights, safe areas, timing and story. Report blocking defects to the independent Reviewer before a demo is presented.

## Optional manual local render (Linux)

Install `ffmpeg`, `espeak-ng` (plus an installed `DejaVu Sans` font), then:

```bash
python3 production/render_short.py --fixture production/fixtures/missing_medal.json --output output/missing_medal_TEST_ONLY.mp4
```

With a rights-cleared gameplay file:

```bash
python3 production/render_short.py --gameplay production/assets/parkour.mp4 --output output/missing_medal_TEST_ONLY.mp4
```

**Next owner dependency:** supply or approve suitable owned/licensed Minecraft parkour footage. **Next QC dependency:** inspect/approve this pipeline's code and actual output before showing the completed Short as anything more than a technical prototype.
