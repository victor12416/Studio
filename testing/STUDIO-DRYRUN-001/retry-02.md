# STUDIO-DRYRUN-001 — Attempt 2 Event-SHA Fallback Test

**Status:** TEST_ONLY, synthetic workflow test; no real research or publishing approval.  
**Original scenario:** [synthetic strategy assignment](assignment.md) on the same GitHub branch.  
**Reason for attempt 2:** The first GitHub event-triggered Strategist execution for PR #5 blocked because its webhook event omitted a pull-request head SHA; GitHub's API exposed a stable current SHA but the old instructions rejected that fallback. Both the existing Strategist and separate independent Reviewer automations were updated to pin to the GitHub API head SHA when the event omits it, with drift detection and honest provenance.

**Assignment:** Follow the complete original `testing/STUDIO-DRYRUN-001/assignment.md` synthetic scenario; generate three distinct creative concepts, select a hypothetical option, create a separate TEST_ONLY strategy review PR and await an independent TEST_ONLY decision. Do not claim actual industry performance or that STUDIO-R001 research was approved.

**Event provenance acceptance test:** For the future *opened* event for this retry PR, confirm repository/title/event action/PR number via authorized GitHub tools. If event SHA is missing, use the complete head SHA fetched from GitHub as the API-derived execution snapshot, document that this is not directly event-supplied, and check again for head changes before delivery. Any contradictory head revision or identity failure must still block.

**Isolation:** Do not reuse PR #5 as a fresh event. No merges, strategy approval, real media production or publishing. The existing independent Reviewer must assess the result.
