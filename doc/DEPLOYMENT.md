# Deployment Guide

Learn how to deploy your MarkSite static site to various hosting platforms. Your site is completely static, making deployment simple and fast.

## Table of Contents

- [Pre-Deployment Checklist](#pre-deployment-checklist)
- [GitHub Pages](#github-pages)
- [Netlify](#netlify)
- [Vercel](#vercel)
- [Other Static Hosts](#other-static-hosts)
- [Custom Domain Setup](#custom-domain-setup)
- [Continuous Deployment](#continuous-deployment)

## Pre-Deployment Checklist

Before deploying, ensure:

- [ ] Build completed successfully: `python build.py`
- [ ] All links work correctly (relative paths)
- [ ] Images load properly
- [ ] Configuration updated (`config.yaml`)
- [ ] Site tested locally
- [ ] `site_url` in config matches your domain
- [ ] Navigation menu is complete

### Update Configuration

Edit `config.yaml`:
```yaml
site_name: "Your Site Name"
site_description: "Your site description"
site_url: "https://yourdomain.com"  # Update to your actual domain

author:
  name: "Your Name"
  email: "your@email.com"
```

### Final Build

```bash
python build.py --template [your-template]
```

Your static site is in the `site/` directory, ready to deploy.

---

## GitHub Pages

Deploy for free with GitHub Pages. Two methods available.

### Method 1: Direct Deployment

**Step 1**: Create GitHub repository
```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/yourusername/yourrepo.git
git push -u origin main
```

**Step 2**: Deploy site folder
```bash
git subtree push --prefix site origin gh-pages
```

**Step 3**: Enable GitHub Pages
1. Go to repository Settings
2. Navigate to Pages
3. Source: Deploy from branch
4. Branch: `gh-pages`, folder: `/ (root)`
5. Save

Your site will be live at: `https://yourusername.github.io/yourrepo/`

### Method 2: GitHub Actions (Recommended)

**Step 1**: Create workflow file

Create `.github/workflows/deploy.yml`:
```yaml
name: Deploy MarkSite

on:
  push:
    branches: [ main ]
  workflow_dispatch:

permissions:
  contents: read
  pages: write
  id-token: write

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      
      - name: Install dependencies
        run: pip install -r requirements.txt
      
      - name: Build site
        run: python build.py
      
      - name: Upload artifact
        uses: actions/upload-pages-artifact@v2
        with:
          path: ./site

  deploy:
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    needs: build
    steps:
      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v2
```

**Step 2**: Push to GitHub
```bash
git add .
git commit -m "Add GitHub Actions workflow"
git push
```

**Step 3**: Enable GitHub Pages
1. Repository Settings → Pages
2. Source: GitHub Actions
3. Save

Site deploys automatically on every push!

### Custom Domain on GitHub Pages

1. Add `CNAME` file in `site/` directory:
```
yourdomain.com
```

2. Update DNS records at your domain provider:
```
Type: CNAME
Name: www (or @)
Value: yourusername.github.io
```

3. Enable custom domain in GitHub Pages settings

---

## Netlify

Free hosting with automatic deployments, SSL, and CDN.

### Deploy via Git

**Step 1**: Push to GitHub/GitLab/Bitbucket
```bash
git init
git add .
git commit -m "Initial commit"
git push origin main
```

**Step 2**: Connect to Netlify
1. Log in to [Netlify](https://netlify.com)
2. Click "Add new site" → "Import an existing project"
3. Connect to your Git provider
4. Select your repository

**Step 3**: Configure build settings
```
Build command: python build.py
Publish directory: site
```

**Step 4**: Deploy
- Click "Deploy site"
- Site builds and deploys automatically
- Get URL: `https://random-name.netlify.app`

### Deploy via Drag & Drop

**Step 1**: Build locally
```bash
python build.py
```

**Step 2**: Deploy
1. Go to [Netlify Drop](https://app.netlify.com/drop)
2. Drag the `site/` folder to the page
3. Site deploys instantly

### Netlify Configuration

Create `netlify.toml` in project root:
```toml
[build]
  command = "python build.py"
  publish = "site"

[build.environment]
  PYTHON_VERSION = "3.11"

[[redirects]]
  from = "/*"
  to = "/404.html"
  status = 404
```

### Custom Domain on Netlify

1. In Netlify dashboard: Domain settings → Add custom domain
2. Follow DNS configuration instructions
3. Netlify provides free SSL automatically

---

## Vercel

Fast edge network with instant deployments.

### Deploy via Git

**Step 1**: Push to GitHub
```bash
git init
git add .
git commit -m "Initial commit"
git push origin main
```

**Step 2**: Import to Vercel
1. Log in to [Vercel](https://vercel.com)
2. Click "Add New" → "Project"
3. Import your Git repository

**Step 3**: Configure
```
Framework Preset: Other
Build Command: python build.py
Output Directory: site
```

**Step 4**: Deploy
- Click "Deploy"
- Site builds and deploys to edge network
- Get URL: `https://yoursite.vercel.app`

### Vercel Configuration

Create `vercel.json`:
```json
{
  "buildCommand": "python build.py",
  "outputDirectory": "site",
  "installCommand": "pip install -r requirements.txt"
}
```

### Custom Domain on Vercel

1. Project Settings → Domains
2. Add your domain
3. Configure DNS as instructed
4. Free SSL included

---

## Other Static Hosts

### Cloudflare Pages

1. Connect Git repository
2. Build command: `python build.py`
3. Output directory: `site`
4. Deploy

### Render

1. Connect repository
2. Type: Static Site
3. Build command: `python build.py`
4. Publish directory: `site`
5. Deploy

### AWS S3 + CloudFront

**Step 1**: Build site
```bash
python build.py
```

**Step 2**: Create S3 bucket
```bash
aws s3 mb s3://yoursite.com
```

**Step 3**: Upload files
```bash
aws s3 sync site/ s3://yoursite.com --delete
```

**Step 4**: Enable static hosting
```bash
aws s3 website s3://yoursite.com --index-document index.html
```

**Step 5**: Set up CloudFront (optional)
- Create CloudFront distribution
- Point to S3 bucket
- Configure SSL

### Traditional Web Hosting

For shared hosting (cPanel, etc.):

**Step 1**: Build site
```bash
python build.py
```

**Step 2**: Upload via FTP/SFTP
- Connect to your hosting
- Upload contents of `site/` folder to `public_html/` or `www/`

**Step 3**: Access
- Visit your domain
- Site is live

---

## Custom Domain Setup

### DNS Configuration

For most hosts, set these DNS records:

**For root domain (example.com)**:
```
Type: A
Name: @
Value: [host IP address]
```

**For www subdomain**:
```
Type: CNAME
Name: www
Value: [host provided value]
```

### SSL Certificate

Most modern hosts provide free SSL:
- **GitHub Pages**: Free via Let's Encrypt
- **Netlify**: Automatic SSL
- **Vercel**: Automatic SSL
- **Cloudflare Pages**: Automatic SSL

For traditional hosts, use [Let's Encrypt](https://letsencrypt.org/) or purchase SSL certificate.

---

## Continuous Deployment

### Automatic Rebuilds

With Git-based deployments, your site rebuilds automatically when you push changes:

```bash
# Make changes to content
nano content/blog/new-post.md

# Commit and push
git add .
git commit -m "Add new blog post"
git push

# Site rebuilds automatically on:
# - GitHub Pages (with Actions)
# - Netlify
# - Vercel
# - Cloudflare Pages
```

### Webhook Deployments

Trigger deployments programmatically:

**Netlify Build Hook**:
1. Site Settings → Build & deploy → Build hooks
2. Create hook → Copy URL
3. Trigger via POST request:
```bash
curl -X POST -d {} https://api.netlify.com/build_hooks/[id]
```

**Vercel Deploy Hook**:
1. Project Settings → Git → Deploy Hooks
2. Create hook → Copy URL
3. Trigger deployment:
```bash
curl -X POST https://api.vercel.com/v1/integrations/deploy/[id]
```

---

## Environment-Specific Builds

### Production Configuration

Create `config.prod.yaml`:
```yaml
site_url: "https://yoursite.com"
theme:
  default_mode: "light"
# Production-specific settings
```

Build for production:
```bash
python build.py --config config.prod.yaml
```

### Staging/Preview

Most platforms provide preview deployments:
- **Netlify**: Deploy previews for pull requests
- **Vercel**: Preview URLs for every push
- **GitHub Pages**: Can use separate branch

---

## Performance Optimization

### Before Deployment

**1. Optimize Images**
- Compress images (use TinyPNG, ImageOptim)
- Use appropriate formats (WebP, JPEG, PNG)
- Include responsive images

**2. Minify Assets**
- CSS/JS minification (built into MarkSite)
- Remove unused code

**3. Enable Caching**
```html
<!-- Automatically included in MarkSite templates -->
<meta http-equiv="cache-control" content="public, max-age=31536000">
```

### After Deployment

**1. Configure CDN**
- Most platforms include CDN (Netlify, Vercel, Cloudflare)
- Speeds up global delivery

**2. Enable Compression**
- Gzip/Brotli (automatic on most platforms)

**3. Monitor Performance**
- Use Lighthouse audits
- Check Core Web Vitals
- Monitor in Google Search Console

---

## Troubleshooting

### 404 Errors

**Problem**: Pages not found after deployment

**Solution**:
- Check build output includes all pages
- Verify relative links (use `/page/` not `page/`)
- Ensure `site/` directory is deployed, not root

### Broken Links

**Problem**: Links don't work on deployed site

**Solution**:
- Use relative URLs: `/about/` not `about/`
- Update `site_url` in config.yaml
- Check navigation links in config

### CSS/JS Not Loading

**Problem**: Styling missing on deployed site

**Solution**:
- Verify static files copied to `site/static/`
- Check browser console for errors
- Ensure correct relative paths

### Build Failures

**Problem**: Deployment build fails

**Solution**:
- Check Python version (3.11+ required)
- Verify `requirements.txt` is included
- Check build logs for errors
- Test build locally first

---

## Deployment Comparison

| Platform | Cost | Build Time | SSL | CDN | Best For |
|----------|------|------------|-----|-----|----------|
| **GitHub Pages** | Free | Fast | Yes | Yes | Open source, portfolios |
| **Netlify** | Free tier | Very Fast | Yes | Yes | All purposes |
| **Vercel** | Free tier | Very Fast | Yes | Yes | All purposes |
| **Cloudflare Pages** | Free | Fast | Yes | Yes | Global sites |
| **AWS S3** | Pay-as-go | N/A | Optional | Optional | Enterprise |
| **Traditional Hosting** | Varies | N/A | Varies | No | Legacy sites |

---

## Post-Deployment

### Monitor Your Site

- Set up Google Analytics
- Configure Google Search Console
- Monitor uptime (UptimeRobot, Pingdom)
- Check performance regularly

### SEO Setup

1. **Submit Sitemap**
   - Your sitemap is at `/sitemap.xml`
   - Submit to Google Search Console

2. **Verify robots.txt**
   - Ensure search engines can crawl your site

3. **Social Media Cards**
   - MarkSite includes Open Graph tags
   - Test with social media debuggers

### Maintenance

- Regularly update content
- Monitor and fix broken links
- Update dependencies periodically
- Keep backups of `content/` folder

---

**Author**: Abdulaziz Al-Qadimi  
**Email**: eng7mi@gmail.com  
**Repository**: [MarkSite](https://github.com/Alqudimi/MarkSite)
