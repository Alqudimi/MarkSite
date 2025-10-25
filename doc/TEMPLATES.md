# Template Guide

MarkSite includes 14 professionally designed templates, each optimized for different types of websites. This guide showcases all templates with examples and use cases.

## Table of Contents

- [Overview](#overview)
- [Choosing a Template](#choosing-a-template)
- [Template Gallery](#template-gallery)
- [Using Templates](#using-templates)
- [Template Customization](#template-customization)

## Overview

All MarkSite templates feature:
- **Responsive Design** - Mobile-first, works on all devices
- **Light/Dark Mode** - User-selectable theme with persistence
- **Full Component Support** - All 8 components work in every template
- **SEO Optimized** - Meta tags and semantic HTML
- **Accessibility** - WCAG 2.1 AA compliant
- **Bootstrap 5** - Modern, professional styling

## Choosing a Template

| Template | Best For | Design Style | Primary Colors |
|----------|----------|--------------|----------------|
| [Default](#1-default) | Business, General | Classic Bootstrap | Blue, Gray |
| [Minimalist](#2-minimalist) | Personal Blog, Portfolio | Clean, Spacious | Subtle Pastels |
| [Tech Blog](#3-tech-blog) | Developer Blog, Tech Site | Dark, Modern | Neon Green/Blue |
| [Documentation](#4-documentation) | Technical Docs, API | Professional, Structured | Blue, White |
| [Portfolio](#5-portfolio) | Creative Work, Photography | Bold, Showcase | Black, Gold |
| [Magazine](#6-magazine) | News, Content Publishers | Editorial, Bold | Red, Black |
| [Landing](#7-landing) | Products, SaaS | Conversion-focused | Gradients |
| [Creative](#8-creative) | Agencies, Studios | Artistic, Dramatic | Purple, Gold |
| [Personal Blog](#9-personal-blog) | Writing, Storytelling | Warm, Cozy | Earth Tones |
| [Inkwell](#10-inkwell) | Authors, Literary | Literary, Elegant | Sepia, Cream |
| [Futuristic](#11-futuristic) | Tech Startups, Innovation | Sci-fi, Modern | Cyan, Purple |
| [Monochrome](#12-monochrome) | Photography, Minimal | Black & White | Grayscale |
| [Oasis](#13-oasis) | Wellness, Lifestyle | Nature-inspired | Green, Earth |
| [Retrowave](#14-retrowave) | Gaming, Music, Retro | 80s Aesthetic | Pink, Cyan |

## Template Gallery

### 1. Default

**Description**: Classic, professional design with Bootstrap's signature styling.

**Best For**: 
- Business websites
- General purpose sites
- Corporate blogs
- Professional portfolios

**Design Features**:
- Clean Bootstrap UI
- Professional typography (Sans-serif)
- Blue primary color scheme
- Standard navigation
- Grid-based layouts

**Usage**:
```bash
python build.py --template default
```

**Config**:
```yaml
template: "default"
theme:
  primary_color: "#0d6efd"
  secondary_color: "#6c757d"
```

---

### 2. Minimalist

**Description**: Clean, spacious layout with subtle colors and elegant typography.

**Best For**:
- Personal blogs
- Creative portfolios
- Photography sites
- Minimalist brands

**Design Features**:
- Generous white space
- Subtle pastel colors
- Large, readable typography
- Simplified navigation
- Focus on content

**Usage**:
```bash
python build.py --template minimalist
```

**Config**:
```yaml
template: "minimalist"
theme:
  primary_color: "#6c63ff"
  secondary_color: "#b8b8b8"
```

---

### 3. Tech Blog

**Description**: Dark theme with neon accents, grid backgrounds, and tech-focused aesthetics.

**Best For**:
- Developer blogs
- Technology sites
- Coding tutorials
- Tech startups

**Design Features**:
- Dark background (#1a1a2e)
- Neon green/blue accents
- Grid pattern backgrounds
- Code-friendly styling
- Monospace fonts for code

**Usage**:
```bash
python build.py --template techblog
```

**Config**:
```yaml
template: "techblog"
theme:
  default_mode: "dark"
  primary_color: "#00ff88"
```

---

### 4. Documentation

**Description**: Professional documentation style optimized for technical content.

**Best For**:
- API documentation
- Technical guides
- Product manuals
- Software docs

**Design Features**:
- Structured layouts
- Enhanced code blocks
- Table of contents
- Search-friendly
- Professional typography

**Usage**:
```bash
python build.py --template documentation
```

**Config**:
```yaml
template: "documentation"
theme:
  primary_color: "#0066cc"
```

---

### 5. Portfolio

**Description**: Showcase-focused design with bold typography and golden accents.

**Best For**:
- Creative portfolios
- Photography showcases
- Design work
- Freelancer sites

**Design Features**:
- Bold, large typography
- Gold accent color (#ffd700)
- Dark backgrounds
- Image-focused layouts
- Dramatic spacing

**Usage**:
```bash
python build.py --template portfolio
```

**Config**:
```yaml
template: "portfolio"
theme:
  primary_color: "#ffd700"
  secondary_color: "#2d2d2d"
```

---

### 6. Magazine

**Description**: Modern editorial design with bold typography and news-style layouts.

**Best For**:
- News sites
- Content publishers
- Online magazines
- Editorial blogs

**Design Features**:
- Bold headlines
- Multi-column layouts
- Red accent colors
- Editorial typography
- Card-based content grid

**Usage**:
```bash
python build.py --template magazine
```

**Config**:
```yaml
template: "magazine"
theme:
  primary_color: "#e74c3c"
```

---

### 7. Landing

**Description**: Conversion-focused landing page with gradient accents and modern UI.

**Best For**:
- Product pages
- SaaS landing pages
- Marketing sites
- Service offerings

**Design Features**:
- Gradient backgrounds
- Strong CTAs
- Conversion-focused layout
- Modern UI elements
- Feature highlights

**Usage**:
```bash
python build.py --template landing
```

**Config**:
```yaml
template: "landing"
theme:
  primary_color: "#667eea"
```

---

### 8. Creative

**Description**: Bold, artistic design with dramatic styling and gold accents.

**Best For**:
- Creative agencies
- Design studios
- Artistic portfolios
- Branding sites

**Design Features**:
- Dramatic contrasts
- Gold accents (#d4af37)
- Large, bold typography
- Artistic layouts
- Premium feel

**Usage**:
```bash
python build.py --template creative
```

**Config**:
```yaml
template: "creative"
theme:
  primary_color: "#d4af37"
```

---

### 9. Personal Blog

**Description**: Warm, cozy blogging theme with serif typography and earthy tones.

**Best For**:
- Personal blogs
- Writing sites
- Storytelling
- Lifestyle blogs

**Design Features**:
- Serif typography (Georgia, Garamond)
- Warm earth tones
- Cozy, inviting layout
- Reading-focused design
- Comfortable line spacing

**Usage**:
```bash
python build.py --template personalblog
```

**Config**:
```yaml
template: "personalblog"
theme:
  primary_color: "#c17d5c"
```

---

### 10. Inkwell

**Description**: Literary magazine aesthetic with elegant serif fonts and classic design.

**Best For**:
- Authors
- Literary journals
- Book blogs
- Writing portfolios

**Design Features**:
- Classic serif fonts
- Sepia and cream tones
- Book-like layout
- Elegant spacing
- Literary typography

**Usage**:
```bash
python build.py --template inkwell
```

**Config**:
```yaml
template: "inkwell"
theme:
  primary_color: "#8b7355"
```

---

### 11. Futuristic

**Description**: Sci-fi inspired modern design with cyan and purple colors.

**Best For**:
- Tech startups
- Innovation sites
- Future-focused brands
- Sci-fi content

**Design Features**:
- Futuristic UI elements
- Cyan/purple gradients
- Modern geometric shapes
- Sleek animations
- Tech-forward feel

**Usage**:
```bash
python build.py --template futuristic
```

**Config**:
```yaml
template: "futuristic"
theme:
  primary_color: "#00d4ff"
```

---

### 12. Monochrome

**Description**: Elegant black and white design, perfect for photography and minimal aesthetics.

**Best For**:
- Photography portfolios
- Minimal blogs
- Art galleries
- Design portfolios

**Design Features**:
- Pure grayscale palette
- High contrast
- Focus on imagery
- Minimal distractions
- Timeless design

**Usage**:
```bash
python build.py --template monochrome
```

**Config**:
```yaml
template: "monochrome"
theme:
  primary_color: "#000000"
  secondary_color: "#ffffff"
```

---

### 13. Oasis

**Description**: Nature-inspired calming design with green and earth tones.

**Best For**:
- Wellness sites
- Lifestyle blogs
- Nature content
- Health & fitness

**Design Features**:
- Green nature colors
- Calming earth tones
- Organic shapes
- Natural imagery
- Peaceful aesthetics

**Usage**:
```bash
python build.py --template oasis
```

**Config**:
```yaml
template: "oasis"
theme:
  primary_color: "#2d6a4f"
```

---

### 14. Retrowave

**Description**: 80s-inspired neon aesthetics with pink and cyan colors.

**Best For**:
- Gaming sites
- Retro tech blogs
- Music sites
- Entertainment

**Design Features**:
- Neon pink/cyan colors
- 80s aesthetic
- Grid backgrounds
- Synthwave vibes
- Nostalgic feel

**Usage**:
```bash
python build.py --template retrowave
```

**Config**:
```yaml
template: "retrowave"
theme:
  primary_color: "#ff00ff"
  secondary_color: "#00ffff"
```

---

## Using Templates

### Set Template in CLI

```bash
# Use a specific template
python build.py --template minimalist

# Combine with other options
python build.py --template techblog --output blog
```

### Set Template in Config

Edit `config.yaml`:
```yaml
template: "minimalist"
```

Then build:
```bash
python build.py
```

### Testing Multiple Templates

Create a script to preview all templates:

```bash
#!/bin/bash
for template in default minimalist techblog documentation portfolio magazine landing creative personalblog inkwell futuristic monochrome oasis retrowave; do
  python build.py --template $template --output "preview-$template"
  echo "✓ Built $template"
done
```

## Template Customization

### Override Colors

Even with a template selected, you can override colors in `config.yaml`:

```yaml
template: "minimalist"
theme:
  primary_color: "#ff6b6b"    # Custom primary
  secondary_color: "#4ecdc4"  # Custom secondary
```

### Custom Fonts

Templates use default fonts, but you can add custom fonts via CSS:

1. Create `generator/static/css/custom.css`
2. Add font imports and overrides:

```css
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap');

body {
  font-family: 'Inter', sans-serif !important;
}
```

### Template Inheritance

Templates inherit from base templates. You can create custom templates by:

1. Copy an existing template folder
2. Modify the HTML/CSS
3. Reference in config

See [Custom Components Guide](CUSTOM_COMPONENTS.md) for details.

## Template Comparison

### Performance

All templates are optimized for performance:
- Minimal CSS (~50-100KB)
- Deferred JavaScript loading
- Optimized images
- Static file serving

### Accessibility

All templates meet WCAG 2.1 AA standards:
- Semantic HTML
- ARIA labels
- Keyboard navigation
- Screen reader support
- Sufficient color contrast

### Mobile Responsiveness

All templates use Bootstrap 5's responsive grid:
- Mobile-first design
- Breakpoints: 576px, 768px, 992px, 1200px
- Touch-friendly navigation
- Responsive typography

## Best Practices

### Choosing the Right Template

1. **Consider Your Audience**
   - Business: Default, Documentation
   - Developers: Tech Blog, Documentation
   - Creatives: Portfolio, Creative, Minimalist
   - Writers: Personal Blog, Inkwell

2. **Match Content Type**
   - Technical docs → Documentation
   - Blog posts → Personal Blog, Minimalist
   - Products → Landing, Magazine
   - Portfolio → Portfolio, Creative, Monochrome

3. **Brand Alignment**
   - Choose template that matches brand personality
   - Customize colors to match brand identity
   - Consider target demographic

### Switching Templates

You can switch templates at any time:

```bash
# Build with new template
python build.py --template portfolio

# Content remains the same
# Layout and styling change
```

Your content stays the same, only the design changes.

## Template Examples

### Complete Setup Examples

**Tech Blog Example**
```yaml
# config.yaml
site_name: "Dev Insights"
template: "techblog"
theme:
  default_mode: "dark"
  primary_color: "#00ff88"
author:
  name: "Jane Developer"
navigation:
  - title: "Home"
    url: "/"
  - title: "Tutorials"
    url: "/tutorials/"
  - title: "About"
    url: "/about/"
```

**Portfolio Example**
```yaml
# config.yaml
site_name: "John Doe Design"
template: "portfolio"
theme:
  primary_color: "#ffd700"
author:
  name: "John Doe"
navigation:
  - title: "Work"
    url: "/"
  - title: "About"
    url: "/about/"
  - title: "Contact"
    url: "/contact/"
```

---

**Author**: Abdulaziz Al-Qadimi  
**Repository**: [MarkSite](https://github.com/Alqudimi/MarkSite)
