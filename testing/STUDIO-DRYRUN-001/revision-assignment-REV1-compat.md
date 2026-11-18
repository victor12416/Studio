# TEST_ONLY — STUDIO-DRYRUN-001-REV1 — Legacy Webhook Compatibility Assignment

**task_type: STRATEGY_REVISION**

This is a synthetic revision assignment routed through the already-tested legacy task-title event filter to diagnose whether changing an existing ChatGPT event automation's prompt also changes its externally registered GitHub title filter. This file does NOT approve any real research or production.

**Original strategy assignment:** https://github.com/victor12416/Studio/pull/6 ; pinned SHA `d0b1e803ea9a1c63e9cf2a0076b938ab6cdf0e3f`.

**Reviewed strategy:** https://github.com/victor12416/Studio/pull/7 ; pinned report SHA `a64c671dbf7379b9c991ae01dca1a1a1cf84864b`.

**Complete independent Reviewer finding:** https://github.com/victor12416/Studio/pull/7#issuecomment-6899769951 — decision REVISE_TEST. Read its entire content before changes.

**Other pending revision assignment:** https://github.com/victor12416/Studio/pull/8 is the previously opened same-scope assignment, but its newer title marker did not visibly launch a worker run. This is a legacy-router diagnostic retry of that same correction scope, not permission to run two workers or create duplicate output. Check existing outputs from both before proceeding.

## Required procedure
1. Verify an actual, NEW `pull_request` event with action exactly `opened` for `victor12416/Studio`. Its *title* must have the legacy `STUDIO-DRYRUN-TASK-` marker and this file must be in its changed files. Verify canonical repository, URL, PR number, title, head commit, and task_type. If webhook omits head SHA, label API-fetched pinned full SHA as execution snapshot, not event-time proof; check drift.
2. Read full task PR description and this entire file at the pinned assignment SHA; read the whole original selected strategy report and the entire independent review on PR #7. Use original reviewed SHA, not current default branch.
3. Correct ONLY Concept A's synthetic experiment-measurement gap while preserving the other two story concepts, selected Concept A, hooks, beat maps, caption guidance, creativity, rights and limitations. Required P1 fixes:
    - Explicit falsifiable creative question contrasting contradictory-date opening against a defined same-story control hook; state which story/gameplay/voice/captions/runtime/publishing context to keep comparable.
    - Define one conditional primary metric with exact numerator, denominator, eligible segment/timepoint, and access-to-actual-analytics prerequisite. Don't invent metrics or per-viewer random assignment.
    - Propose relative observation window and clear eligibility/sufficiency criteria or pre-analysis procedure based on unknown variance; no fabricated baselines or winner thresholds.
    - Specify interpretive outcome rules, inconclusive results, confounds, limitations from nonrandom exposure/small samples, and an explicit fallback when metric unavailable.
4. Create ONE deterministic NEW branch **from original reviewed strategy SHA** `a64c671dbf7379b9c991ae01dca1a1a1cf84864b`. Change ONLY `testing/STUDIO-DRYRUN-001/strategy-TEST_ONLY.md` and any minimally essential new test metadata. Do NOT update PR #7 branch, main or PR #8.
5. Open ONE NEW PR targeting main, title containing only `STUDIO-DRYRUN-STRATEGY-REVIEW-` as the routing marker and prominently `TEST_ONLY`. Reference source by PR URL and SHA, task ID, full reviewer URL, source assignment PR URL and the source-execution key without repeating source title marker. NEVER include these forbidden markers in the OUTPUT PR title/body/report: `STUDIO-RESEARCH-TASK-`, `STUDIO-REVIEW-`, `STUDIO-DRYRUN-TASK-`, `STUDIO-DRYRUN-STRATEGY-REVISION-TASK-`, `STUDIO-DRYRUN-SCRIPT-TASK-` or `STUDIO-DRYRUN-SCRIPT-REVISION-TASK-`.
6. Independent Studio Universal Test Reviewer must review the actual revised strategy at submitted SHA and choose PASS_TEST, REVISE_TEST or FAIL_TEST. Worker never self-approves. Confirm new output PR only after actual creation; reviewer trigger or outcome must not be claimed prematurely.
7. Send one SIMPLE `#studio-handoffs` update with status, work done, next action and link if confirmed.

**Deduplication:** Check branches, open+closed PRs and comments for any prior revised output linked to STUDIO-DRYRUN-001-REV1 / PR #8 or this PR, and stop if complete. Do not produce duplicate corrections.

**Boundaries:** TEST_ONLY. Real STUDIO-R001 remains REVISIONS REQUIRED. No script creation, production, AI voice, videos, analytics collection, merge or publishing. The owner must authorize real publishing.
