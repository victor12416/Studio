# TEST_ONLY — STUDIO-DRYRUN-001-REV1 Strategy Revision Assignment

**Status:** PREPARED / NOT TRIGGERED. A correction task for a *synthetic* Studio strategy test; **not real approved research or production**.  
**Recipient:** Automated **Studio Dryrun Strategy Revision Worker** only.  
**Original test:** STUDIO-DRYRUN-001.  
**Repository:** `victor12416/Studio`.  
**Source Strategist assignment:** [PR #6](https://github.com/victor12416/Studio/pull/6); pinned head `d0b1e803ea9a1c63e9cf2a0076b938ab6cdf0e3f`.  
**Rejected-for-revision strategy:** [PR #7](https://github.com/victor12416/Studio/pull/7); reviewed head `a64c671dbf7379b9c991ae01dca1a1a1cf84864b`.  
**Independent Reviewer decision:** [REVISE_TEST on PR #7](https://github.com/victor12416/Studio/pull/7#issuecomment-6899769951).
**Existing strategy file:** `testing/STUDIO-DRYRUN-001/strategy-TEST_ONLY.md`.  
**Original real research status:** `STUDIO-R001 = REVISIONS REQUIRED`, unchanged.

## Purpose

Correct the *specific P1 defect* found by the independent Reviewer and test the automatic **revision worker → corrected strategy PR → independent Reviewer** handoff. A favorable *synthetic* review does not authorize real strategy, scripts, media, publishing or real research advancement.

## Required inputs and verification

1. Confirm trigger is an actual *new* GitHub `pull_request` event with action exactly `opened`, repository `victor12416/Studio`, PR title containing the exact marker `STUDIO-DRYRUN-STRATEGY-REVISION-TASK-`, and this complete assignment as a changed file. Ignore unrelated events.
2. Verify repository identity, PR number, URL, canonical title and 40-character pinned head SHA. If the event omits head SHA, retrieve the live PR head through authorized GitHub API, clearly label it **API-derived snapshot**, check initial PR creation/commit history for evidence of head changes, pin all reads to the SHA and recheck drift before delivery; stop if any mismatch or post-open revision.
3. Read this ENTIRE assignment file, full triggering PR description, full source strategy report at reviewed SHA `a64c671dbf7379b9c991ae01dca1a1a1cf84864b`, and COMPLETE independent Reviewer comment `#issuecomment-6899769951`; do not rely on excerpts or summaries.
4. Verify exact original concept and reviewed strategy source SHA. If the reviewed content differs, stop with an integrity blocker. Check for prior completed work from this source assignment PR+SHA to avoid duplicates.

## P1 corrections (required; all four)

The Reviewer judged the three concepts and Concept A / **The Missing Medal** usable, but its hypothetical measurement section too vague. Correct only the measurement-related gap in the existing strategy, plus minor clarity cross-references where necessary:

1. **Precise experimental question and treatment:** Define one falsifiable creative hypothesis tied to Concept A's early contradictory-date hook. Propose a suitable alternative/control version of the **same original story**, specifying exactly what differs (hook structure/phrasing) and which important elements should remain the same or comparable (story beats, runtime range, gameplay/source footage rights, voice, caption format, publishing context). Do not assert algorithmic randomized allocation that is not supported; discuss what causal conclusions are unavailable without controlled exposure.
2. **Primary operational metric:** Pick **one** plausible primary indicator linked to the hypothesis (for example hook-stage retention if the creator's actual authorized analytics UI exposes the required aggregated timestamped retention, or viewed-vs-swiped if that is the available indicator). Define the numerator, denominator, eligibility rules and **timepoint/segment**, and clearly state **metric access must be checked before any later execution**. If numerator/denominator cannot be verified, specify a contingent substitute or flag design as not executable, never invent per-viewer exposure data.
3. **Observation window and eligibility:** Propose a comparable analysis window relative to each hypothetical upload and explicit minimum-data/eligibility criteria or a pre-experiment procedure to derive a defensible sample size after baseline/variance checks. Do NOT invent an empirical baseline, arbitrary winning threshold, exact required exposure number, or claim analytics were actually collected.
4. **Interpretation:** State what directional result would favor the proposed hook, which outcomes are **inconclusive**, how confidence/uncertainty and multiple uncontrolled factors should affect conclusions, and how to proceed if primary metric is unavailable. Explicitly describe confounders, missing data, non-random distribution, small samples, and non-causal interpretation where applicable.

Keep all required original content: **three distinct categories/concepts, one selected A, hooks, beat maps, captions, risk/rights, limitations, measured vs hypothetical distinction**. Do not turn this into a finished story script or actual production plan. No fake competitor measurements, retention percentages, actual A/B test results, evidence, or numeric success claims.

## Output procedure (avoid duplicate loops)

1. First inspect existing open/closed PRs, source assignment comments, and expected deterministic branches for this exact correction task ID and pinned source SHA. Do not duplicate completed work. Use a deterministic **NEW branch** such as `studio-dryrun-strategy-rev/pr-<assignment-number>-<assignment-head-sha>`, **starting from the reviewed strategy report commit** `a64c671dbf7379b9c991ae01dca1a1a1cf84864b`. Do not update the rejected submission's PR #7 branch or any other existing branch.
2. Update just `testing/STUDIO-DRYRUN-001/strategy-TEST_ONLY.md` on your new branch. The revision must be complete and the file must still begin with TEST_ONLY.
3. Open **ONE NEW** PR targeted to `main` with title containing `STUDIO-DRYRUN-STRATEGY-REVIEW-001-REV1` and prominently labeled TEST_ONLY. This is intentionally a *new opened-PR event* so the **existing independent Studio Dryrun Strategy Reviewer** can assess the corrected strategy automatically. No new Reviewer automation or manually authored approval.
4. The **new output PR title, body and changed strategy file must NOT contain** these unrelated literal routing markers: `STUDIO-REVIEW-`, `STUDIO-RESEARCH-TASK-`, or `STUDIO-DRYRUN-TASK-`. It must also NOT contain the correction-task routing marker `STUDIO-DRYRUN-STRATEGY-REVISION-TASK-` anywhere in output title/body/file; reference source PR by URL, task ID and SHA instead.
5. The correction PR must cite original PR #7 / reviewed SHA, the exact complete Reviewer comment URL, this correction assignment PR URL / head SHA (URLs only, no literal excluded marker), and the deduplication key `STUDIO-DRYRUN-REVISION:victor12416/Studio#<assignment-number>:<full-head-SHA>`. State exactly which four correction items changed and any remaining limitations. Keep previous PR #7, source assignment PRs and real R001 state unchanged.
6. If source SHA/drift, rights, or required tools prevent completion, report a specific blocker; never claim review or success occurred when it did not. Once output PR opens, wait for a **separate** Reviewer automation and report the new PR URL in the owner notification. No merging, no production, no publishing.

## Quality-control gate

The independent Reviewer should evaluate the **actual corrected file at the new PR head SHA** and issue only `PASS_TEST`, `REVISE_TEST` or `FAIL_TEST` in its own comment. `PASS_TEST` would mean **only** that this synthetic strategy stage is fit to use in a *separately authorized* next agent test. Real STUDIO-R001 remains **REVISIONS REQUIRED**.

**Director next action after QC:** if `PASS_TEST`, set up a separate **TEST_ONLY Scriptwriter → independent Script Reviewer** pipeline. If `REVISE_TEST`, issue another scoped correction task; do not bypass the gate.
