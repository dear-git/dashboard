# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

A single-page battery monitoring dashboard for 24 electrical substations across Thailand. All code (HTML, CSS, JavaScript) lives in `index.html` as a self-contained static application with no build process or external dependencies beyond a Tailwind CSS implementation.

## Development Commands

**Local development server:**
```bash
python3 -m http.server 8000
# Visit http://localhost:8000
```

**Direct preview:**
```bash
open index.html
# Works but lacks production-like headers
```

No build, test, or lint commands exist. Manual testing is required before changes.

## Architecture

### Web Development Fundamentals

This project demonstrates fundamental web technologies working together:

**HTML (HyperText Markup Language)** - Structure and content:
- Defines the document structure with semantic elements (`<div>`, `<button>`, `<table>`)
- Creates the DOM (Document Object Model) tree that browsers render
- Provides data attributes for JavaScript interaction (`data-site-id`)
- Includes inline SVG for icons and visual elements
- Role: The structural foundation - what content exists and how it's organized

**CSS (Cascading Style Sheets)** - Presentation and styling:
- Controls visual appearance (colors, layouts, animations)
- Uses Tailwind utility classes for rapid styling
- Custom animations (`@keyframes`) for floating pins and gradients
- Glass morphism effects with `backdrop-filter` and transparency
- Responsive design with grid layouts and media queries
- Role: The visual layer - how content looks and behaves visually

**JavaScript** - Behavior and interactivity:
- Manipulates the DOM dynamically (`document.getElementById()`, `createElement()`)
- Handles user interactions (clicks, touch events, keyboard navigation)
- Manages application state (current page, selected site, filters)
- Performs calculations (battery metrics, power consumption)
- Communicates between pages via `sessionStorage`
- Role: The logic layer - how content behaves and responds to users

### Single-File Application Structure

- **index.html** - Entire application in one file (~3400 lines):
  - HTML markup (lines 1-1245): Structural elements and containers
  - Embedded CSS (lines 7-1243): Styling, animations, and visual effects
  - Vanilla JavaScript (lines 1246-3400+): Application logic and interactivity
  - No external JS files, no npm, no bundler required

### Multi-Page Architecture

The application now consists of three interconnected pages:

1. **index.html** - Main dashboard with Thailand map
   - Primary entry point for users
   - Displays all 24 battery sites on interactive map
   - JavaScript manages map rendering and click handlers
   - CSS handles pin positioning and animations
   - HTML provides the container structure

2. **detail.html** - Individual battery site details
   - Receives site ID via URL parameters (`?id=1`)
   - JavaScript reads `URLSearchParams` and `sessionStorage`
   - CSS creates battery visual indicator with percentage fill
   - HTML structures the detailed metrics display
   - Includes fallback mock data when accessed directly

3. **db_view.html** - Database table viewer
   - Displays all sites in tabular format
   - JavaScript populates table rows dynamically
   - CSS provides hover effects and status colors
   - HTML defines table structure
   - Click handlers navigate to detail pages

### Data Flow Between Pages

```
index.html (Dashboard)
    ↓ [User clicks battery pin]
    ↓ [JavaScript stores site ID in sessionStorage]
    ↓ [window.open() or window.location.href]
    ↓
detail.html (Site Details)
    ↓ [JavaScript reads URL parameter: ?id=5]
    ↓ [JavaScript checks sessionStorage for site data]
    ↓ [Falls back to embedded mock data if needed]
    ↓ [JavaScript updates DOM with site information]
    ↓ [CSS styles the presentation]
```

### Separation of Concerns

Following web development best practices:

**Structure (HTML)**:
- Semantic elements define meaning
- IDs and classes provide JavaScript/CSS hooks
- Attributes store metadata (`data-*`)
- Forms handle user input

**Presentation (CSS)**:
- Visual styling separate from structure
- Reusable utility classes (Tailwind)
- Responsive layouts (grid, flexbox)
- Animations and transitions

**Behavior (JavaScript)**:
- Event listeners for interactivity
- DOM manipulation for dynamic updates
- State management for application data
- API integration (if needed)
- Navigation between pages

### Core Data Model

**BATTERY_SPEC** (line 1710) - System-wide battery specifications:
```javascript
{
  voltageString: 125,    // VDC
  capacityAh: 350,       // Amp-hours
  cells: 60,             // Cells per string
  voltagePerCell: 2.083  // ~125V ÷ 60 cells
}
```

**sites array** (line 1251) - Main data store containing 24 battery site objects:
```javascript
{
  id, name, province,           // Identity
  lat, lng,                     // Coordinates (for future mapping)
  status,                       // 'good'|'warning'|'critical'
  stateOfCharge,                // SoC % (primary health metric)
  stateOfHealth,                // SoH %
  voltagePerCell,               // ~2.08V per cell
  internalResistance,           // µΩ
  currentPerString,             // Amps
  voltagePerString,             // 125V
  ambientTemp,                  // °C
  battery, temp, voltage, power // Legacy fields (derived/redundant)
}
```

**provinceRegions** (line 1756) - Maps geographic regions to Thai province names:
```javascript
{
  'north': ['สถานีไฟฟ้าเชียงราย 2', ...],
  'northeast': [...],
  'central': [...],
  'south': [...]
}
```

### Key Functions

**Data normalization** (line 1717):
- `normalizeSiteMetrics()` - Derives voltage, power, and cell metrics from BATTERY_SPEC
- Always called on page load to ensure consistent calculations

**Status thresholds** (line 1862):
- `checkBatteryFailures()` - Alert logic:
  - Critical: SoC < 30%
  - Warning: SoC < 50% OR Temp > 40°C OR SoH < 70% OR Resistance > 500µΩ

**Rendering pipeline** (line 2093):
- `renderBatteryPins()` → `createMarkerElement()` - Generates CSS-positioned battery pins on Thailand map
- `getProvincePosition()` - Maps site provinces to pixel coordinates on CSS Thailand map
- `filterByRegion()` - Filters visible sites by geographic region

**Export** (line 2072):
- `exportToCSV()` - Generates timestamped CSV with all battery metrics

### How HTML, CSS, and JavaScript Work Together

**Example 1: Battery Pin Click Handler**

HTML provides the container:
```html
<div id="batteryPins"></div>
```

JavaScript creates interactive elements:
```javascript
const pinGroup = document.createElementNS('http://www.w3.org/2000/svg', 'g');
pinGroup.addEventListener('click', (e) => {
  sessionStorage.setItem('bmsSelectedSiteId', String(siteId));
  window.open(`detail.html?id=${siteId}`, '_blank');
});
```

CSS styles the appearance:
```css
.battery-pin {
  cursor: pointer;
  transition: all 0.3s ease;
}
.battery-pin:hover {
  transform: scale(1.2);
}
```

**Example 2: Dynamic Status Badge**

HTML structure:
```html
<div class="status-badge" id="statusBadge">Loading...</div>
```

JavaScript updates content and class:
```javascript
const statusBadge = document.getElementById('statusBadge');
statusBadge.textContent = site.status.toUpperCase();
statusBadge.className = `status-badge status-${site.status}`;
```

CSS provides conditional styling:
```css
.status-good {
  background: rgba(34, 197, 94, 0.2);
  color: #22c55e;
}
.status-critical {
  background: rgba(239, 68, 68, 0.2);
  color: #ef4444;
}
```

**Example 3: Progress Bar with Dynamic Width**

HTML structure:
```html
<div class="progress-bar">
  <div class="progress-fill" id="socBar" style="width: 0%"></div>
</div>
```

JavaScript calculates and updates:
```javascript
const socBar = document.getElementById('socBar');
socBar.style.width = `${site.stateOfCharge}%`;
socBar.style.background = site.stateOfCharge >= 80 ? '#22c55e' : '#ef4444';
socBar.textContent = `${site.stateOfCharge}%`;
```

CSS provides layout and animation:
```css
.progress-bar {
  height: 24px;
  background: rgba(15, 23, 42, 0.8);
  border-radius: 12px;
}
.progress-fill {
  transition: width 0.5s ease;
  display: flex;
  align-items: center;
}
```

### State Management

**Global variables:**
- `sites` - Primary data array (mutable, updated via Add Asset modal)
- `currentFilter` - Active region filter ('north', 'south', etc.)
- `selectedSite` - Currently viewed site in detail modal
- `alertHistory` - Tracks alert cooldowns to prevent spam (30s default)

**Page routing:**
- `showHome()` / `showDetail(siteId)` - Simple show/hide page transitions
- No URL routing, no hash navigation

## Code Style

- **Indentation:** 2 spaces (HTML, CSS, JS)
- **Constants:** `UPPER_SNAKE_CASE` (e.g., `BATTERY_SPEC`)
- **Variables:** `camelCase`
- **Status literals:** lowercase strings ('good', 'warning', 'critical')
- **Styling:** Tailwind utilities over custom CSS unless reused extensively
- **Site ordering:** Alphabetize by `id` in sites array for clean diffs

## Testing Checklist

Before committing UI changes:
1. Open dashboard in browser, clear console
2. Test 3+ site pins (one per status color)
3. Trigger alert system with "Check Alerts" button
4. Export CSV and verify data integrity
5. Test in incognito if changing CDN dependencies

## Common Tasks

**Adding a new battery site:**
1. Locate `sites` array (line 1251)
2. Add new object with all required fields
3. Assign unique sequential `id`
4. Include site in `provinceRegions` mapping if new province
5. Add position coordinates in `getProvincePosition()` if new location

**Adjusting alert thresholds:**
1. Edit `checkBatteryFailures()` function (line 1862)
2. Modify conditional logic for Critical/Warning states
3. Update README.md to document new thresholds

**Changing battery specifications:**
1. Update `BATTERY_SPEC` object (line 1710)
2. All voltage/power calculations derive from this automatically
3. Update README.md battery specs section

**Modifying CSS Thailand map:**
1. Pin positions defined in `getProvincePosition()` (line 2232)
2. Coordinate system is percentage-based for responsive scaling
3. Test all 24 site pin placements after changes

## Security Notes

- No Google Maps API key is used (pure CSS map implementation)
- CSV exports may contain sensitive site data - verify before sharing
- Thai province names are considered non-sensitive identifiers
