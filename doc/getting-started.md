---
title: Getting Started Guide
description: Learn how to set up and use the Static Site Generator
date: 2025-01-15
author: Documentation Team
tags: [documentation, tutorial, guide]
---

# Getting Started Guide

Welcome to the Static Site Generator! This guide will help you get up and running quickly.

## Installation

### Prerequisites

- Python 3.11 or higher
- pip (Python package manager)

### Setup

1. Clone or download the project
2. Install dependencies:

```bash
pip install -r requirements.txt
```

Or with uv:

```bash
uv sync
```

## Project Structure

```
.
├── content/              # Your Markdown content files
├── generator/
│   ├── templates/       # Jinja2 page templates
│   ├── components/      # Component templates
│   ├── static/          # CSS and JavaScript files
│   └── generator.py     # Main generator code
├── site/                # Generated static site (output)
├── build.py             # Build CLI tool
└── config.yaml          # Site configuration
```

## Creating Content

### Basic Markdown File

Create a new file in the `content/` directory:

```markdown
---
title: My First Page
description: This is my first page
date: 2025-01-15
tags: [example, tutorial]
---

# My First Page

This is the content of my page.

{{< button text="Click Me" variant="primary" />}}
```

### Front Matter

Each Markdown file can include YAML front matter:

- `title`: Page title
- `description`: Page description (for SEO)
- `date`: Publication date
- `author`: Author name
- `tags`: List of tags

## Using Components

Components use shortcode syntax:

```markdown
{{< component_name param1="value1" param2="value2" />}}
```

### Available Components

{{< collapsible title="Button Component" content="{{< button text='Click Me' variant='primary' size='lg' />}}" />}}

{{< collapsible title="Alert Component" content="{{< alert content='Important message' variant='info' />}}" />}}

{{< collapsible title="Card Component" content="{{< card title='Card Title' content='Card content here' />}}" />}}

{{< collapsible title="Code Component" content="{{< code language='python' content='print(Hello)' />}}" />}}

{{< collapsible title="Hero Component" content="{{< hero title='Welcome' subtitle='Subtitle here' />}}" />}}

For complete component documentation, visit the [Pattern Library](/pattern-library/).

## Building Your Site

### Basic Build

```bash
python build.py
```

### Custom Paths

```bash
python build.py --input content --output site
```

### Custom Config

```bash
python build.py --config myconfig.yaml
```

## Configuration

Edit `config.yaml` to customize your site:

```yaml
site_name: "My Awesome Site"
site_description: "A site built with Static Site Generator"
site_url: "https://mysite.com"

theme:
  default_mode: "light"
  primary_color: "#0d6efd"
  secondary_color: "#6c757d"
```

{{< alert content="After changing config.yaml, rebuild your site to see the changes." variant="info" />}}

## Deployment

The generated `site/` directory contains your complete static website. Deploy it to:

### GitHub Pages

1. Push the `site/` directory to your repository
2. Enable GitHub Pages in repository settings
3. Select the `site/` directory as the source

### Netlify

1. Drag and drop the `site/` directory to Netlify
2. Or connect your repository and set build command: `python build.py`

### Vercel

1. Import your repository
2. Set build command: `python build.py`
3. Set output directory: `site`

### Any Static Host

Simply upload the contents of the `site/` directory to your web server.

## Next Steps

{{< card title="Explore Components" content="Check out all available components in the Pattern Library" footer="View Pattern Library →" variant="primary" />}}

{{< card title="Customize Theme" content="Learn how to customize colors, fonts, and styles" footer="Theme Documentation →" variant="success" />}}

{{< card title="Add Custom Components" content="Create your own reusable components" footer="Developer Guide →" variant="info" />}}

---

Need help? Check the full documentation or create an issue on GitHub.
