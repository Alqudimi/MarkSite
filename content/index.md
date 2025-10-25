---
title: Welcome to Static Site Generator
description: A powerful, component-based static site generator built with Python and Flask
date: 2025-01-15
author: Static Site Generator
tags: [welcome, introduction, getting-started]
---

# Welcome to Static Site Generator

This is a modern, high-end static site generator that converts Markdown files into beautiful, responsive websites with a powerful component system.

## Key Features

- **Recursive Markdown Scanning**: Automatically finds and processes all `.md` files in nested directories
- **Component System**: Reusable, themeable components with shortcode syntax
- **Syntax Highlighting**: Beautiful code highlighting with Pygments
- **Full-Text Search**: Client-side search powered by Lunr.js
- **Theme Support**: Light/Dark mode with customizable color palettes
- **SEO Optimized**: Automatic sitemap generation and meta tags
- **Fully Static**: Deploy anywhere - GitHub Pages, Netlify, Vercel, or any static host

## Component Examples

### Buttons

{{< button text="Primary Button" variant="primary" />}}
{{< button text="Success Button" variant="success" />}}
{{< button text="Large Button" variant="danger" size="lg" />}}
{{< button text="Visit Documentation" href="/docs/" variant="outline-primary" />}}

### Alerts

{{< alert content="This is an informational alert with important details!" variant="info" icon="bi bi-info-circle-fill" />}}

{{< alert content="Success! Your operation completed successfully." variant="success" dismissible="true" />}}

{{< alert content="Warning: Please review this before proceeding." variant="warning" />}}

### Cards

{{< card title="Getting Started" content="Learn how to build amazing static sites with our comprehensive documentation and examples." footer="Read more →" variant="primary" />}}

### Hero Section

{{< hero title="Build Amazing Sites" subtitle="Create beautiful, fast, and modern static websites with our powerful component system" cta_text="Get Started Now" cta_link="/pattern-library/" />}}

### Badges

Documentation {{< badge text="New" variant="success" />}}
Tutorial {{< badge text="Updated" variant="info" />}}
API {{< badge text="v2.0" variant="primary" />}}

## Getting Started

1. Create Markdown files in the `content/` directory
2. Use components with shortcode syntax: `{{< component param="value" />}}`
3. Run the build: `python build.py`
4. Deploy the `site/` directory to your hosting platform

## Next Steps

- View the [Pattern Library](/pattern-library/) for all available components
- Explore the documentation
- Customize your theme in `config.yaml`
- Add your own custom components

{{< collapsible title="Advanced Configuration" content="You can customize colors, navigation, footer links, and more in the config.yaml file. The theme system supports custom color palettes and both light and dark modes." />}}

---

Built with ❤️ using Python, Flask, and Bootstrap
