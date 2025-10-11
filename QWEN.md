# Thailand Battery Monitoring Dashboard - QWEN Context

## Project Overview

This is a comprehensive battery monitoring dashboard application that provides real-time visualization of battery status across 24 locations throughout Thailand. The dashboard features an interactive map with custom battery pin markers that indicate the status of each battery site and provides detailed monitoring metrics when selected.

The application is built as a modern single-page application using HTML, CSS, and vanilla JavaScript with the following technologies:

- Tailwind CSS (via CDN)
- SVG-based interactive Thailand map
- Custom animations and styling using CSS
- Glass morphism UI design with gradient backgrounds
- Client-side routing for GitHub Pages compatibility
- Responsive design for all device sizes

## Key Features

- **Interactive Thailand Map**: Visualize battery sites across all regions of Thailand
- **Real-time Monitoring**: Track SoC, SoH, voltage, current, temperature, and resistance
- **Multi-page SPA**: Single-page application with virtual routing for all pages
- **Modern UI**: Glass morphism design with animated elements
- **Responsive Design**: Works on desktop, tablet, and mobile devices
- **Alert System**: Automatic failure detection and warnings
- **Data Export**: Export all metrics to CSV format
- **Asset Management**: Add new battery sites dynamically
- **GitHub Pages Optimized**: Fully compatible with static site hosting

## File Structure

```
├── index.html                    # Main SPA with all pages (home, detail, database)
├── detail.html                   # Original detail page (now virtual page in SPA)
├── db_view.html                  # Database view (now virtual page in SPA)
├── package.json                  # Node.js dependencies and scripts
├── README.md                     # Main project documentation
├── QWEN.md                       # This documentation file
├── DEPLOYMENT.md                 # Deployment guide
├── sql/
│   ├── bms.sql                   # Database schema
│   └── db_viewer.html            # SQL-based viewer
├── file/
│   ├── thailand-map.png          # Map background
│   └── thai.jpg                  # Additional assets
└── .gitignore                    # Git ignore file
```

## GitHub Pages Deployment

The application has been optimized to work seamlessly with GitHub Pages:

1. All navigation now uses client-side routing instead of file-based navigation
2. URL parameters are used to control page state (e.g., `?page=detail&id=5`)
3. Browser history is properly managed with pushState API
4. The application detects URL parameters on load to show the correct page
5. Separate HTML files (detail.html, db_view.html) are now virtual pages within the single index.html

To deploy to GitHub Pages:
1. Push your code to a GitHub repository
2. Go to repository Settings → Pages
3. Set source to "Deploy from a branch"
4. The application will be accessible at https://username.github.io/repository-name/

## Development and Build Process

### Prerequisites
- Node.js (optional, for development server tools)

### Local Development
```bash
# Install development dependencies
npm install

# Start development server
npm start

# Or with live reload
npm run dev
```

### Static File Generation
The application is already optimized for static hosting and requires no build process. All code is contained in static HTML/CSS/JS files that can be served directly.

## Development Conventions

The application follows these conventions:

- All code is contained in a single HTML file for simplicity (index.html)
- Tailwind CSS is loaded via CDN for styling
- SVG is used for map visualization
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
8. **Interactive Map**: SVG-based Thailand map with custom battery pin markers

## Architecture & Technical Implementation

### Architecture
- **Single Page Application**: All HTML, CSS, and JavaScript in `index.html` with virtual routing
- **Styling**: Tailwind CSS with custom animations and glass morphism effects
- **Mapping**: SVG-based Thailand map (fully self-contained, no external dependencies)
- **State Management**: Vanilla JavaScript with reactive rendering
- **Data Structure**: Array of site objects with comprehensive battery metrics
- **Routing**: Client-side routing with URL parameter handling

### Key Components
- **Battery Pins**: Interactive SVG map markers with hover tooltips and click interactions
- **Province Filters**: Clickable region labels for filtered site views
- **Alert System**: Notification system with customizable cooldown periods
- **Export Module**: CSV generation with timestamp and complete metrics
- **Asset Management**: Modal forms for adding new battery sites
- **Animation Effects**: Custom CSS animations for status indicators and pin movements

### Client-Side Routing Implementation
The application implements virtual routing using:
- `URLSearchParams` to read page parameters
- `window.history.pushState()` to update URLs without page reloads
- `popstate` event listener to handle browser back/forward navigation
- Virtual pages that render different content based on URL parameters

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