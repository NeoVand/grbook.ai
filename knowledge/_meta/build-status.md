# Vault build status and how to resume

Last updated 2026-09-12. Workflow scripts live in `knowledge/_workflows/` and run with the Workflow tool
(`scriptPath` plus `args`).

## Done

- Phase 0: source manifests, reading copies, inventories (`knowledge/_tools/build_source_manifests.py`).
- Pilot dossiers: SCH ch05, GA ch11, DIV ch09 (verified).
- Legacy inventory: `knowledge/sources/legacy/*.json` and `overview.md` (336 assets).
- Course conventions: `knowledge/notation/course-conventions.md` (MTW, signature −+++).
- Tutor research: `docs/research/openai-live-voice-and-elevenlabs.md`; design note `knowledge/_meta/tutor-access-design.md`.

## In progress when this note was written

The four parallel batches were stopped to protect the usage limit (46 dossiers on disk: 4 verified, 42 read but not
yet verified). The remaining 48 units are being read in **read-only mode, 2 at a time** (`read_only: true`,
`concurrency: 2`). Verification of all read-only dossiers happens after the usage limit resets, most important first.

**Pacing rule from now on:** at most 5 agents in flight per run, one run at a time (raised from 2 by the user on 2026-09-13).

**Automatic resume (session-only):** an hourly job at :07 checks `knowledge/_tools/workflow_alive.py`; when no run is
active it launches the next 20 units from `phase1_status.py --next 20 --verify-after 2026-09-13T03:00` (reading first,
then verification after the 3 am reset). It stops itself when phase 1 is verified and asks before phase 2. It lives
only in the running Claude session and expires after 7 days; if the session closes, resume manually with the same
two commands.

## Resume

1. **Finish phase 1.** `python3 knowledge/_tools/phase1_status.py --args` prints one args object per line.
   Run `knowledge/_workflows/gr-dossiers-batch.js` once per line (in parallel). Units whose JSON exists but has no
   `verification` object go to `verify_only`; units without JSON go to `units`. Repeat until everything is verified.
2. **Book profiles and QA.** Run `knowledge/_workflows/gr-book-profiles-and-qa.js` (no args). Fix any units QA reports.
3. **Concept candidates.** `python3 knowledge/_tools/collect_concept_candidates.py` and note the cluster count.
4. **Concept registry.** Run `knowledge/_workflows/gr-concept-registry.js` with `{"cluster_count": <N>}`.
   Check with `python3 knowledge/_tools/check_registry.py`.
5. **Concept notes.** Build batches from the registry (3 concepts per batch for prerequisite/foundation/core tiers,
   5 for advanced/frontier), split into several args sets of about 25 batches, and run
   `knowledge/_workflows/gr-concept-notes-batch.js` for each set in parallel (each workflow runs 8 agents at a time).
   Then `python3 knowledge/_tools/render_concept.py --indexes`.
6. **Later phases (not yet scripted):** pedagogy catalogs (analogies, misconceptions, demos, examples, history,
   glossary), notation crosswalk per book, curriculum and prerequisite DAG with learning paths, tutor indices and
   retrieval functions, completeness review.
