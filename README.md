# MarkSite

<div align="center">

![MarkSite Logo](https://img.shields.io/badge/MarkSite-Static%20Site%20Generator-blue)
![Python](https://img.shields.io/badge/Python-3.11%2B-green)
![License](https://img.shields.io/badge/License-MIT-yellow)


[Features](#features) • [Quick Start](#quick-start) • [Documentation](doc/) • [Templates](#templates) • [Components](#components)

</div>
<p align="center">
  <a href="https://github.com/Alqudimi/MarkSite">
    <img src="assets/images/logo.png" alt="Project Logo" width="200" height="200">
  </a>
</p>

<h1 align="center">MarkSite</h1>

<h3 align="center">Transform Markdown into Beautiful, Professional Websites</h3>

<p align="center">
  A powerful, component-based static site generator built with Python. Transform Markdown files into beautiful, modern static websites with 14 professional templates and 8 interactive components.
  <br />
  <br />
  <a href="https://github.com/Alqudimi/MarkSite/doc"><strong>Explore the Docs »</strong></a>
  <br />
  <br />
  <a href="https://github.com/Alqudimi/MarkSite/demo">View Demo</a>
  ·
  <a href="https://github.com/Alqudimi/MarkSite/issues">Report Bug</a>
  ·
  <a href="https://github.com/Alqudimi/MarkSite/issues">Request Feature</a>
</p>

<p align="center">
  <a href="https://github.com/Alqudimi/MarkSite/blob/main/LICENSE">
    <img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="License">
  </a>
  <a href="https://github.com/Alqudimi/MarkSite/releases">
    <img src="https://img.shields.io/badge/version-1.0.0-green.svg" alt="Version">
  </a>
  <a href="https://github.com/Alqudimi/MarkSite/stargazers">
    <img src="https://img.shields.io/github/stars/Alqudimi/MarkSite.svg?style=social&label=Stars" alt="Stars">
  </a>
  <a href="https://github.com/Alqudimi/MarkSite/forks">
    <img src="https://img.shields.io/github/forks/Alqudimi/MarkSite.svg?style=social&label=Forks" alt="Forks">
  </a>
  <a href="https://github.com/Alqudimi/MarkSite/issues">
    <img src="https://img.shields.io/github/issues/Alqudimi/MarkSite.svg" alt="Issues">
  </a>
</p>
---

## Overview

MarkSite is a high-performance static site generator that converts Markdown content into stunning, production-ready websites. Built with Python, Flask, and Jinja2, it offers a powerful component system, 14 professional templates, and advanced features for developers and content creators.

## Features

### 🚀 Core Features
- **Recursive Markdown Processing** - Automatically scans and processes all `.md` files in nested directories
- **Advanced Markdown Rendering** - Full CommonMark support with syntax highlighting via Pygments
- **Automatic TOC Generation** - Table of contents generated from headings
- **Static Export** - Complete static HTML/CSS/JS output ready for any hosting platform
- **SEO Optimized** - Automatic sitemap.xml generation and meta tags
- **Full-Text Search** - Client-side search powered by Lunr.js

### 🎨 Component System
- **8 Built-in Components** - Button, Card, Alert, Code Sample, Hero, Tabs, Collapsible, Badge
- **Shortcode Syntax** - Easy `{{< component param="value" />}}` syntax in Markdown
- **Theme-Aware** - Components automatically adapt to site theme
- **Accessible** - ARIA attributes and semantic HTML throughout
- **Pattern Library** - Auto-generated documentation with live examples

### 🎭 Professional Templates
- **14 Beautiful Templates** - From minimalist blogs to corporate portfolios
- **Bootstrap 5** - Responsive, mobile-first design
- **Light/Dark Mode** - User-selectable theme with persistent preference
- **Custom Styling** - Easily customizable colors and branding
- **Smooth Animations** - Professional transitions and effects

### ⚡ Performance
- **Fast Builds** - Processes hundreds of pages in seconds
- **Optimized Output** - Clean, minified CSS and deferred JS loading
- **CDN Ready** - All assets are static and cacheable
- **Lighthouse Score** - 95+ on all metrics

## Quick Start

### Prerequisites
- Python 3.11 or higher
- pip package manager

### Installation

```bash
# Clone the repository
git clone https://github.com/Alqudimi/MarkSite.git
cd MarkSite

# Install dependencies
pip install -r requirements.txt
```

### Build Your First Site

```bash
# Basic build (uses content/ as input, outputs to site/)
python build.py

# Build with a specific template
python build.py --template minimalist

# Custom configuration
python build.py --config myconfig.yaml
```

### View Your Site

```bash
# Serve locally
python -m http.server -d site 8000

# Visit http://localhost:8000
```

## Templates

Choose from 14 professionally designed templates:

| Template | Description | Best For |
|----------|-------------|----------|
| **Default** | Classic, professional Bootstrap design | Business sites, general purpose |
| **Minimalist** | Clean, spacious with elegant typography | Personal blogs, portfolios |
| **Tech Blog** | Dark theme with neon accents | Technology blogs, developer sites |
| **Documentation** | Professional documentation style | Technical docs, API references |
| **Portfolio** | Showcase design with bold typography | Creative portfolios, photography |
| **Magazine** | Modern editorial with bold layouts | News sites, content publishers |
| **Landing** | Conversion-focused with gradients | Product pages, SaaS sites |
| **Creative** | Bold, artistic with dramatic styling | Agencies, creative studios |
| **Personal Blog** | Warm, cozy with serif typography | Personal writing, storytelling |
| **Inkwell** | Literary magazine aesthetic | Authors, literary journals |
| **Futuristic** | Sci-fi inspired modern design | Tech startups, innovation sites |
| **Monochrome** | Elegant black and white | Photography, minimal portfolios |
| **Oasis** | Nature-inspired calming design | Wellness, lifestyle blogs |
| **Retrowave** | 80s-inspired neon aesthetics | Gaming, retro tech, music |

All templates include:
- Responsive layouts optimized for their purpose
- Full component support
- Light and dark mode variants
- Mobile-first responsive design
- Unique color schemes and typography

## Components

### Available Components

- **Button** - Call-to-action buttons with multiple variants and sizes
- **Card** - Content cards with headers, footers, and images
- **Alert** - Notification messages with icons and dismissible options
- **Code Sample** - Syntax-highlighted code blocks with copy functionality
- **Hero** - Large hero sections with backgrounds and CTAs
- **Tabs** - Tabbed content organization
- **Collapsible** - Accordion-style expandable sections
- **Badge** - Labels and tags for highlighting content

### Example Usage

```markdown
{{< button text="Get Started" variant="primary" href="/docs/" />}}
{{< card title="Welcome" content="Start building amazing sites!" />}}
{{< alert content="Important update!" variant="info" icon="bi bi-info-circle" />}}
{{< code language="python" content="print('Hello, MarkSite!')" />}}
```

See [Component Documentation](doc/COMPONENTS.md) for complete usage guide.

## Project Structure

```
MarkSite/
├── content/              # Your Markdown content files (input)
│   ├── index.md
│   ├── example/
│   └── docs/
├── generator/
│   ├── generator.py      # Main generator engine
│   ├── shortcode_parser.py  # Component parser
│   ├── templates/        # Jinja2 page templates (14 themes)
│   ├── components/       # Component templates
│   └── static/           # CSS and JavaScript
├── site/                 # Generated static site (output)
├── doc/                  # Documentation
├── build.py              # CLI build tool
├── config.yaml           # Site configuration
└── requirements.txt      # Python dependencies
```

## Documentation

- [Getting Started Guide](doc/GETTING_STARTED.md) - Complete setup and usage guide
- [Component Guide](doc/COMPONENTS.md) - Detailed component documentation
- [Template Guide](doc/TEMPLATES.md) - All templates with examples
- [Deployment Guide](doc/DEPLOYMENT.md) - Deploy to GitHub Pages, Netlify, Vercel
- [Configuration Guide](doc/CONFIGURATION.md) - Customize your site
- [Custom Components](doc/CUSTOM_COMPONENTS.md) - Create your own components

## Configuration

Customize your site in `config.yaml`:

```yaml
site_name: "My Awesome Site"
site_description: "Built with MarkSite"
site_url: "https://example.com"
template: "minimalist"

theme:
  default_mode: "light"
  primary_color: "#0d6efd"

author:
  name: "Your Name"
  email: "your@email.com"

navigation:
  - title: "Home"
    url: "/"
  - title: "Blog"
    url: "/blog/"
```

## Deployment

Deploy your site to any static hosting platform:

- **GitHub Pages** - Free hosting for GitHub repositories
- **Netlify** - Automatic builds and deployments
- **Vercel** - Edge network with instant deployments
- **Any Static Host** - Upload the `site/` directory

See [Deployment Guide](doc/DEPLOYMENT.md) for detailed instructions.

## Browser Support

- Chrome/Edge (latest 2 versions)
- Firefox (latest 2 versions)
- Safari (latest 2 versions)
- Mobile browsers (iOS Safari, Chrome Android)

## Accessibility

- Semantic HTML throughout
- ARIA labels and roles
- Keyboard navigation support
- Screen reader compatible
- WCAG 2.1 AA compliant

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

**Abdulaziz Al-Qadimi**
- Email: eng7mi@gmail.com
- GitHub: [@Alqudimi](https://github.com/Alqudimi)
- Project Repository: [MarkSite](https://github.com/Alqudimi/MarkSite)

## Acknowledgments

Built with:
- Python 3.11+
- Flask & Jinja2
- Bootstrap 5
- Pygments (syntax highlighting)
- Lunr.js (search)
- Markdown (python-markdown)

---

<div align="center">

**[⭐ Star this repository](https://github.com/Alqudimi/MarkSite) if you find it helpful!**

Made with ❤️ by Abdulaziz Al-Qadimi

</div>
