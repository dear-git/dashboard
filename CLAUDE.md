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

### Single-File Application Structure

- **index.html** - Entire application in one file (~3000 lines):
  - HTML markup (lines 1-1240)
  - Embedded CSS with Tailwind utilities and custom animations (lines 8-950)
  - Vanilla JavaScript application logic (lines 1241-3400)
  - No external JS files, no npm, no bundler

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
