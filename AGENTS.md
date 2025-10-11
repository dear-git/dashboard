# Repository Guidelines

## Project Structure & Module Organization
- Single‑page app: all HTML, Tailwind utilities, and vanilla JS live in `index.html`.
- Assets reside in `file/` (e.g., `file/logo.png`, exports). Use relative paths.
- Small data fixtures and UI helpers go inside the `<script>` of `index.html`. Keep related helpers grouped and site metadata alphabetized by `id`.

## Build, Test, and Development Commands
- Local preview: open `index.html` directly in a browser.
- Serve with prod‑like headers: `python3 -m http.server 8000` then visit `http://localhost:8000`.
- CDN deps require network. When offline, use dev‑tools overrides or temporary local stubs; do not commit real keys.

## Coding Style & Naming Conventions
- Indentation: 2 spaces for HTML, CSS, and JS.
- Prefer Tailwind utilities; add bespoke CSS only for widely reused patterns.
- Naming: constants `UPPER_SNAKE_CASE`, runtime objects `camelCase`, status strings lowercase (`good`, `warning`, `critical`).
- Centralize battery math in `BATTERY_SPEC` (125 VDC, 350 Ah, 60 cells). Derive voltage/current/power—avoid magic numbers.

## Testing Guidelines
- No automated tests yet. Do targeted manual passes:
  - Load the dashboard and confirm no console errors.
  - Interact with at least three site pins (one per status).
  - Verify alert toasts animate.
  - Export a CSV and spot‑check data integrity.
- For CDN changes, re‑run the local server in an incognito window to avoid cache.

## Commit & Pull Request Guidelines
- Commits: short, imperative (e.g., "Refine alert animations", "Add Chiang Mai asset data"). Squash incidental assets that directly support the change.
- PRs: describe problem and solution, expected impact on battery metrics, screenshots/screen recordings for UI changes, linked issues, and note any manual checks skipped.

## Security & Configuration Tips
- Do not commit production Google Maps keys. The checked‑in key is a placeholder—rotate if exposed.
- Scrub sensitive site identifiers in exports/screenshots; keep anonymized Thai province naming consistent in `sites`.

