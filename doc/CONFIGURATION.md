# Configuration Guide

Complete guide to configuring your MarkSite static site using `config.yaml`.

## Table of Contents

- [Configuration File](#configuration-file)
- [Site Settings](#site-settings)
- [Template Selection](#template-selection)
- [Theme Configuration](#theme-configuration)
- [Author Information](#author-information)
- [Navigation Menu](#navigation-menu)
- [Footer Configuration](#footer-configuration)
- [Advanced Options](#advanced-options)
- [Multiple Configurations](#multiple-configurations)

## Configuration File

MarkSite uses `config.yaml` for all site configuration. This YAML file controls your site's appearance, behavior, and content.

### Default Configuration

```yaml
site_name: "MarkSite"
site_description: "A powerful, component-based static site generator"
site_url: "https://example.com"

template: "default"

theme:
  default_mode: "light"
  primary_color: "#0d6efd"
  secondary_color: "#6c757d"
  success_color: "#198754"
  danger_color: "#dc3545"
  warning_color: "#ffc107"
  info_color: "#0dcaf0"
  
author:
  name: "Your Name"
  email: "your.email@example.com"
  
navigation:
  - title: "Home"
    url: "/"
  - title: "Pattern Library"
    url: "/pattern-library/"
  - title: "Documentation"
    url: "/docs/"

footer:
  copyright: "© 2025 Your Name. All rights reserved."
  links:
    - title: "GitHub"
      url: "https://github.com"
    - title: "Documentation"
      url: "/docs/"
```

## Site Settings

### site_name

**Type**: String  
**Required**: Yes  
**Description**: Your website's name, displayed in the header and browser title.

```yaml
site_name: "My Awesome Blog"
```

Appears in:
- Browser tab title
- Site header
- Meta tags
- Social media shares

### site_description

**Type**: String  
**Required**: Yes  
**Description**: Brief description of your site for SEO and social media.

```yaml
site_description: "A blog about web development, Python, and technology"
```

Used for:
- Meta description tag
- Search engine results
- Social media previews
- RSS feeds (if enabled)

**Best Practices**:
- Keep under 160 characters
- Include relevant keywords
- Make it compelling and accurate

### site_url

**Type**: String (URL)  
**Required**: Yes  
**Description**: Your site's full URL, used for generating absolute links.

```yaml
site_url: "https://myblog.com"
```

Important for:
- Sitemap generation
- Social media tags
- RSS feeds
- Canonical URLs

**Note**: Include protocol (`https://`) and exclude trailing slash.

## Template Selection

### template

**Type**: String  
**Required**: No  
**Default**: `"default"`  
**Description**: Choose from 14 professional templates.

```yaml
template: "minimalist"
```

**Available Templates**:
- `default` - Classic Bootstrap design
- `minimalist` - Clean, spacious layout
- `techblog` - Dark theme for developers
- `documentation` - Technical documentation style
- `portfolio` - Creative showcase design
- `magazine` - Editorial news layout
- `landing` - Conversion-focused page
- `creative` - Bold artistic design
- `personalblog` - Warm blogging theme
- `inkwell` - Literary magazine style
- `futuristic` - Sci-fi modern design
- `monochrome` - Black and white elegance
- `oasis` - Nature-inspired calming design
- `retrowave` - 80s neon aesthetics

See [Template Guide](TEMPLATES.md) for details on each template.

**Override in CLI**:
```bash
python build.py --template techblog
```

## Theme Configuration

### default_mode

**Type**: String  
**Required**: No  
**Default**: `"light"`  
**Options**: `"light"` or `"dark"`  
**Description**: Default theme mode when users first visit.

```yaml
theme:
  default_mode: "dark"
```

**Note**: Users can toggle between light/dark mode; this sets initial state.

### Color Customization

Customize your site's color palette:

```yaml
theme:
  primary_color: "#0d6efd"      # Main brand color
  secondary_color: "#6c757d"    # Secondary/muted color
  success_color: "#198754"      # Success messages
  danger_color: "#dc3545"       # Error messages
  warning_color: "#ffc107"      # Warning messages
  info_color: "#0dcaf0"         # Info messages
```

**Color Guidelines**:
- Use hex format (`#RRGGBB`)
- Ensure sufficient contrast for accessibility
- Test in both light and dark modes
- Consider color blindness

**Examples**:

**Brand Colors**:
```yaml
theme:
  primary_color: "#FF6B6B"    # Coral red
  secondary_color: "#4ECDC4"  # Turquoise
```

**Professional**:
```yaml
theme:
  primary_color: "#2C3E50"    # Dark blue-gray
  secondary_color: "#95A5A6"  # Light gray
```

**Vibrant**:
```yaml
theme:
  primary_color: "#9B59B6"    # Purple
  secondary_color: "#3498DB"  # Blue
```

## Author Information

Configure author/owner details:

```yaml
author:
  name: "Jane Smith"
  email: "jane@example.com"
```

### name

**Type**: String  
**Required**: No  
**Description**: Your name or site owner's name.

Appears in:
- Footer copyright
- Meta tags
- About sections

### email

**Type**: String  
**Required**: No  
**Description**: Contact email address.

**Note**: Consider privacy; only include if you want it public.

## Navigation Menu

Configure your site's main navigation menu:

```yaml
navigation:
  - title: "Home"
    url: "/"
  - title: "Blog"
    url: "/blog/"
  - title: "About"
    url: "/about/"
  - title: "Contact"
    url: "/contact/"
```

### Navigation Item Structure

Each menu item requires:
- `title`: Link text
- `url`: Link destination (relative or absolute)

**Best Practices**:
- Keep menu items to 5-7 for usability
- Use clear, concise titles
- Order by importance (Home first)
- Use relative URLs for internal pages

**Internal Links** (recommended):
```yaml
navigation:
  - title: "Docs"
    url: "/docs/"          # Relative URL
```

**External Links**:
```yaml
navigation:
  - title: "GitHub"
    url: "https://github.com/username"  # Absolute URL
```

**Dropdown/Hierarchical**:
Currently not supported; keep menu flat.

## Footer Configuration

### copyright

**Type**: String  
**Required**: No  
**Description**: Copyright notice displayed in footer.

```yaml
footer:
  copyright: "© 2025 Jane Smith. All rights reserved."
```

**Dynamic Year** (optional):
The year can be updated manually each year, or you can use a static year.

### links

**Type**: List  
**Required**: No  
**Description**: Footer links (social media, legal pages, etc.).

```yaml
footer:
  links:
    - title: "Privacy Policy"
      url: "/privacy/"
    - title: "Terms"
      url: "/terms/"
    - title: "GitHub"
      url: "https://github.com/username"
    - title: "Twitter"
      url: "https://twitter.com/username"
```

**Common Footer Links**:
- Privacy Policy
- Terms of Service
- Contact
- About
- Social media profiles
- RSS feed

## Advanced Options

### Custom Configuration Files

Use different configs for different purposes:

**Development**:
```yaml
# config.dev.yaml
site_url: "http://localhost:8000"
theme:
  default_mode: "light"
```

**Production**:
```yaml
# config.prod.yaml
site_url: "https://mysite.com"
theme:
  default_mode: "light"
```

Build with specific config:
```bash
python build.py --config config.prod.yaml
```

### Environment-Specific Settings

**Local Development**:
```yaml
site_name: "[DEV] My Site"
site_url: "http://localhost:8000"
```

**Staging**:
```yaml
site_name: "[STAGING] My Site"
site_url: "https://staging.mysite.com"
```

**Production**:
```yaml
site_name: "My Site"
site_url: "https://mysite.com"
```

## Complete Configuration Examples

### Personal Blog

```yaml
site_name: "Jane's Tech Blog"
site_description: "Thoughts on web development, Python, and software engineering"
site_url: "https://janeblog.com"

template: "personalblog"

theme:
  default_mode: "light"
  primary_color: "#c17d5c"
  secondary_color: "#8b7355"

author:
  name: "Jane Smith"
  email: "jane@janeblog.com"

navigation:
  - title: "Home"
    url: "/"
  - title: "Blog"
    url: "/blog/"
  - title: "About"
    url: "/about/"
  - title: "Contact"
    url: "/contact/"

footer:
  copyright: "© 2025 Jane Smith"
  links:
    - title: "RSS"
      url: "/feed.xml"
    - title: "Twitter"
      url: "https://twitter.com/janesmith"
```

### Portfolio Site

```yaml
site_name: "John Doe Design"
site_description: "Creative portfolio of John Doe - UI/UX Designer"
site_url: "https://johndoe.design"

template: "portfolio"

theme:
  default_mode: "dark"
  primary_color: "#ffd700"
  secondary_color: "#2d2d2d"

author:
  name: "John Doe"
  email: "hello@johndoe.design"

navigation:
  - title: "Work"
    url: "/"
  - title: "About"
    url: "/about/"
  - title: "Contact"
    url: "/contact/"

footer:
  copyright: "© 2025 John Doe. All rights reserved."
  links:
    - title: "Dribbble"
      url: "https://dribbble.com/johndoe"
    - title: "Behance"
      url: "https://behance.net/johndoe"
    - title: "Instagram"
      url: "https://instagram.com/johndoe"
```

### Documentation Site

```yaml
site_name: "MyApp Documentation"
site_description: "Complete guide and API reference for MyApp"
site_url: "https://docs.myapp.com"

template: "documentation"

theme:
  default_mode: "light"
  primary_color: "#0066cc"
  secondary_color: "#6c757d"

author:
  name: "MyApp Team"
  email: "docs@myapp.com"

navigation:
  - title: "Home"
    url: "/"
  - title: "Getting Started"
    url: "/getting-started/"
  - title: "API Reference"
    url: "/api/"
  - title: "Examples"
    url: "/examples/"
  - title: "FAQ"
    url: "/faq/"

footer:
  copyright: "© 2025 MyApp Inc."
  links:
    - title: "GitHub"
      url: "https://github.com/myapp/myapp"
    - title: "Support"
      url: "/support/"
    - title: "Status"
      url: "https://status.myapp.com"
```

### Tech Blog

```yaml
site_name: "DevInsights"
site_description: "In-depth tutorials and insights on modern web development"
site_url: "https://devinsights.dev"

template: "techblog"

theme:
  default_mode: "dark"
  primary_color: "#00ff88"
  secondary_color: "#00ccff"

author:
  name: "Alex Developer"
  email: "alex@devinsights.dev"

navigation:
  - title: "Home"
    url: "/"
  - title: "Tutorials"
    url: "/tutorials/"
  - title: "Tips"
    url: "/tips/"
  - title: "About"
    url: "/about/"

footer:
  copyright: "© 2025 DevInsights"
  links:
    - title: "GitHub"
      url: "https://github.com/alexdev"
    - title: "Twitter"
      url: "https://twitter.com/devinsights"
    - title: "Newsletter"
      url: "/newsletter/"
```

## Configuration Validation

### Common Issues

**Invalid YAML Syntax**:
```yaml
# WRONG - inconsistent indentation
navigation:
  - title: "Home"
  url: "/"

# CORRECT
navigation:
  - title: "Home"
    url: "/"
```

**Missing Quotes**:
```yaml
# WRONG - special characters need quotes
site_name: Jane's Blog

# CORRECT
site_name: "Jane's Blog"
```

**Invalid Colors**:
```yaml
# WRONG - missing #
theme:
  primary_color: "0d6efd"

# CORRECT
theme:
  primary_color: "#0d6efd"
```

### Testing Configuration

Test your config:
```bash
python build.py --config config.yaml
```

Check for errors in build output.

## Best Practices

### 1. Consistency
- Use consistent naming conventions
- Keep color palette cohesive
- Maintain navigation structure

### 2. Accessibility
- Ensure color contrast ratios meet WCAG standards
- Use descriptive navigation labels
- Test with screen readers

### 3. SEO
- Write compelling site descriptions
- Use accurate site URLs
- Keep navigation logical and hierarchical

### 4. Maintenance
- Document custom configurations
- Keep backup configs
- Version control your config files

### 5. Performance
- Minimize navigation items
- Use relative URLs when possible
- Keep footer links reasonable

---

**Author**: Abdulaziz Al-Qadimi  
**Email**: eng7mi@gmail.com  
**Repository**: [MarkSite](https://github.com/Alqudimi/MarkSite)
