# TEST_ONLY — Studio Synthetic Scriptwriter Assignment

**task_id: STUDIO-DRYRUN-SCRIPT-001**
**task_type: SCRIPTWRITER**
**status: ASSIGNED / NOT YET REVIEWED**
**role: Studio Universal Test Worker, Scriptwriter mode only**
**recipient after delivery: Studio Universal Test Reviewer, SCRIPT-QC-001 mode**

## Authorized source and independent gate

The Director authorizes ONE *synthetic* screenplay-style narration draft to test universal worker-to-independent reviewer routing. This is a **TEST_ONLY** exercise. It is not an actual production start, a publishing authorization, or an approval of the real STUDIO-R001 research.

- Source approved-for-test strategy: [PR #10](https://github.com/victor12416/Studio/pull/10)
- Exact reviewed strategy SHA: `3479a40f08a7302ed1332cc7c739145c6ecfaffc`
- Exact source strategy file at SHA: `testing/STUDIO-DRYRUN-001/strategy-TEST_ONLY.md`
- Independent reviewer: [PASS_TEST on PR #10](https://github.com/victor12416/Studio/pull/10#issuecomment-6969557804)
- Full source assignment and creative category: Concept A, **The Missing Medal**, original evidence-puzzle mystery with a fair, nonviolent revenge/restitution outcome.
- Real task `STUDIO-R001`: **REVISIONS REQUIRED**, unchanged.

Verify the complete actual PASS_TEST comment and complete strategy file directly at source SHA before starting. This test approval clears only the *synthetic* strategy stage; it is not approval to produce media or publish. Source PR must still match the verified SHA, or stop with an integrity blocker.

## Event routing (legacy subscription compatibility)

The existing ChatGPT automation's GitHub subscription was proven to process newly opened PR titles carrying its **legacy assignment-routing marker**, even when new markers introduced only in the prompt did not visibly fire. This task deliberately uses that legacy PR-title marker. **Do not classify this as a STRATEGIST task:** this file declares `task_type: SCRIPTWRITER` and exact `task_id: STUDIO-DRYRUN-SCRIPT-001`. This source-specific SCRIPTWRITER override is expressly configured in the existing Universal Worker; use it only here.

Process only GitHub pull_request event `opened` for canonical repository `victor12416/Studio`, and this new task PR; verify event/PR ID, source title, URL and complete pinned 40-character head SHA via API if webhook omits it, label any API-derived snapshot honestly and check drift. Read **entire task PR body and all changed assignment files** at pinned SHA. Do not process comments/edits/reopen as new tasks.

## What the Scriptwriter must create (ONE story)

**Working title:** *The Missing Medal*

**Creative constraint:** Original fictional 45–70 second narrated story designed around the selected Concept A's **60-second** beat map. Target a natural, plausible 60-second reading; estimate total spoken word count and speaking rate; do not pretend the recording exists or give false word-perfect caption timing.

- **0–3s hook:** The winner notices the medal has the **wrong date**, phrased so the contradiction is immediately graspable.
- **3–12s:** Establish community contest winner, ownership stakes, no more characters than necessary.
- **12–26s:** Seed TWO independently comprehensible audible clues pointing toward a swapped replica. Do not rely on the viewer seeing Minecraft footage or reading unspoken on-screen text.
- **26–38s:** Plausible wrong explanation, tested against known facts.
- **38–50s:** Final fair clue logically connects evidence to a trusted organizer's switch; reveal must be earned from previously spoken clues, not psychic knowledge or an offscreen confession.
- **50–57s:** Recover original medal and impose proportionate, nonviolent accountability. No violent revenge, humiliation campaign, doxxing, harassment or identifiable real people.
- **57–60s:** Brief satisfying callback to the wrong date.

Use **first-person narration** with a concise voice appropriate for a YouTube Short over *original/licensed* Minecraft parkour gameplay. The gameplay is background only; original story must be fully understood without looking at footage. Deliver actual original narrated script text, not only an outline, and keep exactly one coherent canon story.

## Deliverables (on ONE new branch)

1. `testing/STUDIO-DRYRUN-SCRIPT-001/script-TEST_ONLY.md` — original complete narration with readable segment timing, full continuous voiceover text, estimated words/rate and honest runtime uncertainty, source citations (PR references), short originality/rights/casting notes, TEST_ONLY and unapproved-real-research warnings.
2. `testing/STUDIO-DRYRUN-SCRIPT-001/caption-plan-TEST_ONLY.md` — provisional line/phrase caption chunks with **approximate** timestamps aligned to exact words in the narration; concise readable on-screen text, emphasis rules, vertical-safe-area policy and instruction that final timings must be adjusted to an actual recorded voice track. Do NOT create actual audio, videos, SRT timing claims, screenshots or 3rd-party asset licenses.

**Quality checks before submission:** Count narration words, assess spoken plausibility around 60 seconds; compare beat map to source; ensure no clues are visible-only; check semantic continuity and ending; caption chunks must be verbatim from script except clearly identified display styling, and no captions that contradict narration; readability on small phones; avoid more than one simultaneous complex caption line; explain uncertainty/rights. Do not fabricate views, retention data or claim full media exists.

## Routing and duplicate prevention

Use deterministic new branch based on repository `main` (DO NOT alter source PR #10 branch, previous PR #7, PR #9, or assignment branch). Write only the two test files under the script-test directory. Before creating anything, check repository open/closed PRs and branches for this exact task ID + assignment PR + SHA and any existing output, including an uncertain partial run. If complete result already exists, report it and STOP; no duplicate commits/PRs.

Open ONE NEW PR targeting `main` and labeled TEST_ONLY. Because the existing Reviewer GitHub event subscription is proven for the old strategy-review title marker, the **title must contain the one legacy reviewer marker** `STUDIO-DRYRUN-STRATEGY-REVIEW-`, **plus the plain type tag** `SCRIPT-QC-001`. The type tag is NOT an additional webhook trigger marker. Example form:

`STUDIO-DRYRUN-STRATEGY-REVIEW-SCRIPT-QC-001 — TEST_ONLY Script Review`

The reviewer is source-specifically configured to interpret this PR as **SCRIPT QC**, not strategy QC, upon full source verification. The output PR title/body/file must NOT repeat the task PR's worker-routing marker or any unrelated event routing markers; reference this task PR by its URL, exact task ID and pinned SHA, not copied title. Include source strategy PR #10, its reviewed SHA, exact full PASS_TEST review URL, deliverable filenames, approximate length and limitations, and the requested independent reviewer. Check source PR SHA and assignment source SHA for drift before PR delivery.

## Required boundaries

No real competitor research, no script publishing, no voice generation, no video editing/rendering, no experimental analytics, no merge and no live audience exposure. No claims of real authorizations. This is strictly a workflow test. The **independent Reviewer** must choose its own PASS_TEST / REVISE_TEST / FAIL_TEST and post a complete review with actual inspected file coverage. The Worker cannot approve its own script. Owner publishing approval remains required for any future real production.

**Owner update:** Send exactly one simple status to verified Slack `#studio-handoffs` at task conclusion with DONE/NEEDS FIX/BLOCKED, what happened, next action, and the real PR link; label TEST_ONLY. If unavailable, report the Slack failure honestly.
