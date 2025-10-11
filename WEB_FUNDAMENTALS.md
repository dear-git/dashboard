# Web Development Fundamentals

This document explains how HTML, CSS, and JavaScript work together in the Battery Monitoring System dashboard.

## The Three Pillars of Web Development

### HTML - Structure (The Skeleton)

**What it does**: Defines the structure and content of web pages

**Role in this project**:
- Creates the document structure with semantic elements
- Defines containers for battery pins, tables, and forms
- Provides IDs and classes for JavaScript/CSS targeting
- Stores data in attributes (`data-site-id`, `id`)

**Example from our dashboard**:
```html
<!-- HTML defines WHAT content exists -->
<div id="app"></div>
<div id="alertContainer"></div>
<button onclick="showAddAssetModal()">Add Asset</button>
<table>
  <thead>
    <tr><th>Site ID</th><th>Name</th></tr>
  </thead>
  <tbody id="siteTableBody"></tbody>
</table>
```

**Key Concepts**:
- **Elements**: Building blocks like `<div>`, `<button>`, `<table>`
- **Attributes**: Additional info like `id`, `class`, `data-*`
- **DOM**: Browser converts HTML into a tree structure that JavaScript can manipulate
- **Semantic HTML**: Using meaningful tags (`<header>`, `<nav>`, `<table>`)

---

### CSS - Presentation (The Skin)

**What it does**: Controls visual appearance and layout

**Role in this project**:
- Defines colors, sizes, spacing, and positioning
- Creates animations (floating battery pins, gradient backgrounds)
- Implements responsive layouts (grid, flexbox)
- Provides visual feedback (hover effects, transitions)

**Example from our dashboard**:
```css
/* CSS defines HOW content looks */
.battery-pin {
  position: absolute;
  transform: translate(-50%, -100%);
  cursor: pointer;
  transition: all 0.3s ease;
  animation: float 2.5s ease-in-out infinite;
}

.battery-pin:hover {
  transform: translate(-50%, -100%) scale(1.2);
  z-index: 100;
}

.status-good {
  background: rgba(34, 197, 94, 0.2);
  color: #22c55e;
  border: 2px solid #22c55e;
}

.status-critical {
  background: rgba(239, 68, 68, 0.2);
  color: #ef4444;
  border: 2px solid #ef4444;
}
```

**Key Concepts**:
- **Selectors**: Target elements (`.class`, `#id`, `element`)
- **Properties**: Visual characteristics (`color`, `width`, `margin`)
- **Box Model**: Content, padding, border, margin
- **Layouts**: Flexbox, Grid for positioning
- **Animations**: `@keyframes` for smooth transitions
- **Responsive Design**: Media queries for different screen sizes

---

### JavaScript - Behavior (The Muscles)

**What it does**: Makes pages interactive and dynamic

**Role in this project**:
- Responds to user actions (clicks, keyboard, touch)
- Updates the DOM dynamically
- Manages application state (current page, filters, selected site)
- Performs calculations (battery metrics, power)
- Communicates between pages (sessionStorage)
- Fetches and processes data

**Example from our dashboard**:
```javascript
// JavaScript defines HOW content behaves

// 1. DOM Manipulation - Create and update elements
function renderBatteryPins() {
  const container = document.getElementById('batteryPins');
  sites.forEach(site => {
    const pin = document.createElement('div');
    pin.className = 'battery-pin';
    pin.textContent = `${site.stateOfCharge}%`;
    container.appendChild(pin);
  });
}

// 2. Event Handling - Respond to user actions
pinGroup.addEventListener('click', (e) => {
  e.preventDefault();
  sessionStorage.setItem('bmsSelectedSiteId', String(siteId));
  window.open(`detail.html?id=${siteId}`, '_blank');
});

// 3. State Management - Track application data
let currentFilter = 'all';
let selectedSite = null;

function filterByRegion(region) {
  currentFilter = region;
  render();
}

// 4. Data Processing - Calculate metrics
function normalizeSiteMetrics(site) {
  const current = site.currentPerString || 140;
  site.power = parseFloat(((BATTERY_SPEC.voltageString * current) / 1000).toFixed(1));
  return site;
}

// 5. Navigation - Move between pages
function showDetail(siteId) {
  sessionStorage.setItem('bmsSelectedSiteId', String(siteId));
  window.location.href = `detail.html?id=${siteId}`;
}
```

**Key Concepts**:
- **Variables**: Store data (`let`, `const`)
- **Functions**: Reusable blocks of code
- **Events**: User interactions (click, hover, submit)
- **DOM API**: Methods to manipulate HTML (`getElementById`, `createElement`)
- **Storage**: Save data (`sessionStorage`, `localStorage`)
- **Async**: Handle timing and delays (`setTimeout`, `addEventListener`)

---

## How They Work Together

### Example 1: Battery Status Badge

**1. HTML provides structure:**
```html
<div class="status-badge" id="statusBadge">Loading...</div>
```

**2. CSS defines appearance:**
```css
.status-badge {
  padding: 12px 24px;
  border-radius: 8px;
  font-weight: 600;
  font-size: 1.2rem;
}

.status-good {
  background: rgba(34, 197, 94, 0.2);
  color: #22c55e;
}

.status-critical {
  background: rgba(239, 68, 68, 0.2);
  color: #ef4444;
}
```

**3. JavaScript makes it dynamic:**
```javascript
const statusBadge = document.getElementById('statusBadge');
statusBadge.textContent = site.status.toUpperCase();
statusBadge.className = `status-badge status-${site.status}`;
```

**Result**: Badge automatically shows "GOOD" in green or "CRITICAL" in red based on battery data.

---

### Example 2: Interactive Battery Pin

**1. HTML container:**
```html
<div id="batteryPins"></div>
```

**2. CSS styling:**
```css
.battery-pin {
  position: absolute;
  cursor: pointer;
  transition: transform 0.3s ease;
}

.battery-pin:hover {
  transform: scale(1.2);
}
```

**3. JavaScript creates and handles interaction:**
```javascript
function createBatteryPin(site) {
  const pin = document.createElement('div');
  pin.className = 'battery-pin';
  pin.style.left = `${site.x}%`;
  pin.style.top = `${site.y}%`;

  pin.addEventListener('click', () => {
    window.open(`detail.html?id=${site.id}`, '_blank');
  });

  return pin;
}
```

**Result**: User sees a styled pin, hovers to see it grow, clicks to navigate to details.

---

### Example 3: Dynamic Progress Bar

**1. HTML structure:**
```html
<div class="progress-bar">
  <div class="progress-fill" id="socBar" style="width: 0%"></div>
</div>
```

**2. CSS animation:**
```css
.progress-bar {
  width: 100%;
  height: 24px;
  background: rgba(15, 23, 42, 0.8);
  border-radius: 12px;
}

.progress-fill {
  height: 100%;
  transition: width 0.5s ease;
  border-radius: 12px;
}
```

**3. JavaScript updates dynamically:**
```javascript
const socBar = document.getElementById('socBar');
const percentage = site.stateOfCharge;

socBar.style.width = `${percentage}%`;
socBar.style.background = percentage >= 80 ? '#22c55e' : '#ef4444';
socBar.textContent = `${percentage}%`;
```

**Result**: Bar smoothly animates to show battery charge level with appropriate color.

---

## Data Flow in This Application

### 1. Page Load Sequence

```
Browser requests index.html
    ↓
HTML parsed → DOM tree created
    ↓
CSS loaded → Styles applied to DOM
    ↓
JavaScript executed → Event listeners attached
    ↓
JavaScript manipulates DOM → Renders battery pins
    ↓
User sees interactive dashboard
```

### 2. User Interaction Flow

```
User clicks battery pin
    ↓
JavaScript event listener fires
    ↓
JavaScript stores site ID in sessionStorage
    ↓
JavaScript navigates to detail.html?id=5
    ↓
detail.html loads
    ↓
JavaScript reads URL parameter
    ↓
JavaScript finds site data
    ↓
JavaScript updates DOM with site info
    ↓
CSS styles the presentation
    ↓
User sees detailed battery metrics
```

### 3. Cross-Page Communication

```
index.html
    ↓
JavaScript: sessionStorage.setItem('bmsSitesData', JSON.stringify(sites))
    ↓
JavaScript: sessionStorage.setItem('bmsSelectedSiteId', '5')
    ↓
Navigate to detail.html?id=5
    ↓
detail.html
    ↓
JavaScript: const sites = JSON.parse(sessionStorage.getItem('bmsSitesData'))
    ↓
JavaScript: const siteId = new URLSearchParams(window.location.search).get('id')
    ↓
JavaScript: const site = sites.find(s => s.id === parseInt(siteId))
    ↓
Display site details
```

---

## Key Web APIs Used

### DOM Manipulation

```javascript
// Get element by ID
const element = document.getElementById('statusBadge');

// Create new element
const div = document.createElement('div');

// Update content
element.textContent = 'New Text';
element.innerHTML = '<strong>Bold Text</strong>';

// Modify styles
element.style.color = 'red';
element.style.width = '100px';

// Add/remove classes
element.className = 'status-good';
element.classList.add('active');
element.classList.remove('hidden');

// Append to DOM
container.appendChild(element);
```

### Event Handling

```javascript
// Click events
button.addEventListener('click', (e) => {
  e.preventDefault();
  console.log('Button clicked!');
});

// Hover events
element.addEventListener('mouseenter', () => {
  element.style.transform = 'scale(1.2)';
});

// Keyboard events
document.addEventListener('keydown', (e) => {
  if (e.key === 'Enter') {
    submitForm();
  }
});

// Touch events (mobile)
element.addEventListener('touchend', (e) => {
  e.preventDefault();
  handleTouch();
});
```

### Storage API

```javascript
// Save data
sessionStorage.setItem('key', 'value');
sessionStorage.setItem('sites', JSON.stringify(sites));

// Retrieve data
const value = sessionStorage.getItem('key');
const sites = JSON.parse(sessionStorage.getItem('sites'));

// Remove data
sessionStorage.removeItem('key');

// Clear all
sessionStorage.clear();
```

### URL Parameters

```javascript
// Read URL: detail.html?id=5&status=good
const urlParams = new URLSearchParams(window.location.search);
const siteId = urlParams.get('id');        // "5"
const status = urlParams.get('status');     // "good"

// Navigate with parameters
window.location.href = `detail.html?id=${siteId}`;
```

---

## Best Practices Applied

### 1. Separation of Concerns

**DO**: Keep HTML, CSS, and JavaScript responsibilities separate
```html
<!-- HTML: Structure -->
<button id="submitBtn" class="btn-primary">Submit</button>
```

```css
/* CSS: Presentation */
.btn-primary {
  background: #3b82f6;
  padding: 10px 20px;
}
```

```javascript
// JavaScript: Behavior
document.getElementById('submitBtn').addEventListener('click', handleSubmit);
```

**DON'T**: Mix concerns
```html
<!-- Bad: Inline styles and scripts -->
<button style="background:#3b82f6;padding:10px" onclick="alert('clicked')">
```

### 2. Progressive Enhancement

Start with HTML that works, then enhance:
```html
<!-- Works without JavaScript -->
<a href="detail.html?id=5">View Details</a>

<!-- Enhanced with JavaScript -->
<a href="detail.html?id=5" onclick="handleNavigation(event, 5)">View Details</a>
```

### 3. Semantic HTML

Use meaningful elements:
```html
<!-- Good: Semantic -->
<header>
  <nav><a href="/">Home</a></nav>
</header>
<main>
  <article>Content</article>
</main>
<footer>Footer</footer>

<!-- Bad: Non-semantic -->
<div class="header">
  <div class="nav"><div class="link">Home</div></div>
</div>
```

### 4. Event Delegation

Handle multiple elements efficiently:
```javascript
// Good: One listener for all pins
container.addEventListener('click', (e) => {
  if (e.target.classList.contains('battery-pin')) {
    const siteId = e.target.dataset.siteId;
    showDetail(siteId);
  }
});

// Bad: Listener for each pin
pins.forEach(pin => {
  pin.addEventListener('click', () => showDetail(pin.id));
});
```

---

## Learning Resources

### HTML
- [MDN HTML Guide](https://developer.mozilla.org/en-US/docs/Web/HTML)
- Semantic elements, forms, tables, attributes

### CSS
- [MDN CSS Guide](https://developer.mozilla.org/en-US/docs/Web/CSS)
- Selectors, flexbox, grid, animations

### JavaScript
- [MDN JavaScript Guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
- DOM API, events, async, fetch

### Web APIs
- [Web APIs](https://developer.mozilla.org/en-US/docs/Web/API)
- Storage, URL, Canvas, Geolocation

---

## Summary

| Technology | Purpose | Example |
|------------|---------|---------|
| **HTML** | Structure & Content | `<div id="app">` |
| **CSS** | Styling & Layout | `.battery-pin { color: red; }` |
| **JavaScript** | Behavior & Logic | `element.addEventListener('click')` |

**Together they create**:
- HTML: "This is a button"
- CSS: "The button is blue and rounded"
- JavaScript: "When clicked, navigate to details page"

This separation makes code:
- **Maintainable**: Change styling without touching logic
- **Reusable**: Same CSS/JS for multiple HTML pages
- **Accessible**: HTML provides structure for screen readers
- **Performant**: Browser can optimize each layer independently
