# Deployment Guide for Thailand Battery Monitoring Dashboard

## GitHub Pages Deployment

This single-page application is optimized for deployment to GitHub Pages and follows all modern static site requirements.

### Prerequisites
- GitHub account
- Repository for the project
- Git installed locally

### Step-by-Step Deployment

#### 1. Prepare Your Repository
```bash
# Clone your repository (if starting fresh)
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

# Add your files
cp -r /path/to/dashboard/* .

# Initialize git if needed
git init
git add .
git commit -m "Initial commit with battery monitoring dashboard"
```

#### 2. Configure GitHub Pages
1. Push your code to GitHub:
   ```bash
   git remote add origin https://github.com/your-username/your-repo-name.git
   git branch -M main
   git push -u origin main
   ```

2. Navigate to your repository on GitHub
3. Go to **Settings** tab
4. Scroll down to **Pages** section
5. Under **Source**, select:
   - Branch: `main`
   - Folder: `/ (root)`
6. Click **Save**

#### 3. Access Your Deployed Site
Your site will be available at: `https://your-username.github.io/your-repo-name/`

### GitHub Actions Deployment (Alternative)

For automated deployments with GitHub Actions, create `.github/workflows/deploy.yml`:

```yaml
name: Deploy to GitHub Pages

on:
  push:
    branches: [ main ]

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v3

      - name: Setup Node.js
        uses: actions/setup-node@v3
        with:
          node-version: '18'

      - name: Install dependencies
        run: npm install

      - name: Deploy to GitHub Pages
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./
```

## Static Site Generation Compatibility

The application is compatible with all major static site generators and frameworks:

### Hugo
```bash
# Hugo can serve the static files directly
hugo server --source=dashboard/
```

### Gatsby
The static HTML/CSS/JS components can be integrated into a Gatsby project.

### Next.js (Static Export)
The application can be embedded in a Next.js project and exported as static files.

### Vite (Static Build)
Can be served using Vite's static server capabilities.

### Eleventy
The HTML structure is compatible with Eleventy's template system.

## Local Development Server

### Using Node.js
```bash
# Install development dependencies
npm install

# Start local server
npm start
# or with live reload
npm run dev
```

### Using Python
```bash
# Python 3
python -m http.server 8000

# Python 2
python -m SimpleHTTPServer 8000
```

### Using PHP
```bash
php -S localhost:8000
```

## URL Structure & Routing

The application uses client-side routing compatible with GitHub Pages:

- **Home Page**: `https://your-username.github.io/your-repo-name/`
- **Detail View**: `https://your-username.github.io/your-repo-name/?page=detail&id=5`
- **Database View**: `https://your-username.github.io/your-repo-name/?page=database`

## Optimization for GitHub Pages

### File Structure
```
├── index.html (main SPA application)
├── detail.html (legacy - now virtual page)
├── db_view.html (legacy - now virtual page)
├── file/
│   ├── thailand-map.png
│   └── thai.jpg
├── sql/
│   ├── bms.sql
│   └── db_viewer.html
├── README.md
├── QWEN.md
├── DEPLOYMENT.md
├── package.json
└── .gitignore
```

### Performance Considerations
- All JavaScript and CSS is inlined in `index.html` for minimal HTTP requests
- SVG-based graphics for crisp rendering at any resolution
- Optimized animations with CSS rather than JavaScript where possible
- Lightweight implementation without heavy frameworks

### Caching
GitHub Pages automatically handles static asset caching. The application uses relative paths for all resources to ensure proper functionality under subdirectories.

## Troubleshooting

### Common Issues

1. **Links not working after deployment**
   - Ensure all paths are relative (e.g., `./detail.html`, `../file/image.png`)
   - Verify client-side routing is working properly

2. **Images or assets not loading**
   - Check that file paths are correct relative to the HTML file
   - Ensure files are in the correct subdirectories

3. **URL parameters not working**
   - GitHub Pages uses Jekyll by default; ensure `_config.yml` doesn't interfere
   - Add this to your root to disable Jekyll if needed: `echo "" > .nojekyll`

### Verifying Deployment

1. Check the GitHub Pages status in your repository settings
2. Verify all files are present in the deployed version
3. Test navigation between different virtual pages
4. Verify URL parameters work correctly

## Environment-Specific Configuration

The application doesn't require environment-specific configuration as it uses static assets only. All data is embedded in the JavaScript code.

## CDN Integration

For production use, consider adding CDN headers if needed, though GitHub Pages provides global CDN distribution by default.

## Security Headers

GitHub Pages automatically applies security headers. The application uses secure practices:
- No external dependencies for core functionality
- All data is statically defined
- Client-side only processing

---
Deployed with GitHub Pages: https://pages.github.com/