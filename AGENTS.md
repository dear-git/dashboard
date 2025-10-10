# Repository Guidelines

## Project Structure & Module Organization
The dashboard ships as a static single-page app. All markup, Tailwind-driven styling, and vanilla JS live in `index.html`, while image assets sit in `file/`. Keep new data fixtures and UI helpers close to their existing counterparts in the script block, and document major structures with brief inline comments. Store large media or downloadable exports alongside the existing images and reference them with relative paths.

## Build, Test, and Development Commands
Install-free preview works by opening `index.html` directly in a browser. For a realistic environment that mirrors production headers, run `python3 -m http.server 8000` (from this directory) and visit `http://localhost:8000`. Ensure an active network connection so the Tailwind CDN and Google Maps API load correctly; when offline, use browser dev-tools overrides or local stubs before committing.

## Coding Style & Naming Conventions
Use two-space indentation for HTML, CSS, and JavaScript, matching the current formatting. Favor Tailwind utility classes over bespoke CSS unless a style is reused extensively. Declare immutable values in `UPPER_SNAKE_CASE`, runtime objects in `camelCase`, and string-literal statuses as lowercase (`good`, `warning`, `critical`). Group related helper functions and keep site metadata alphabetized by `id` to ease diff reviews.

## Testing Guidelines
Automated tests are not yet wired up, so rely on targeted manual passes. Before opening a pull request, load the dashboard, clear the console, interact with at least three site pins (one per status), verify alert toasts animate, and export a CSV to confirm data integrity. Re-run the local server in an incognito window when tweaking CDN dependencies to catch caching issues.

## Commit & Pull Request Guidelines
Follow the repo norm: short, imperative summaries such as “Refine alert animations” or “Add Chiang Mai asset data.” Squash incidental assets into the same commit only when they directly support the feature. Pull requests should outline the problem, the solution, expected impact on battery metrics, and include screenshots or screen recordings for UI shifts. Link tracker issues when available and call out any manual verification steps you skipped.

## Security & Configuration Tips
Never commit production Google Maps keys; treat the checked-in key as a placeholder and rotate it if you expose the repo publicly. When sharing exports or screenshots, scrub sensitive site identifiers that extend beyond the anonymized Thai province naming used in `sites`.
