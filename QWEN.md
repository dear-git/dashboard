# Battery Monitoring System - Thailand Dashboard

## Project Overview

This is a battery monitoring dashboard application that provides real-time visualization of battery status across 24 locations throughout Thailand. The dashboard features an interactive map with custom battery pin markers that indicate the status of each battery site and provides detailed monitoring metrics when selected.

The application is built as a single-page application using HTML, CSS, and vanilla JavaScript with the following technologies:

- Tailwind CSS (via CDN)
- Google Maps JavaScript API
- Custom animations and styling using CSS
- Glass morphism UI design with gradient backgrounds

## Key Features

- Interactive Thailand map with 24 battery site locations
- Color-coded battery pins indicating status (green=good, yellow=warning, red=critical)
- Real-time battery metrics including state of charge, state of health, voltage, current, temperature, and internal resistance
- Standardized 125 VDC / 350 Ah (60-cell) pack model applied across all sites
- Detailed view for each battery site with comprehensive metrics
- Alert system for critical and warning conditions
- Add new battery asset functionality
- Export data to CSV functionality
- Automatic battery failure detection and alerting
- Responsive design with glass-morphism UI elements

## File Structure

- `index.html`: Main application file containing all HTML, CSS, and JavaScript (now implements full client-side routing)
- `README.md`: Basic project description
- `.gitignore`: Git ignore file for macOS specific files
- `QWEN.md`: This documentation file
- `detail.html`: Original detailed view page (now integrated as virtual page in index.html)
- `db_view.html`: Database view of all monitoring data (navigates to index.html with parameters for GitHub Pages compatibility)
- `sql/bms.sql`: SQL schema and data for the battery management system
- `sql/db_viewer.html`: Alternative database viewer
- `file/thailand-map.png`: Background map image
- `file/thai.jpg`: Additional map image

## Building and Running

This is a static HTML application that can be run directly in any modern web browser:

1. Simply open `index.html` in a web browser
2. The application will automatically load and initialize
3. An internet connection is required to load external dependencies (Tailwind CSS CDN and Google Maps API)

Alternatively, you can serve it via a local web server:

- Using Python: `python -m http.server 8000`
- Using Node.js: `npx serve .`
- Using PHP: `php -S localhost:8000`

## GitHub Pages Deployment

The application has been updated to work properly with GitHub Pages:

1. All navigation now uses client-side routing instead of file-based navigation
2. URL parameters are used to control page state (e.g., `?page=detail&id=5`)
3. Browser history is properly managed with pushState API
4. The application detects URL parameters on load to show the correct page
5. Separate HTML files (detail.html, db_view.html) are now virtual pages within the single index.html

To deploy to GitHub Pages:
1. Push your code to a GitHub repository
2. Go to repository Settings → Pages
3. Set source to "Deploy from a branch" or "GitHub Actions"
4. The application will be accessible at https://username.github.io/repository-name/

## Development Conventions

The application follows these conventions:

- All code is contained in a single HTML file for simplicity
- Tailwind CSS is loaded via CDN for styling
- Google Maps API is dynamically loaded via CDN
- Vanilla JavaScript is used without any frameworks
- Sites are electrical substations with names in the format 'สถานีไฟฟ้า [Province] [Number]'
- Color-coded status system: green (≥80%), yellow (60-79%), red (<60%)
- Enhanced Battery Metrics:
  - Voltage per Cell: 1.5-2.5V (±0.2% accuracy)
  - Temperature: 0-99.5°C (±1.0°C accuracy)
  - Internal Resistance: 100-60000 µΩ (±2.0% accuracy)
  - Current per String: 0-700A (±2.0% accuracy)
  - Voltage per String: 20-200V (±2.0% accuracy)
  - State of Charge: 0-100%
  - State of Health: 0-100%
  - Ambient Temperature: 0-99.5°C (±1.0°C accuracy)
- Standardized 125 VDC / 350 Ah OPzV gel battery system across all sites
- Substations include: น่าน 1, เชียงราย 2, ลำปาง 3, พิษณุโลก 6, ท่าวุ้ง, ชนแดน, ชัยนาท, อุดรธานี 3, ขอนแก่น 3, โพนพิสัย, บรบือ, วาปีปทุม, เขื่องใน, โรจนะ 3, โรจนะ 4, บางพระครู, สมุทรสาคร 7, สามพราน 4, ถลาง 2, ภูเก็ต 3, กระบี่ 1, หาดใหญ่ 2

## Key Components

1. **Home Page**: Shows an overview map of Thailand with all battery sites
2. **Detail Page**: Shows detailed metrics for a selected battery site (virtual page within SPA)
3. **Database View**: Shows all monitoring data in table format (virtual page within SPA)
4. **Alert System**: Automatically detects and reports battery issues
5. **Data Export**: Exports all battery data to a CSV file
6. **Asset Management**: Allows adding new battery assets to the system
7. **Client-Side Routing**: URL-based navigation using pushState API for GitHub Pages compatibility

## Google Maps Integration

The application uses Google Maps JavaScript API to display battery locations with:

- Custom styling for the map to match the dark theme
- Custom battery pin markers with animation effects
- Automatic zoom and centering on Thailand
- Detailed view with zoomed map when a specific site is selected
- Marker clustering and highlighting on hover

## Battery Status Indicators

- **Good (Green)**: State of charge ≥80%
- **Warning (Yellow)**: State of charge 60-79%
- **Critical (Red)**: State of charge <60%

The status is reflected in both the map pins and detailed views.

## Technical Implementation

### Architecture
- **Single Page Application**: All HTML, CSS, and JavaScript in `index.html`
- **Styling**: Tailwind CSS with custom animations and glass morphism effects
- **Mapping**: Pure CSS-based Thailand map (no external map dependencies)
- **State Management**: Vanilla JavaScript with reactive rendering
- **Data Structure**: Array of site objects with comprehensive battery metrics

### Key Components
- **Battery Pins**: Interactive map markers with hover tooltips and click interactions
- **Province Filters**: Clickable region labels for filtered site views
- **Alert System**: Notification system with customizable cooldown periods
- **Export Module**: CSV generation with timestamp and complete metrics
- **Asset Management**: Modal forms for adding new battery sites

### Monitoring Logic
```javascript
// Alert thresholds
- Critical: SoC < 30%
- Warning: SoC < 50%, Temp > 40°C, SoH < 70%, Resistance > 500µΩ
- Good: SoC ≥ 80%
```

## Data Model

Each battery site includes:
```javascript
{
  id: number,                    // Unique identifier
  name: string,                  // Site name (Thai)
  province: string,              // Thai province
  lat: number, lng: number,     // Coordinates (for future mapping)
  status: 'good'|'warning'|'critical',
  battery: number,               // Legacy field (SoC %)
  temp: number,                  // Temperature (°C)
  voltage: number,               // System voltage (125V)
  current: number,               // Current (A)
  power: number,                 // Power (W)
  voltagePerCell: number,        // Cell voltage (~2.08V)
  internalResistance: number,    // Resistance (µΩ)
  currentPerString: number,      // String current (A)
  voltagePerString: number,      // String voltage (125V)
  stateOfCharge: number,         // SoC (%)
  stateOfHealth: number,         // SoH (%)
  ambientTemp: number           // Ambient temperature (°C)
}
```

## SQL Schema

The application includes a SQL schema for the battery management system:

```sql
-- Battery Management System Table Schema
CREATE TABLE IF NOT EXISTS public.bms (
    id SERIAL PRIMARY KEY,
    substation VARCHAR(255),
    substation_code VARCHAR(10),
    area VARCHAR(50),
    voltage_per_cell NUMERIC(10, 3),
    temperature_per_cell NUMERIC(10, 3),
    internal_resistance_per_cell NUMERIC(10, 3),
    current_per_string NUMERIC(10, 3),
    voltage_per_string NUMERIC(10, 3),
    state_of_charge NUMERIC(5, 2),      -- SoC (%)
    state_of_health NUMERIC(5, 2),      -- SoH (%)
    ambient_temperature NUMERIC(10, 3),
    recorded_at TIMESTAMP DEFAULT NOW()
);
```

## Database Viewers

Two database viewer implementations are provided:
1. `sql/db_viewer.html` - Standalone database schema and sample viewer
2. `db_view.html` - Data table viewer with integration from the main app

## Province Regions

The dashboard organizes sites by Thai geographic regions:
- **ภาคเหนือ (North)**: สถานีไฟฟ้าเชียงราย 2, สถานีไฟฟ้าลำปาง 3, สถานีไฟฟ้าน่าน 1
- **ภาคอีสาน (Northeast)**: สถานีไฟฟ้าอุดรธานี 3, สถานีไฟฟ้าขอนแก่น 3, สถานีไฟฟ้าโพนพิสัย, etc.
- **ภาคกลาง (Central)**: สถานีไฟฟ้าพิษณุโลก 6, สถานีไฟฟ้าชนแดน, สถานีไฟฟ้าชัยนาท, etc.
- **ภาคตะวันออก (East)**: Region support available
- **ภาคตะวันตก (West)**: Region support available
- **ภาคใต้ (South)**: สถานีไฟฟ้าถลาง 2, สถานีไฟฟ้าภูเก็ต 3, สถานีไฟฟ้ากระบี่ 1, etc.