# Thailand Battery Monitoring Dashboard

A comprehensive single-page battery monitoring system for 24 electrical substations across Thailand, optimized for GitHub Pages deployment. The application features real-time monitoring, interactive Thailand map, and comprehensive battery metrics for substations nationwide.

## ✨ Features

- **Interactive Thailand Map**: Visualize battery sites across all regions of Thailand
- **Real-time Monitoring**: Track SoC, SoH, voltage, current, temperature, and resistance
- **Multi-page SPA**: Single-page application with virtual routing for all pages
- **Responsive Design**: Works on desktop, tablet, and mobile devices
- **Modern UI**: Glass morphism design with animated elements
- **Alert System**: Automatic failure detection and warnings
- **Data Export**: Export all metrics to CSV format
- **Asset Management**: Add new battery sites dynamically

## 🚀 Quick Start

### Prerequisites

- Node.js (optional, for local development tools) 
- Modern web browser

### Local Development

```bash
# Clone the repository
git clone <repository-url>
cd thailand-battery-monitoring-dashboard

# Install dependencies (optional, for local server)
npm install

# Start local development server
npm start
# or for live reload
npm run dev
```

Or simply open `index.html` directly in your browser.

### GitHub Pages Deployment

1. Push your code to a GitHub repository
2. Enable GitHub Pages in your repository settings
3. Select the `main` branch as source
4. Your site will be available at `https://<username>.github.io/<repository-name>/`

## 📁 Project Structure

```
├── index.html         # Main SPA with all pages (home, detail, database)
├── detail.html        # Original detail page (now virtual page in SPA)
├── db_view.html       # Database view (now virtual page in SPA)
├── sql/
│   ├── bms.sql        # Database schema
│   └── db_viewer.html # SQL-based viewer
├── file/
│   ├── thailand-map.png   # Map background
│   └── thai.jpg           # Additional assets
├── README.md
├── QWEN.md
├── DEPLOYMENT.md
├── package.json
└── .gitignore
```

## 🛠️ Tech Stack

- **HTML5**: Semantic markup and structure
- **CSS3**: Modern styling with animations and glass morphism effects
- **JavaScript (ES6+)**: Client-side logic and routing
- **VanillaJS**: No frameworks - lightweight and performant
- **Tailwind CSS**: Utility-first CSS framework
- **SVG**: Scalable vector graphics for map visualization
- **GitHub Pages**: Static site hosting

## 🗺️ Pages & Navigation

The application features a single-page architecture with the following virtual pages:

- **Home Page** (`/`): Main dashboard with Thailand map and all battery sites
- **Detail Page** (`?page=detail&id=5`): Individual battery site details
- **Database View** (`?page=database`): All monitoring data in table format

URL parameters control page state, enabling direct links to specific content.

## 📊 Battery Metrics

### Standard Configuration
- **System Voltage**: 125 VDC
- **Battery Capacity**: 350 Ah
- **Cell Configuration**: 60 cells per string
- **Nominal Cell Voltage**: 2.08 V

### Monitored Parameters
- **State of Charge (SoC)**: 0-100%
- **State of Health (SoH)**: 0-100%
- **Voltage per Cell**: 1.5-2.5V (±0.2% accuracy)
- **Temperature**: 0-99.5°C (±1.0°C accuracy)
- **Internal Resistance**: 100-60000 µΩ (±2.0% accuracy)
- **Current per String**: 0-700A (±2.0% accuracy)
- **Voltage per String**: 20-200V (±2.0% accuracy)
- **Ambient Temperature**: 0-99.5°C (±1.0°C accuracy)

## 🏭 Monitored Substations

### Northern Region
- สถานีไฟฟ้า เชียงราย 2 (Chiang Rai 2)
- สถานีไฟฟ้า ลำปาง 3 (Lampang 3)
- สถานีไฟฟ้า น่าน 1 (Nan 1)
- สถานีไฟฟ้า พิษณุโลก 6 (Phitsanulok 6)

### Northeastern Region
- สถานีไฟฟ้า อุดรธานี 3 (Udon Thani 3)
- สถานีไฟฟ้า ขอนแก่น 3 (Khon Kaen 3)
- สถานีไฟฟ้า โพนพิสัย (Phon Phisai)
- สถานีไฟฟ้า บรบือ (Borabue)
- สถานีไฟฟ้า วาปีปทุม (Wapi Pathum)
- สถานีไฟฟ้า เขื่องใน (Khueang Nai)

### Central Region
- สถานีไฟฟ้า ท่าวุ้ง (Tha Wung)
- สถานีไฟฟ้า ชนแดน (Chon Daen)
- สถานีไฟฟ้า ชัยนาท (Chai Nat)
- สถานีไฟฟ้า โรจนะ 3 (Rojana 3)
- สถานีไฟฟ้า โรจนะ 4 (Rojana 4)
- สถานีไฟฟ้า บางพระครู (Bang Phra Khu)
- สถานีไฟฟ้า สมุทรสาคร 7 (Samut Sakhon 7)
- สถานีไฟฟ้า สามพราน 4 (Sam Phran 4)

### Southern Region
- สถานีไฟฟ้า ถลาง 2 (Thalang 2)
- สถานีไฟฟ้า ภูเก็ต 3 (Phuket 3)
- สถานีไฟฟ้า กระบี่ 1 (Krabi 1)
- สถานีไฟฟ้า หาดใหญ่ 2 (Hat Yai 2)
- สถานีไฟฟ้า ฉลุง (Chalung)
- สถานีไฟฟ้า ปัตตานี 2 (Pattani 2)

## 🚨 Alert System

The dashboard features automatic monitoring and alerts:

- **Critical**: SoC < 30%
- **Warning**: SoC < 50%, Temp > 40°C, SoH < 70%, Resistance > 500µΩ
- **Normal**: SoC ≥ 80%

### Cooldown Period
- 2-minute cooldown between identical alerts to prevent spam

## 📅 Deployment

### GitHub Pages Setup
1. Push your code to the `main` branch
2. Go to repository Settings → Pages
3. Set source to "Deploy from a branch"
4. Select "main" branch and "/ (root)" folder
5. Your site will be available at `https://<username>.github.io/<repository-name>/`

### Direct Links
- Home: `https://<username>.github.io/<repository-name>/`
- Detail: `https://<username>.github.io/<repository-name>/?page=detail&id=5`
- Database: `https://<username>.github.io/<repository-name>/?page=database`

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

If you encounter any issues, please open an issue in the GitHub repository.

---
Built with ❤️ for Thailand's energy infrastructure monitoring