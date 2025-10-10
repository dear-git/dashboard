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

- `index.html`: Main application file containing all HTML, CSS, and JavaScript
- `README.md`: Basic project description
- `.gitignore`: Git ignore file for macOS specific files
- `QWEN.md`: This documentation file

## Building and Running

This is a static HTML application that can be run directly in any modern web browser:

1. Simply open `index.html` in a web browser
2. The application will automatically load and initialize
3. An internet connection is required to load external dependencies (Tailwind CSS CDN and Google Maps API)

Alternatively, you can serve it via a local web server:

- Using Python: `python -m http.server 8000`
- Using Node.js: `npx serve .`
- Using PHP: `php -S localhost:8000`

## Development Conventions

The application follows these conventions:

- All code is contained in a single HTML file for simplicity
- Tailwind CSS is loaded via CDN for styling
- Google Maps API is dynamically loaded via CDN
- Vanilla JavaScript is used without any frameworks
- Thai names and locations are used for the battery sites
- Color-coded status system: green (≥80%), yellow (60-79%), red (<60%)
- Metric measurements include State of Charge (SoC), State of Health (SoH), voltage per cell, internal resistance, current per string, voltage per string, and ambient temperature
- Derived metrics assume a 125 VDC string built from 60 cells (~2.08 V per cell) with a nominal 350 Ah capacity

## Key Components

1. **Home Page**: Shows an overview map of Thailand with all battery sites
2. **Detail Page**: Shows detailed metrics for a selected battery site
3. **Alert System**: Automatically detects and reports battery issues
4. **Data Export**: Exports all battery data to a CSV file
5. **Asset Management**: Allows adding new battery assets to the system

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
 site name substation
 เชียงราย 2
 ลำปาง 3
 พิษณุโลก 6
 น่าน 1
 ท่าวุ้ง
 ชนแดน
 ชัยนาท
 อุดรธานี 3
 ขอนแก่น 3
 โพนพิสัย
 บรบือ
 วาปีปทุม
 เขื่องใน
 โรจนะ 3
 โรจนะ 4
 บางพระครู
 สมุทรสาคร 7
 สามพราน 4
 ถลาง 2
 ภูเก็ต 3
 กระบี่ 1
 หาดใหญ่ 2
 