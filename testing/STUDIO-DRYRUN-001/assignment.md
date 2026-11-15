# STUDIO-DRYRUN-001 — Synthetic strategy pipeline test

**Type:** TEST_ONLY / SYNTHETIC SCENARIO — NOT REAL VERIFIED MARKET RESEARCH  
**Status:** Prepared; not yet executed or approved.  
**Authoritative real-task status:** `STUDIO-R001 = REVISIONS REQUIRED`; no strategy/production/publishing authorization for real project.  
**Workflow gate:** A future `pull_request opened` containing the literal title marker `STUDIO-DRYRUN-TASK-` in repo `victor12416/Studio`.  
**Stage to test:** STRATEGIST, followed by separate independent DRYRUN Reviewer (not the real R001 Reviewer).
**Date:** November 14, 2026.

## Scenario fixture

Studio plans to create *original* vertical YouTube Shorts with original/licensed Minecraft-style parkour gameplay footage as the background, an original narrated story, and speech-synchronized on-screen captions. TikTok may follow later.

For this one **synthetic rehearsal**, assume the Director requests a conceptual content format for a **45–70 second original mystery/revenge narrative**. The audience, engagement potential, category performance and ideal runtime are **unknown**; no evidence-based winner, competitor metrics, 30-video dataset, retention percentages or market trend is supplied. No fabricated or privately sourced statistics may be introduced.

The scenario is solely to test that Stage 1 delivers a structured strategic brief through GitHub and hands it off to a separate quality-control execution. It **does not replace** or resolve the rejected research in PR #2, PR #3, or PR #4.

## Strategist assignment: TEST_ONLY

1. Validate this is a GitHub opened PR in `victor12416/Studio` with exact title marker `STUDIO-DRYRUN-TASK-`, check PR number/URL/head SHA and read this entire file and PR body. Ignore all other PRs and events.
2. Act only as Studio **Strategist**, not the Reviewer, Scriptwriter or Producer. Do not research outside sources unless necessary to clarify a concrete requirement; the test is creative hypothesis development from a synthetic brief, **not empirical competitor research**.
3. Develop three **distinct** original-format concepts for the synthetic brief, varying narrative opening, tension/reveal and pacing. Explicitly label all audience claims as creative **hypotheses**.
4. Select one proposed concept and justify the choice for an initial hypothetical test, but **do not claim** that real-world evidence has established its performance.
5. Produce a clear test-ready strategy brief with 0–3 second hook idea, short structure beat map, approximate creative timing (not measured competitor runtime), caption style suggestion, originality/rights plan, key execution risks and a proposed future **measurement plan** (no fabricated actual metrics).
6. Include TEST_ONLY prominently on the first line and in output filenames. Preserve real R001 blocked status. Do not script entire video, create/modify footage, publish, alter other automations or merge anything.
7. Deliver a structured file `testing/STUDIO-DRYRUN-001/strategy-TEST_ONLY.md` on a **new** GitHub branch. Open a **new PR** containing the exact marker `STUDIO-DRYRUN-STRATEGY-REVIEW-` in the title and linking this original task PR+SHA. This output title must **not** contain `STUDIO-REVIEW-` (real Research Reviewer trigger), `STUDIO-RESEARCH-TASK-` (real Research Worker trigger) or `STUDIO-DRYRUN-TASK-` (loop).
8. Never emit `READY_FOR_REVIEW` as though this were real research. Include `TEST_ONLY — STRATEGY QC REQUEST` in the new PR description instead. Note that the dryrun independent Reviewer, not the Strategist, decides PASS_TEST / REVISE_TEST / FAIL_TEST.
9. Record the generated PR URL and commit SHA, then notify owner/Director of the **test** result; no Slack channel posts except the designated Studio test update if specifically authorized.

## Independent dry-run strategy review criteria

The separate dry-run Reviewer should evaluate, independently:
- It retrieved all changed files at the immutable PR head SHA, not just a truncated patch.
- The strategy brief remains explicitly TEST_ONLY and does not claim STUDIO-R001 was approved.
- Three concepts are genuinely different; one is prioritized with clear reasoning.
- Opening, narrative beats, caption approach, originality/rights, practical risks and measurement proposal are coherent and deliverable to the next hypothetical agent.
- No made-up competitor metrics, market statistics, retention performance or false evidence.
- No real production, publishing, copyrighted-asset reuse, merges or fake inter-agent communications.
- Decision as `PASS_TEST`, `REVISE_TEST` or `FAIL_TEST` with specific reasoned findings in a PR comment. This is a **test decision**, never independent approval of real research.

## Next stage after PASS_TEST

**STOP at the strategy review gate.** Do not automatically start real scriptwriting or production. Director will inspect the outcome and then create a separate `STUDIO-DRYRUN-SCRIPT-TASK-` workflow for Scriptwriter with distinct independent QC, followed by controlled Producer/publishing-preparation tests. Real publication stays disabled.

## Deduplication

Use `STUDIO-DRYRUN-001:<triggering PR number>:<head SHA>` as the identity key. Check whether a valid output PR already exists for the triggering event before creating branches/commits/PRs. Do not duplicate work for the same event.
