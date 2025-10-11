# Repository Guidelines

## Project Structure & Module Organization
- Single-page dashboard: all markup, Tailwind utility styling, and vanilla JS live in `index.html`. Images/assets in `file/`.
- Keep new data fixtures and UI helpers near existing ones inside the `<script>` block in `index.html` with brief inline comments.
- Store large media or downloadable exports alongside images in `file/` and reference via relative paths.

## Build, Test, and Development Commands
- Local preview (no install): open `index.html` directly in a browser.
- Serve with headers mirroring prod: `python3 -m http.server 8000` then visit `http://localhost:8000`.
- CDN dependencies: ensure network is active; when offline, use dev-tools overrides or local stubs before committing.

## Coding Style & Naming Conventions
- Indentation: 2 spaces for HTML, CSS, and JS.
- Prefer Tailwind utilities over custom CSS; only add bespoke CSS for widely reused patterns.
- Naming: constants `UPPER_SNAKE_CASE`, runtime objects `camelCase`, status strings lowercase (`good`, `warning`, `critical`).
- Centralize battery math in `BATTERY_SPEC` (125 VDC, 350 Ah, 60 cells); derive voltage/current/power from it—avoid magic numbers.
- Alphabetize site metadata by `id` to simplify diffs; group related helpers together.

## Testing Guidelines
- No automated tests yet; do targeted manual passes.
- Before PRs: load the dashboard, clear console, interact with at least three site pins (one per status), verify alert toasts animate, and export a CSV to confirm data integrity.
- When tweaking CDN deps, re-run the local server in an incognito window to avoid cache surprises.

## Commit & Pull Request Guidelines
- Commit messages: short, imperative (e.g., "Refine alert animations", "Add Chiang Mai asset data"). Squash incidental assets if they directly support the change.
- PRs: describe problem, solution, expected impact on battery metrics; include screenshots/screen recordings for UI changes; link tracker issues; note any manual checks skipped.

## Security & Configuration Tips
- Do not commit production Google Maps keys. The checked-in key is a placeholder—rotate if exposed.
- Scrub sensitive site identifiers in exports/screenshots; keep anonymized Thai province naming consistent in `sites`.
