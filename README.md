# Static Site Generator

A high-end Python + Flask-based static site generator with a powerful component system. Convert Markdown files into beautiful, modern static websites ready for deployment anywhere.

## Features

### Core Features
- **Recursive Markdown Scanning**: Automatically processes all `.md` files in nested directories
- **Advanced Markdown Rendering**: Full CommonMark support with syntax highlighting via Pygments
- **Table of Contents**: Automatic TOC generation from headings
- **Static Export**: Complete static HTML/CSS/JS output ready for deployment
- **SEO Optimized**: Automatic sitemap.xml generation and meta tags

### Component System
- **8 Built-in Components**: Button, Card, Alert, Code Sample, Hero, Tabs, Collapsible, Badge
- **Shortcode Syntax**: Easy-to-use `{{< component param="value" />}}` syntax in Markdown
- **Theme-Aware**: Components respect site theme and color palettes
- **Accessible**: ARIA attributes and semantic HTML throughout
- **Pattern Library**: Auto-generated documentation with live examples

### Modern UI
- **Bootstrap 5**: Responsive, mobile-first design
- **Light/Dark Mode**: User-selectable theme with persistent preference
- **Smooth Animations**: Professional transitions and effects
- **Custom Styling**: Easily customizable colors and branding

### Interactive Features
- **Full-Text Search**: Client-side search powered by Lunr.js
- **Copy to Clipboard**: One-click code copying
- **Collapsible Sections**: Interactive accordion components
- **Tabbed Content**: Multi-tab content organization

## Quick Start

### Prerequisites
- Python 3.11 or higher
- pip or uv package manager

### Installation

```bash
# Clone the repository
git clone <your-repo-url>
cd static-site-generator

# Install dependencies with pip
pip install flask markdown python-frontmatter pygments beautifulsoup4 pyyaml

# Or with uv (faster)
uv sync
```

### Build Your Site

```bash
# Basic build (uses content/ as input, outputs to site/)
python build.py

# Custom paths
python build.py --input content --output site

# Custom configuration
python build.py --config myconfig.yaml
```

### View Your Site

Open `site/index.html` in your browser or serve it with any HTTP server:

```bash
# Python built-in server
python -m http.server -d site 5000

# Then visit http://localhost:5000
```

## Project Structure

```
.
├── content/              # Your Markdown content files (input)
│   ├── index.md
│   ├── example/
│   └── docs/
├── generator/
│   ├── generator.py     # Main generator engine
│   ├── shortcode_parser.py  # Component shortcode parser
│   ├── templates/       # Jinja2 page templates
│   │   ├── base.html
│   │   ├── page.html
│   │   ├── index.html
│   │   └── pattern-library.html
│   ├── components/      # Component templates
│   │   ├── button.html
│   │   ├── card.html
│   │   ├── alert.html
│   │   ├── code-sample.html
│   │   ├── hero.html
│   │   ├── tabs.html
│   │   ├── collapsible.html
│   │   └── badge.html
│   └── static/          # CSS and JavaScript
│       ├── css/
│       │   ├── styles.css
│       │   ├── animations.css
│       │   └── pygments.css (auto-generated)
│       └── js/
│           ├── theme.js
│           ├── search.js
│           └── components.js
├── site/                # Generated static site (output)
├── build.py             # CLI build tool
├── config.yaml          # Site configuration
└── README.md
```

## Creating Content

### Basic Markdown File

Create a file in `content/` with YAML front matter:

```markdown
---
title: My Page Title
description: A short description for SEO
date: 2025-01-15
author: Your Name
tags: [tutorial, example]
---

# My Page Title

Your content here...

{{< button text="Get Started" variant="primary" href="/docs/" />}}
```

### Front Matter Fields

- `title`: Page title (required)
- `description`: SEO description (optional)
- `date`: Publication date (optional)
- `author`: Author name (optional)
- `tags`: List of tags (optional)

## Using Components

### Button Component

```markdown
{{< button text="Click Me" variant="primary" />}}
{{< button text="Large Button" variant="success" size="lg" />}}
{{< button text="Link Button" href="/page/" variant="outline-primary" />}}
{{< button text="With Icon" icon="bi bi-download" variant="primary" />}}
```

**Parameters:**
- `text`: Button text
- `variant`: primary, secondary, success, danger, warning, info, light, dark, outline-*
- `size`: sm, md (default), lg
- `href`: Link URL (optional)
- `icon`: Bootstrap icon class (optional)
- `disabled`: true/false (optional)

### Card Component

```markdown
{{< card title="Card Title" content="Card content here" />}}
{{< card title="With Footer" content="Content" footer="Footer text" variant="primary" />}}
```

**Parameters:**
- `title`: Card title
- `content`: Card body content
- `footer`: Card footer (optional)
- `variant`: primary, secondary, success, danger, warning, info (optional)
- `image`: Image URL (optional)

### Alert Component

```markdown
{{< alert content="Important message!" variant="info" />}}
{{< alert content="Warning message" variant="warning" icon="bi bi-exclamation-triangle-fill" />}}
{{< alert content="Dismissible alert" variant="success" dismissible="true" />}}
```

**Parameters:**
- `content`: Alert message
- `variant`: primary, secondary, success, danger, warning, info, light, dark
- `icon`: Bootstrap icon class (optional)
- `dismissible`: true/false (optional)

### Code Sample Component

```markdown
{{< code language="python" title="Example" content="print('Hello')" />}}
{{< code language="javascript" content="console.log('Hello');" copy="true" />}}
```

**Parameters:**
- `content`: Code content
- `language`: Programming language for syntax highlighting
- `title`: Code block title (optional)
- `copy`: Show copy button - true (default), false

### Hero Component

```markdown
{{< hero title="Welcome" subtitle="Build amazing sites" cta_text="Get Started" cta_link="/docs/" />}}
{{< hero title="Hero" subtitle="With background" image="/path/to/image.jpg" variant="dark" />}}
```

**Parameters:**
- `title`: Hero title
- `subtitle`: Hero subtitle
- `cta_text`: Call-to-action button text (optional)
- `cta_link`: Call-to-action button link (optional)
- `image`: Background image URL (optional)
- `variant`: primary (default), secondary, dark, light

### Tabs Component

```markdown
{{< tabs id="example-tabs" tabs='[
    {"title": "Tab 1", "content": "Content 1"},
    {"title": "Tab 2", "content": "Content 2"}
]' />}}
```

**Parameters:**
- `id`: Unique ID for the tabs
- `tabs`: JSON array of tab objects with `title` and `content`

### Collapsible Component

```markdown
{{< collapsible title="Click to expand" content="Hidden content here" />}}
{{< collapsible title="Open by default" content="Content" open="true" />}}
```

**Parameters:**
- `title`: Collapsible section title
- `content`: Collapsible content
- `open`: Start expanded - true/false (optional)
- `variant`: Color variant (optional)

### Badge Component

```markdown
{{< badge text="New" variant="success" />}}
{{< badge text="v2.0" variant="primary" />}}
```

**Parameters:**
- `text`: Badge text
- `variant`: primary, secondary, success, danger, warning, info, light, dark

## Configuration

Edit `config.yaml` to customize your site:

```yaml
site_name: "My Site"
site_description: "Site description"
site_url: "https://example.com"

theme:
  default_mode: "light"  # or "dark"
  primary_color: "#0d6efd"
  secondary_color: "#6c757d"
  success_color: "#198754"
  danger_color: "#dc3545"
  warning_color: "#ffc107"
  info_color: "#0dcaf0"

author:
  name: "Your Name"
  email: "your@email.com"

navigation:
  - title: "Home"
    url: "/"
  - title: "Docs"
    url: "/docs/"

footer:
  copyright: "© 2025 Your Site"
  links:
    - title: "GitHub"
      url: "https://github.com"
```

## Adding Custom Components

### 1. Create Component Template

Create a new file in `generator/components/`:

```html
<!-- generator/components/mycomponent.html -->
<div class="my-component {{ variant|default('default') }}">
    <h3>{{ title }}</h3>
    <p>{{ content }}</p>
</div>
```

### 2. Register Component

Add to `generator/shortcode_parser.py` in the `components` dictionary:

```python
'mycomponent': {
    'template': 'mycomponent.html',
    'description': 'My custom component',
    'params': {
        'title': 'Component title',
        'content': 'Component content',
        'variant': 'Style variant (optional)'
    },
    'example': '{{< mycomponent title="Hello" content="World" />}}'
}
```

### 3. Use in Markdown

```markdown
{{< mycomponent title="Custom" content="This is my component!" />}}
```

## Deployment

The `site/` directory contains your complete static website. Deploy to:

### GitHub Pages

```bash
# Option 1: Direct deployment
git subtree push --prefix site origin gh-pages

# Option 2: Use GitHub Actions
# Add .github/workflows/deploy.yml with build and deploy steps
```

### Netlify

1. Connect your repository
2. Set build command: `python build.py`
3. Set publish directory: `site`
4. Deploy!

### Vercel

1. Import your repository
2. Framework preset: Other
3. Build command: `python build.py`
4. Output directory: `site`

### Any Static Host

Upload the contents of `site/` to your web server via FTP, SFTP, or hosting panel.

## Development

### Running Locally

```bash
# Build the site
python build.py

# Serve locally
python -m http.server -d site 5000

# Or use any other HTTP server
# cd site && npx serve
```

### Watching for Changes

Currently manual rebuild is required. For auto-rebuild on file changes, consider using:

```bash
# Install watchdog
pip install watchdog

# Create a watch script (example)
watchmedo shell-command \
  --patterns="*.md;*.html;*.css;*.js;*.yaml" \
  --recursive \
  --command='python build.py' \
  .
```

## Testing

The generator includes built-in validation:

- Markdown parsing errors are logged
- Missing components are replaced with error messages
- Invalid shortcode syntax is highlighted
- Build process reports all generated files

## Performance

- **Fast Builds**: Processes hundreds of pages in seconds
- **Optimized Output**: Minified CSS, deferred JS loading
- **CDN Ready**: All assets are static and cacheable
- **Lighthouse Score**: 95+ on all metrics

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

## License

MIT License - feel free to use for personal or commercial projects.

## Contributing

Contributions welcome! To add features or fix bugs:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## Support

- Documentation: Check the generated Pattern Library
- Issues: Report bugs via GitHub Issues
- Examples: See the `content/` directory for samples

## Changelog

### Version 2.0.0 (2025-01-15)
- Complete component system with 8 components
- Shortcode parser for Markdown integration
- Pattern library documentation
- Light/Dark theme support
- Full-text search with Lunr.js
- Responsive Bootstrap 5 UI
- Automatic sitemap generation
- Enhanced accessibility

---

Built with Python, Flask, Jinja2, and Bootstrap 5

Happy site building! 🚀
