# Getting Started with MarkSite

Welcome to MarkSite! This guide will help you set up and start building beautiful static websites in minutes.

## Table of Contents

- [Installation](#installation)
- [Your First Site](#your-first-site)
- [Creating Content](#creating-content)
- [Building Your Site](#building-your-site)
- [Local Development](#local-development)
- [Next Steps](#next-steps)

## Installation

### Prerequisites

Before you begin, ensure you have:
- Python 3.11 or higher installed
- pip package manager
- Git (optional, for cloning)

Check your Python version:
```bash
python --version
# or
python3 --version
```

### Step 1: Get MarkSite

Clone the repository:
```bash
git clone https://github.com/Alqudimi/MarkSite.git
cd MarkSite
```

Or download the ZIP file from GitHub and extract it.

### Step 2: Install Dependencies

Install all required Python packages:
```bash
pip install -r requirements.txt
```

Or if you prefer using pip3:
```bash
pip3 install -r requirements.txt
```

### Step 3: Verify Installation

Test that everything is working:
```bash
python build.py --help
```

You should see the help message with all available options.

## Your First Site

### Step 1: Explore the Sample Content

MarkSite comes with sample content in the `content/` directory:

```
content/
├── index.md              # Homepage
├── docs/
│   └── getting-started.md
└── example/
    └── components-demo.md
```

### Step 2: Build the Site

Run the build command:
```bash
python build.py
```

You'll see output like:
```
Building site from content to site...
Using template: default
Found 3 Markdown files
Processing: content/index.md
Processing: content/docs/getting-started.md
Processing: content/example/components-demo.md
✓ Site generated successfully in site/
```

### Step 3: View Your Site

Serve the site locally:
```bash
python -m http.server -d site 8000
```

Open your browser and visit: `http://localhost:8000`

## Creating Content

### Basic Markdown File

Create a new file in the `content/` directory:

```markdown
---
title: My First Post
description: This is my first post with MarkSite
date: 2025-10-25
author: Your Name
tags: [tutorial, getting-started]
---

# My First Post

Welcome to my new static site! This is built with **MarkSite**.

## Features I Love

- Fast static site generation
- Beautiful templates
- Easy to use components

{{< button text="Learn More" variant="primary" href="/docs/" />}}
```

### Front Matter Explained

The YAML front matter at the top of each file contains metadata:

- **title** (required): Page title shown in browser tab and headings
- **description** (optional): SEO description for search engines
- **date** (optional): Publication date (YYYY-MM-DD format)
- **author** (optional): Content author name
- **tags** (optional): List of tags for categorization

### Using Components

Add interactive components using shortcode syntax:

```markdown
{{< alert content="Welcome to MarkSite!" variant="success" />}}

{{< card 
    title="Quick Tip" 
    content="You can nest components for complex layouts!" 
    variant="info" 
/>}}

{{< button text="Get Started" variant="primary" size="lg" />}}
```

See [Components Guide](COMPONENTS.md) for all available components.

## Building Your Site

### Basic Build

Generate your site with default settings:
```bash
python build.py
```

### Choose a Template

Build with a specific template:
```bash
python build.py --template minimalist
```

Available templates: `default`, `minimalist`, `techblog`, `documentation`, `portfolio`, `magazine`, `landing`, `creative`, `personalblog`, `inkwell`, `futuristic`, `monochrome`, `oasis`, `retrowave` (14 total)

### Custom Paths

Specify custom input/output directories:
```bash
python build.py --input my-content --output my-site
```

### Custom Configuration

Use a custom config file:
```bash
python build.py --config custom-config.yaml
```

### Combined Options

Combine multiple options:
```bash
python build.py --template techblog --output blog --config blog-config.yaml
```

## Local Development

### Development Workflow

1. **Edit Content**: Modify Markdown files in `content/`
2. **Rebuild**: Run `python build.py`
3. **Refresh Browser**: Reload to see changes

### Quick Rebuild Script

Create a bash script `rebuild.sh`:
```bash
#!/bin/bash
python build.py && echo "✓ Site rebuilt successfully!"
```

Make it executable:
```bash
chmod +x rebuild.sh
./rebuild.sh
```

### Auto-Rebuild (Optional)

For automatic rebuilds on file changes, install watchdog:
```bash
pip install watchdog
```

Create `watch.sh`:
```bash
#!/bin/bash
watchmedo shell-command \
  --patterns="*.md;*.html;*.css;*.js;*.yaml" \
  --recursive \
  --command='python build.py' \
  content/ generator/
```

Run it:
```bash
chmod +x watch.sh
./watch.sh
```

### Testing Different Templates

Quickly test different templates:
```bash
# Try each template
for template in default minimalist techblog documentation portfolio; do
  python build.py --template $template --output "preview-$template"
  echo "Built $template template in preview-$template/"
done
```

## Project Configuration

Edit `config.yaml` to customize your site:

```yaml
site_name: "My Awesome Site"
site_description: "A site built with MarkSite"
site_url: "https://mysite.com"

# Choose your template
template: "minimalist"

# Customize colors
theme:
  default_mode: "light"
  primary_color: "#0d6efd"
  secondary_color: "#6c757d"

# Author info
author:
  name: "Your Name"
  email: "your@email.com"

# Navigation menu
navigation:
  - title: "Home"
    url: "/"
  - title: "Blog"
    url: "/blog/"
  - title: "About"
    url: "/about/"

# Footer
footer:
  copyright: "© 2025 Your Name"
  links:
    - title: "GitHub"
      url: "https://github.com/yourusername"
    - title: "Contact"
      url: "/contact/"
```

See [Configuration Guide](CONFIGURATION.md) for all options.

## Directory Structure

Organize your content logically:

```
content/
├── index.md                 # Homepage
├── about.md                 # About page
├── blog/                    # Blog posts
│   ├── 2025-01-15-first-post.md
│   └── 2025-01-20-second-post.md
├── docs/                    # Documentation
│   ├── getting-started.md
│   └── advanced.md
└── projects/                # Portfolio items
    ├── project-1.md
    └── project-2.md
```

URLs will match your directory structure:
- `content/about.md` → `/about/`
- `content/blog/first-post.md` → `/blog/first-post/`
- `content/docs/getting-started.md` → `/docs/getting-started/`

## Next Steps

Now that you've got the basics down:

1. **Explore Templates**: Try different templates to find your style
   - [Template Guide](TEMPLATES.md)

2. **Learn Components**: Master all 8 built-in components
   - [Component Guide](COMPONENTS.md)

3. **Customize Configuration**: Tailor your site to your needs
   - [Configuration Guide](CONFIGURATION.md)

4. **Deploy Your Site**: Get your site online
   - [Deployment Guide](DEPLOYMENT.md)

5. **Create Custom Components**: Extend MarkSite with your own components
   - [Custom Components Guide](CUSTOM_COMPONENTS.md)

## Common Tasks

### Adding a New Page

1. Create `content/my-page.md`
2. Add front matter and content
3. Run `python build.py`
4. Access at `/my-page/`

### Adding a Blog Post

1. Create `content/blog/my-post.md`
2. Add front matter with date and tags
3. Rebuild site
4. Access at `/blog/my-post/`

### Changing Theme

Edit `config.yaml`:
```yaml
template: "techblog"  # Change to any template name
```

Rebuild:
```bash
python build.py
```

### Adding Images

1. Place images in `generator/static/images/` or reference external URLs
2. Use in Markdown:
```markdown
![Alt text](/static/images/photo.jpg)
```

### Adding Custom CSS

Create `generator/static/css/custom.css` and add your styles. The file will be automatically copied to the output.

## Troubleshooting

### Build Errors

**Problem**: Module not found error
```
ModuleNotFoundError: No module named 'markdown'
```

**Solution**: Install dependencies
```bash
pip install -r requirements.txt
```

**Problem**: Permission denied
```
PermissionError: [Errno 13] Permission denied: 'site'
```

**Solution**: Close any programs accessing the `site/` folder, or use a different output directory:
```bash
python build.py --output website
```

### Content Not Showing

**Problem**: Page not appearing in navigation

**Solution**: Add it to `config.yaml` navigation:
```yaml
navigation:
  - title: "My Page"
    url: "/my-page/"
```

### Search Not Working

**Problem**: Search returns no results

**Solution**: 
1. Rebuild site to regenerate search index
2. Ensure you're serving via HTTP (search doesn't work with `file://` URLs)

## Getting Help

- **Documentation**: Check other guides in `doc/` folder
- **Issues**: Report bugs at [GitHub Issues](https://github.com/Alqudimi/MarkSite/issues)
- **Examples**: See sample content in `content/` directory
- **Email**: Contact eng7mi@gmail.com

## Additional Resources

- [Component Reference](COMPONENTS.md) - All components with examples
- [Template Gallery](TEMPLATES.md) - All 14 templates showcased
- [Deployment Options](DEPLOYMENT.md) - Host your site anywhere
- [Advanced Configuration](CONFIGURATION.md) - Deep customization

---

Happy building with MarkSite! 🚀

**Author**: Abdulaziz Al-Qadimi  
**GitHub**: [@Alqudimi](https://github.com/Alqudimi)  
**Repository**: [MarkSite](https://github.com/Alqudimi/MarkSite)
