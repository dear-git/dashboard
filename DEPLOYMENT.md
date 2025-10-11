# Deployment Guide - Battery Monitoring System

## GitHub Pages Deployment

This project is configured for GitHub Pages deployment with zero build steps required.

### Current Deployment

- **Repository**: https://github.com/dear-git/dashboard
- **GitHub Pages URL**: https://dear-git.github.io/dashboard/
- **Branch**: main
- **Directory**: / (root)

### Files Structure

```
dashboard/
├── index.html              # Main dashboard (entry point)
├── detail.html             # Battery detail page
├── db_view.html            # Database viewer page
├── file/
│   ├── thailand-map.png    # Thailand map image
│   └── thai.jpg            # Alternative map
├── sql/
│   ├── bms.sql            # Database schema
│   └── db_viewer.html     # SQL viewer
├── CLAUDE.md              # Claude Code documentation
├── AGENTS.md              # Development guidelines
├── README.md              # Project overview
└── DEPLOYMENT.md          # This file
```

### Navigation Flow

1. **index.html** → Main dashboard with Thailand map
   - Click battery pin → Opens detail.html in new tab
   - Click "DB Viewer" → Opens internal database page
   - Click "Export Data" → Downloads CSV

2. **detail.html** → Individual battery site details
   - Accepts URL parameter: `?id=1` through `?id=24`
   - Supports sessionStorage data injection
   - Back button returns to index.html

3. **Database Pages**
   - Internal viewer via "DB Viewer" button
   - Standalone db_view.html
   - SQL schema viewer in sql/db_viewer.html

### GitHub Pages Configuration

#### Enable GitHub Pages

1. Go to repository settings: https://github.com/dear-git/dashboard/settings/pages
2. Under "Source":
   - Select: **Deploy from a branch**
   - Branch: **main**
   - Folder: **/ (root)**
3. Click **Save**
4. Wait 1-2 minutes for deployment

#### Access Your Site

- Main dashboard: https://dear-git.github.io/dashboard/
- Direct site detail: https://dear-git.github.io/dashboard/detail.html?id=1
- Database viewer: https://dear-git.github.io/dashboard/db_view.html

### Features for GitHub Pages

✅ **Static Files Only**: No build process required
✅ **Relative Paths**: All links use relative paths
✅ **Self-Contained**: CSS embedded in HTML
✅ **No External APIs**: Pure CSS map (no Google Maps key needed)
✅ **Mobile Friendly**: Responsive design works on all devices
✅ **sessionStorage**: Data persists between page navigations

### Testing Locally

Before pushing to GitHub Pages, test locally:

```bash
# Start local server
python3 -m http.server 8000

# Visit in browser
open http://localhost:8000
```

Test these flows:
1. Click battery pins → Detail page opens
2. Navigate back from detail page
3. Click "DB Viewer" → Database table shows
4. Export CSV functionality
5. Test on mobile viewport

### Deployment Workflow

```bash
# 1. Make changes locally
# 2. Test with local server
python3 -m http.server 8000

# 3. Commit changes
git add .
git commit -m "Your commit message"

# 4. Push to GitHub
git push origin main

# 5. GitHub Pages auto-deploys (1-2 minutes)
```

### URL Structure

#### Main Dashboard
```
https://dear-git.github.io/dashboard/
```

#### Battery Detail Pages
```
https://dear-git.github.io/dashboard/detail.html?id=1   # เชียงราย 2
https://dear-git.github.io/dashboard/detail.html?id=2   # ลำปาง 3
https://dear-git.github.io/dashboard/detail.html?id=3   # พิษณุโลก 6
...
https://dear-git.github.io/dashboard/detail.html?id=24  # ปัตตานี 2
```

#### Database Viewer
```
https://dear-git.github.io/dashboard/db_view.html
```

### Troubleshooting

#### Site Not Loading
- Wait 1-2 minutes after first deployment
- Check GitHub Pages settings are enabled
- Verify branch is set to "main"
- Clear browser cache (Cmd+Shift+R)

#### Battery Pins Not Clickable
- Issue was fixed in commit c079190
- JavaScript bug with `selectedSite` variable resolved
- All click handlers now properly navigate to detail.html

#### Images Not Loading
- All images use relative paths: `./file/thailand-map.png`
- Ensure `file/` directory is committed to git
- Check file names match exactly (case-sensitive)

#### Navigation Issues
- All links use relative paths (no leading `/`)
- sessionStorage preserves data between pages
- Back buttons use `window.location.href = 'index.html'`

### Custom Domain (Optional)

To use a custom domain:

1. Add `CNAME` file to repository root:
   ```
   your-domain.com
   ```

2. Configure DNS with your domain provider:
   ```
   Type: CNAME
   Host: www
   Value: dear-git.github.io
   ```

3. Enable HTTPS in GitHub Pages settings

### Performance

- **Load Time**: ~1-2 seconds (all assets embedded)
- **File Sizes**:
  - index.html: ~137 KB
  - detail.html: ~47 KB
  - thailand-map.png: ~153 KB
- **Total**: ~340 KB (no external dependencies)

### Browser Compatibility

✅ Chrome 90+
✅ Firefox 88+
✅ Safari 14+
✅ Edge 90+
✅ Mobile browsers (iOS Safari, Chrome Mobile)

### Monitoring

Check deployment status:
- https://github.com/dear-git/dashboard/deployments
- Click latest deployment to see status
- View build logs if errors occur

### Updating Content

#### Add New Battery Site

1. Edit `index.html` - add to `sites` array (line ~1251)
2. Site automatically appears in:
   - Main dashboard map
   - Database viewer
   - Detail page (via URL parameter)
3. Commit and push

#### Update Battery Specifications

1. Edit `BATTERY_SPEC` in `index.html` (line ~1710)
2. All calculations auto-update
3. Commit and push

#### Modify Styling

1. Edit embedded CSS in `<style>` tags
2. Test locally first
3. Commit and push

### Security Notes

- No API keys required (pure CSS map)
- No backend/database (static files only)
- Safe to expose publicly
- CSV exports contain site data (intentional)
- No authentication required

### Support

- Issues: https://github.com/dear-git/dashboard/issues
- Documentation: See CLAUDE.md and README.md
- Development: See AGENTS.md

---

**Last Updated**: October 2024
**Deployment Status**: ✅ Active on GitHub Pages
