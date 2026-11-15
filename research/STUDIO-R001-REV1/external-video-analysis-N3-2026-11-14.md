# Studio R001 REV1 — External AI video-analysis experiment (N3)

**Status:** SUCCESSFUL VIDEO-ANALYSIS JOB; **INDEPENDENT CAPTION-SYNC VERIFICATION STILL OPEN**  
**Video:** [N3 — jk7ehjJXXQw](https://www.youtube.com/watch?v=jk7ehjJXXQw)  
**Provider/tool:** Connected Higgsfield `video_analysis_create` with the **YouTube URL** as input; subsequently read `video_analysis_status`.  
**Provider analysis job ID:** `4076be8c-0c5c-48ce-934f-7df0e3be7e95`  
**Provider job result:** `completed`, `fail_reason: null`, six returned timecoded scene objects.  
**Result checked:** November 14, 2026, EST (UTC November 15, 2026). Exact provider creation/finish timestamps were not exposed by this result.  
**Evidence class:** **Third-party AI-generated audiovisual scene analysis.** This is independent of the owner's manual notes in the sense of a separately run service, but it is **not** an authenticated frame-by-frame audit, human observation or full transcript; model descriptions/transcriptions can be inaccurate. No media bytes or individual frames were returned to this conversation.

## Test and result

A direct YouTube URL was submitted to a connected external video-analysis service. Unlike the earlier browser's stuck player (`currentTime=0`, `readyState=0`), this service returned a completed analysis with scene-level references to visual Minecraft-style parkour activity and narrated story audio.

| AI scene | Time interval returned | Gameplay description (model-generated; paraphrased) | Story audio content (model-generated; paraphrased) |
| --- | --- | --- | --- |
| 1 | 0:00–0:05 | First-person movement/jumping on snow and wooden platforms. | Family betrayal / revenge opening line. |
| 2 | 0:05–0:15 | Progression into bright green garden and water sections. | Family leadership dispute, sibling Sarah favored. |
| 3 | 0:15–0:30 | Architectural areas and canyon-like passages. | Narrator plans response using knowledge of business. |
| 4 | 0:30–0:42 | Movement through water channels and brick structure. | Narrator covertly transfers valuable company contracts/assets. |
| 5 | 0:42–0:57 | Open terrain and glowing crystalline cave. | Narrator resigns and announces own business. |
| 6 | 0:57–1:21 | Continuous parkour through purple crystalline area. | New company succeeds; family's betrayal backfires. |

The returned analysis characterizes the visuals as first-person parkour in blocky game worlds and reports continuous spoken story narration. It does **not explicitly identify Minecraft by official game metadata**; classification rests on rendered scene descriptions and original page/source context. The scene labels supplied by the model (e.g. “Product Selling Points”) appear generic and are not adopted as story-structure labels.

## Cross-source consistency and unresolved conflicts

- The owner's [first inspection note](owner-inspection-notes-2026-11-14.md) and [follow-up](owner-inspection-N3-followup-2026-11-14.md) reported parkour, narration, and speech-matched captions at checked points. These are **owner-reported**, not independently authenticated.
- The external AI analysis separately returned an opening about family betrayal and revenge, mid-story transfer of valuable contracts/assets, and an ending where family betrayal backfires; these align closely with the owner's recollections. This is corroborating **content-summary consistency**, not proof that either transcript is verbatim.
- The Researcher's browser/page metadata for N3 earlier reported **1:20** (source-reported player duration). External AI scene segmentation's last timestamp is **1:21**; these are different measurements/estimates and should **not** be silently reconciled or treated as independent frame-accurate proof of duration.
- **No synchronized caption sample, caption text coordinates, actual screen frame capture, caption timing or per-word alignment was included in the external analysis response.** Therefore an independent caption-sync claim remains unsupported; owner's check is still owner testimony.
- Views, publication date, channel identity, Shorts classification and licensing are **not independently corroborated by this AI analysis**; keep each separately sourced and dated. A public YouTube link is not permission to reuse the video.

## Proposed acceptance test before broad rollout

1. For an accessible public target candidate, call the same provider with its exact YouTube URL. Require `status=completed` and genuine video-specific timecodes and observed visual/audio descriptions; a queued job or generic prediction is not evidence.
2. Save provider job ID, retrieval date, raw technical status, source URL, scene timings and concise NON-verbatim observational summaries. Avoid posting copyrighted full voiceover transcripts in the public GitHub repository.
3. Cross-check the provider's output against source-reported player metadata and owner/permitted sample screenshots/inspection notes; especially verify whether **burned-in captions match actual spoken words** at beginning, middle and end. If no caption evidence, mark caption synchronization **UNKNOWN / OWNER-REPORTED**, not independently verified.
4. Make the Researcher label method and confidence for each individual claim. The Reviewer should independently inspect the returned source and determine whether this is sufficient for a **limited pilot**; do not auto-approve the original 30-example research target from one AI job.

**Workflow status:** Research still in revisions; no new `STUDIO-REVIEW-` PR, strategy authorization or publication was produced by this experiment.
