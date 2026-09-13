# Vault build status and how to resume

Last updated 2026-09-13. Workflow scripts live in `knowledge/_workflows/` and run with the Workflow tool
(`scriptPath` plus `args`).

**Pacing rule:** at most 5 agents in flight, one workflow at a time.

## Done

- **Phase 0 (source manifests):** reading copies and inventories.
- **Phase 1 (chapter dossiers):** 94 dossiers, all verified, plus book profiles and QA.
- **Legacy inventory:** 336 assets (`sources/legacy/`).
- **Concept registry:** 1,370 concepts in 24 domains (`concepts/<domain>/_registry.json`), with 0 check errors.
- **Course conventions:** `notation/course-conventions.md`.
- **Standard v2** (2026-09-13), which replaces the book-centred pilot notes:
  - writing guide `_meta/writing-guide.md`;
  - schemas `_schemas/concept-note.schema.json` and `_schemas/visual.schema.json`;
  - exemplars `concepts/curvature/holonomy.json` and `visuals/carry-an-arrow-around-a-loop.json`.

## Now

Concept notes, domain by domain, followed by that domain's visuals. Curvature goes first as the v2 pilot, because 14
of its concepts have older drafts to mine. After curvature, the domains follow taxonomy order.

## Resume

1. **Write the notes for a domain.**
   - Run `python3 knowledge/_tools/make_note_batches.py --domain <id>`. It prints a summary line, then one args object.
   - Run `knowledge/_workflows/gr-concept-notes-v2.js` with that args object. Each batch of 4 concepts goes through a
     writer, a novice-reader review and a physics review.
   - Re-run both commands until the summary says 0 pending.
2. **Build the domain's visuals.** Run `knowledge/_workflows/gr-visuals-v2.js` with `{"domain": "<id>"}`. It plans
   canonical ids, writes catalog entries, and reviews them.
3. **Sync and check.** Run these commands in order:
   - `python3 knowledge/_tools/sync_registry.py --domain <id> --write`
   - `python3 knowledge/_tools/check_registry.py`
   - `python3 knowledge/_tools/render_concept.py --indexes`
   - `python3 knowledge/_tools/render_visual.py --index`
4. **Commit and push** to main.

## Later phases

These are not scripted yet:

- curriculum: learning paths and modules over the prerequisite DAG, at several entry levels;
- tutor indices and retrieval functions over concepts and visuals;
- a completeness review;
- an app pivot from book-unit pages to concept and lesson pages.
