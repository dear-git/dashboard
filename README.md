# Battery Monitoring System - Thailand

A comprehensive monitoring dashboard for battery assets across Thailand, featuring real-time status tracking, interactive mapping, and alert management.

## 🚀 Features

- **Real-time Battery Monitoring**: Track 24 battery sites across Thailand with detailed metrics
- **Interactive Thailand Map**: CSS-based interactive map with province regions and filtering
- **Status Management**: Visual indicators for Good (≥80%), Warning (60-79%), and Critical (<60%) battery states
- **Alert System**: Automated failure detection and notifications with cooldown management
- **Data Export**: CSV export functionality for analysis and reporting
- **Responsive Design**: Mobile-friendly interface using Tailwind CSS

## 🔋 Battery Specifications

- **System Voltage**: 125V DC
- **Battery Capacity**: 350Ah
- **Cell Configuration**: 60 cells per string
- **Voltage per Cell**: ~2.08V (125V ÷ 60 cells)
- **Spec Source**: Derived in code from the `BATTERY_SPEC` constant (125 VDC, 350 Ah, 60 cells)
- **Monitored Parameters**:
  - State of Charge (SoC)
  - State of Health (SoH)
  - Voltage per Cell
  - Internal Resistance
  - Current per String
  - Ambient Temperature

## 🏭 Substations List

The dashboard monitors 24 electrical substations across Thailand:

### สถานีไฟฟ้า (Electrical Substations)

- **เชียงราย 2** - Chiang Rai Substation 2
- **ลำปาง 3** - Lampang Substation 3  
- **พิษณุโลก 6** - Phitsanulok Substation 6
- **น่าน 1** - Nan Substation 1
- **ท่าวุ้ง** - Tha Wung Substation
- **ชนแดน** - Chon Daen Substation
- **ชัยนาท** - Chai Nat Substation
- **อุดรธานี 3** - Udon Thani Substation 3
- **ขอนแก่น 3** - Khon Kaen Substation 3
- **โพนพิสัย** - Phon Phisai Substation
- **บรบือ** - Bue Rue Substation
- **วาปีปทุม** - Wapi Pathum Substation
- **เขื่องใน** - Khueang Nai Substation
- **โรจนะ 3** - Rotjana Substation 3
- **โรจนะ 4** - Rotjana Substation 4
- **บางพระครู** - Bang Phra Khru Substation
- **สมุทรสาคร 7** - Samut Sakhon Substation 7
- **สามพราน 4** - Sam Phran Substation 4
- **ถลาง 2** - Thalang Substation 2
- **ภูเก็ต 3** - Phuket Substation 3
- **กระบี่ 1** - Krabi Substation 1
- **หาดใหญ่ 2** - Hat Yai Substation 2

## 🗺️ Map Regions

The dashboard organizes sites by Thai geographic regions:

- **ภาคเหนือ (North)**: สถานีไฟฟ้าเชียงราย 2, สถานีไฟฟ้าลำปาง 3, สถานีไฟฟ้าน่าน 1
- **ภาคอีสาน (Northeast)**: สถานีไฟฟ้าอุดรธานี 3, สถานีไฟฟ้าขอนแก่น 3, สถานีไฟฟ้าโพนพิสัย, สถานีไฟฟ้าบรบือ, สถานีไฟฟ้าเขื่องใน, สถานีไฟฟ้าโรจนะ 3, สถานีไฟฟ้าโรจนะ 4, สถานีไฟฟ้าวาปีปทุม, สถานีไฟฟ้าบรบือ
- **ภาคกลาง (Central)**: สถานีไฟฟ้าพิษณุโลก 6, สถานีไฟฟ้าชนแดน, สถานีไฟฟ้าชัยนาท, สถานีไฟฟ้าท่าวุ้ง, สถานีไฟฟ้าบางพระครู, สถานีไฟฟ้าสมุทรสาคร 7, สถานีไฟฟ้าสามพราน 4
- **ภาคตะวันออก (East)**: Region support available
- **ภาคตะวันตก (West)**: Region support available  
- **ภาคใต้ (South)**: สถานีไฟฟ้าถลาง 2, สถานีไฟฟ้าภูเก็ต 3, สถานีไฟฟ้ากระบี่ 1, สถานีไฟฟ้าหาดใหญ่ 2, สถานีไฟฟ้าฉลุง, สถานีไฟฟ้าปัตตานี

## 🛠️ Technical Implementation

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

## 🚀 Quick Start

### Prerequisites
- Modern web browser with JavaScript enabled
- Local HTTP server (recommended for full functionality)

### Installation
```bash
# Clone the repository
git clone <repository-url>
cd dashboard

# Serve locally (recommended)
python3 -m http.server 8000

# Or open directly in browser
open index.html
```

### Usage
1. Open `http://localhost:8000` in your browser
2. View all battery sites on the Thailand map
3. Click on province labels to filter by region
4. Click battery pins for detailed site information
5. Use "Add Asset" button to add new battery sites
6. Export data using the "Export Data" button
7. Check alerts periodically with "Check Alerts" button

## 📊 Data Model

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

## 🔧 Development

### File Structure
```
dashboard/
├── index.html          # Main application (HTML, CSS, JS)
├── README.md          # This documentation
├── AGENTS.md          # Development guidelines
└── file/             # Asset directory (if needed)
```

### Adding New Sites
1. Click "Add Asset" button in the UI
2. Fill in site details and battery specifications
3. Click "Add Asset" to save

### Customization
- **Provinces**: Update `provinceRegions` object
- **Positions**: Modify `getProvincePosition()` function
- **Alert Thresholds**: Adjust values in `checkBatteryFailures()`
- **Styling**: Modify CSS classes and Tailwind utilities

## 🐛 Troubleshooting

### Map Not Displaying
- Ensure JavaScript is enabled
- Check browser console for errors
- Verify CSS animations are supported

### Data Export Issues
- Allow browser downloads if prompted
- Check CSV file in Downloads folder

### Alerts Not Working
- Verify `ALERT_COOLDOWN_MS` setting
- Check console for JavaScript errors
- Ensure site status thresholds are met

## 📄 License

[Add your license information here]

## 🤝 Contributing

1. Follow the coding guidelines in `AGENTS.md`
2. Maintain two-space indentation
3. Use Thai province naming conventions
4. Test alerts, exports, and filtering
5. Update documentation for new features

---

**Last Updated**: Automated documentation generation from current HTML implementation

## 🌐 Static Site Generation & Deployment

- Supported generators (static output): Hugo, Gatsby, Next.js (static export), Nuxt.js (static generate), Eleventy, Vite (static builds), SvelteKit (static adapter).
- Front-end frameworks (when exported to static HTML/CSS/JS): React, Angular, Vue.js. CSS frameworks like Bootstrap are supported.
- GitHub Pages publishing methods:
  - Direct branch publishing: configure Pages to serve from `gh-pages`, `main` (root), or `docs/` in repository settings.
  - Typical flow for generators: build to `dist/` or `out/`, then push build output to the publishing branch.
- This repo (plain static site):
  - No build required. Ensure `index.html`, `detail.html`, `db_view.html`, and `file/` are present at repo root (or in `docs/`).
  - In GitHub → Settings → Pages: Source → Deploy from a branch → choose `main` and `/ (root)` (or `docs/`).
  - Use relative paths like `./detail.html` and `./db_view.html` to work under the repository subpath on Pages.
