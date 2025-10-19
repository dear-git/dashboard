# Repository Guidelines

## Build/Test Commands
- `npm start` - serve with http-server and open browser
- `npm run dev` - live-server with hot reload
- `python3 -m http.server 8000` - alternative static server
- Manual testing: load dashboard, check console, interact with site pins, verify CSV export

## Code Style & Structure
- Single-page app: all HTML/CSS/JS in `index.html`
- Indentation: 2 spaces for HTML, CSS, and JS
- Naming: constants `UPPER_SNAKE_CASE`, runtime objects `camelCase`, status strings lowercase
- Prefer Tailwind utilities; custom CSS only for reusable patterns
- Group related helpers in `<script>` section; alphabetize site metadata by `id`
- Centralize battery math in `BATTERY_SPEC` (125 VDC, 350 Ah, 60 cells) - avoid magic numbers

## Import & Asset Guidelines
- Assets in `file/` with relative paths
- CDN deps require network; use dev-tools overrides when offline
- Never commit production API keys or secrets

## Error Handling
- Validate all user inputs before processing
- Use try-catch for async operations and API calls
- Provide user-friendly error messages via toast notifications

