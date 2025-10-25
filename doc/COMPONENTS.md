# Component Guide

MarkSite includes 8 powerful, customizable components that can be embedded directly in your Markdown content using shortcode syntax.

## Table of Contents

- [Button Component](#button-component)
- [Card Component](#card-component)
- [Alert Component](#alert-component)
- [Code Sample Component](#code-sample-component)
- [Hero Component](#hero-component)
- [Tabs Component](#tabs-component)
- [Collapsible Component](#collapsible-component)
- [Badge Component](#badge-component)
- [Component Best Practices](#component-best-practices)

## Shortcode Syntax

All components use the same shortcode syntax:

```markdown
{{< component_name param1="value1" param2="value2" />}}
```

- Self-closing: `{{< component />}}`
- Parameters are key="value" pairs
- Quotes required for values with spaces
- Case-sensitive parameter names

---

## Button Component

Interactive buttons with multiple styles, sizes, and optional icons.

### Basic Usage

```markdown
{{< button text="Click Me" variant="primary" />}}
```

### Parameters

| Parameter | Type | Required | Description | Default |
|-----------|------|----------|-------------|---------|
| `text` | string | Yes | Button text | - |
| `variant` | string | No | Button style variant | `primary` |
| `size` | string | No | Button size: `sm`, `md`, `lg` | `md` |
| `href` | string | No | Link URL (makes it a link button) | - |
| `icon` | string | No | Bootstrap icon class | - |
| `disabled` | boolean | No | Disable button | `false` |

### Variants

- `primary` - Primary brand color
- `secondary` - Secondary gray color
- `success` - Green success color
- `danger` - Red danger/error color
- `warning` - Yellow warning color
- `info` - Cyan info color
- `light` - Light background
- `dark` - Dark background
- `outline-primary`, `outline-secondary`, etc. - Outlined versions

### Examples

**Basic Buttons**
```markdown
{{< button text="Primary" variant="primary" />}}
{{< button text="Success" variant="success" />}}
{{< button text="Danger" variant="danger" />}}
```

**Sizes**
```markdown
{{< button text="Small" size="sm" />}}
{{< button text="Medium" size="md" />}}
{{< button text="Large" size="lg" />}}
```

**Link Buttons**
```markdown
{{< button text="Go to Docs" variant="primary" href="/docs/" />}}
{{< button text="External Link" variant="info" href="https://example.com" />}}
```

**With Icons**
```markdown
{{< button text="Download" icon="bi bi-download" variant="primary" />}}
{{< button text="Settings" icon="bi bi-gear" variant="secondary" />}}
{{< button text="Delete" icon="bi bi-trash" variant="danger" />}}
```

**Outline Buttons**
```markdown
{{< button text="Outline" variant="outline-primary" />}}
{{< button text="Outline Success" variant="outline-success" />}}
```

**Disabled Button**
```markdown
{{< button text="Disabled" variant="primary" disabled="true" />}}
```

---

## Card Component

Content cards with optional headers, footers, images, and color variants.

### Basic Usage

```markdown
{{< card title="Card Title" content="Card content goes here" />}}
```

### Parameters

| Parameter | Type | Required | Description | Default |
|-----------|------|----------|-------------|---------|
| `title` | string | Yes | Card title/header | - |
| `content` | string | Yes | Card body content | - |
| `footer` | string | No | Card footer text | - |
| `variant` | string | No | Color variant | - |
| `image` | string | No | Image URL for card top | - |

### Variants

- `primary`, `secondary`, `success`, `danger`, `warning`, `info`
- Applies colored border and header background

### Examples

**Basic Card**
```markdown
{{< card title="Welcome" content="This is a simple card component." />}}
```

**Card with Footer**
```markdown
{{< card 
    title="Featured Article" 
    content="Read our latest insights on web development." 
    footer="Published on Oct 25, 2025" 
/>}}
```

**Colored Cards**
```markdown
{{< card title="Success" content="Operation completed!" variant="success" />}}
{{< card title="Warning" content="Please review this." variant="warning" />}}
{{< card title="Info" content="Did you know?" variant="info" />}}
```

**Card with Image**
```markdown
{{< card 
    title="Beautiful Landscape" 
    content="Explore the mountains" 
    image="/static/images/mountain.jpg"
    footer="Photo by John Doe"
/>}}
```

**Full Example**
```markdown
{{< card 
    title="Complete Card" 
    content="This card has all features: image, colored border, and footer." 
    image="https://via.placeholder.com/400x200"
    variant="primary"
    footer="Last updated: Today"
/>}}
```

---

## Alert Component

Notification messages with icons, colors, and optional dismiss button.

### Basic Usage

```markdown
{{< alert content="This is an alert message!" variant="info" />}}
```

### Parameters

| Parameter | Type | Required | Description | Default |
|-----------|------|----------|-------------|---------|
| `content` | string | Yes | Alert message | - |
| `variant` | string | No | Alert color variant | `info` |
| `icon` | string | No | Bootstrap icon class | - |
| `dismissible` | boolean | No | Show dismiss button | `false` |

### Variants

- `primary`, `secondary`, `success`, `danger`, `warning`, `info`, `light`, `dark`

### Examples

**Basic Alerts**
```markdown
{{< alert content="Information message" variant="info" />}}
{{< alert content="Success! Changes saved." variant="success" />}}
{{< alert content="Warning: Check your input" variant="warning" />}}
{{< alert content="Error occurred" variant="danger" />}}
```

**With Icons**
```markdown
{{< alert content="Success!" variant="success" icon="bi bi-check-circle-fill" />}}
{{< alert content="Warning!" variant="warning" icon="bi bi-exclamation-triangle-fill" />}}
{{< alert content="Error!" variant="danger" icon="bi bi-x-circle-fill" />}}
{{< alert content="Info" variant="info" icon="bi bi-info-circle-fill" />}}
```

**Dismissible Alerts**
```markdown
{{< alert content="You can close this alert" variant="primary" dismissible="true" />}}
{{< alert content="Click X to dismiss" variant="success" dismissible="true" icon="bi bi-check" />}}
```

---

## Code Sample Component

Syntax-highlighted code blocks with optional copy button and titles.

### Basic Usage

```markdown
{{< code language="python" content="print('Hello, World!')" />}}
```

### Parameters

| Parameter | Type | Required | Description | Default |
|-----------|------|----------|-------------|---------|
| `content` | string | Yes | Code content | - |
| `language` | string | Yes | Programming language | - |
| `title` | string | No | Code block title | - |
| `copy` | boolean | No | Show copy button | `true` |

### Supported Languages

Python, JavaScript, HTML, CSS, Java, C, C++, Go, Rust, Ruby, PHP, Swift, Kotlin, TypeScript, SQL, Bash, and many more (via Pygments).

### Examples

**Python Code**
```markdown
{{< code language="python" content="def hello():\n    print('Hello!')" />}}
```

**JavaScript Code**
```markdown
{{< code language="javascript" content="const greeting = 'Hello';\nconsole.log(greeting);" />}}
```

**With Title**
```markdown
{{< code 
    language="python" 
    title="Example Function" 
    content="def add(a, b):\n    return a + b" 
/>}}
```

**HTML Code**
```markdown
{{< code 
    language="html" 
    content="<div class=\"container\">\n  <h1>Hello</h1>\n</div>" 
/>}}
```

**Without Copy Button**
```markdown
{{< code language="bash" content="npm install" copy="false" />}}
```

**Multi-line Code**
```markdown
{{< code 
    language="python" 
    title="Flask App" 
    content="from flask import Flask\n\napp = Flask(__name__)\n\n@app.route('/')\ndef home():\n    return 'Hello, World!'" 
/>}}
```

---

## Hero Component

Large hero sections with titles, subtitles, call-to-action buttons, and optional backgrounds.

### Basic Usage

```markdown
{{< hero title="Welcome" subtitle="Start building amazing sites" />}}
```

### Parameters

| Parameter | Type | Required | Description | Default |
|-----------|------|----------|-------------|---------|
| `title` | string | Yes | Hero title | - |
| `subtitle` | string | Yes | Hero subtitle | - |
| `cta_text` | string | No | Call-to-action button text | - |
| `cta_link` | string | No | Call-to-action button link | - |
| `image` | string | No | Background image URL | - |
| `variant` | string | No | Color variant | `primary` |

### Variants

- `primary`, `secondary`, `dark`, `light`

### Examples

**Basic Hero**
```markdown
{{< hero 
    title="Welcome to MarkSite" 
    subtitle="Build beautiful static sites with ease" 
/>}}
```

**With Call-to-Action**
```markdown
{{< hero 
    title="Get Started Today" 
    subtitle="Transform your Markdown into stunning websites" 
    cta_text="Start Building" 
    cta_link="/docs/" 
/>}}
```

**With Background Image**
```markdown
{{< hero 
    title="Beautiful Design" 
    subtitle="Professional templates included" 
    image="/static/images/hero-bg.jpg"
    variant="dark"
/>}}
```

**Different Variants**
```markdown
{{< hero title="Primary Hero" subtitle="With primary colors" variant="primary" />}}
{{< hero title="Dark Hero" subtitle="Dark background" variant="dark" />}}
{{< hero title="Light Hero" subtitle="Light background" variant="light" />}}
```

---

## Tabs Component

Organize content into tabbed sections for better navigation.

### Basic Usage

```markdown
{{< tabs id="example" tabs='[
    {"title": "Tab 1", "content": "Content 1"},
    {"title": "Tab 2", "content": "Content 2"}
]' />}}
```

### Parameters

| Parameter | Type | Required | Description | Default |
|-----------|------|----------|-------------|---------|
| `id` | string | Yes | Unique ID for the tabs | - |
| `tabs` | JSON | Yes | Array of tab objects | - |

### Tab Object Structure

Each tab object must have:
- `title`: Tab label
- `content`: Tab content (supports HTML)

### Examples

**Simple Tabs**
```markdown
{{< tabs id="basic-tabs" tabs='[
    {"title": "Overview", "content": "This is the overview section."},
    {"title": "Details", "content": "Here are the details."}
]' />}}
```

**Code Examples in Tabs**
```markdown
{{< tabs id="code-tabs" tabs='[
    {"title": "Python", "content": "<pre>print(\"Hello\")</pre>"},
    {"title": "JavaScript", "content": "<pre>console.log(\"Hello\")</pre>"},
    {"title": "Ruby", "content": "<pre>puts \"Hello\"</pre>"}
]' />}}
```

**Documentation Tabs**
```markdown
{{< tabs id="install-tabs" tabs='[
    {"title": "pip", "content": "<code>pip install marksite</code>"},
    {"title": "git", "content": "<code>git clone https://github.com/Alqudimi/MarkSite</code>"}
]' />}}
```

---

## Collapsible Component

Accordion-style expandable sections for organizing content.

### Basic Usage

```markdown
{{< collapsible title="Click to expand" content="Hidden content here" />}}
```

### Parameters

| Parameter | Type | Required | Description | Default |
|-----------|------|----------|-------------|---------|
| `title` | string | Yes | Section title (always visible) | - |
| `content` | string | Yes | Collapsible content | - |
| `open` | boolean | No | Start expanded | `false` |
| `variant` | string | No | Color variant | - |

### Examples

**Basic Collapsible**
```markdown
{{< collapsible title="FAQ: What is MarkSite?" content="MarkSite is a static site generator." />}}
```

**Open by Default**
```markdown
{{< collapsible title="Important Notice" content="Read this first!" open="true" />}}
```

**FAQ Section**
```markdown
{{< collapsible title="How do I install?" content="Run: pip install -r requirements.txt" />}}
{{< collapsible title="How do I build?" content="Run: python build.py" />}}
{{< collapsible title="How do I deploy?" content="Upload the site/ folder to any static host" />}}
```

**With Variant**
```markdown
{{< collapsible title="Success Tips" content="Follow best practices" variant="success" />}}
{{< collapsible title="Warning" content="Be careful with this" variant="warning" />}}
```

---

## Badge Component

Small labels and tags for highlighting information.

### Basic Usage

```markdown
{{< badge text="New" variant="success" />}}
```

### Parameters

| Parameter | Type | Required | Description | Default |
|-----------|------|----------|-------------|---------|
| `text` | string | Yes | Badge text | - |
| `variant` | string | No | Color variant | `primary` |

### Variants

- `primary`, `secondary`, `success`, `danger`, `warning`, `info`, `light`, `dark`

### Examples

**Status Badges**
```markdown
{{< badge text="New" variant="success" />}}
{{< badge text="Beta" variant="warning" />}}
{{< badge text="Deprecated" variant="danger" />}}
```

**Version Badges**
```markdown
Version {{< badge text="2.0" variant="primary" />}}
{{< badge text="Stable" variant="success" />}}
```

**Category Tags**
```markdown
{{< badge text="Tutorial" variant="info" />}}
{{< badge text="Advanced" variant="warning" />}}
{{< badge text="Python" variant="primary" />}}
```

---

## Component Best Practices

### 1. Accessibility

- Use descriptive button text
- Provide meaningful alert messages
- Use semantic heading levels in cards
- Ensure sufficient color contrast

### 2. Performance

- Minimize nested components
- Use appropriate component for the task
- Avoid excessive tabs/collapsibles on one page

### 3. Content Organization

- Group related content in cards
- Use tabs for alternative content (e.g., different code languages)
- Use collapsibles for supplementary information (FAQs, details)

### 4. Visual Hierarchy

- Use hero components for page introductions
- Use alerts for important messages
- Use badges sparingly for highlights
- Maintain consistent button variants throughout site

### 5. Code Examples

- Always specify language for code blocks
- Use descriptive titles for code samples
- Enable copy button for user convenience
- Keep code samples concise

### 6. Common Patterns

**Call-to-Action Section**
```markdown
{{< hero 
    title="Ready to Start?" 
    subtitle="Build your first site in minutes" 
    cta_text="Get Started" 
    cta_link="/docs/getting-started/" 
/>}}
```

**Feature Grid**
```markdown
{{< card title="Fast" content="Lightning-fast build times" variant="primary" />}}
{{< card title="Beautiful" content="13 professional templates" variant="success" />}}
{{< card title="Simple" content="Easy Markdown syntax" variant="info" />}}
```

**Documentation Pattern**
```markdown
# Installation

{{< alert content="Requires Python 3.11+" variant="info" icon="bi bi-info-circle" />}}

{{< tabs id="install" tabs='[
    {"title": "pip", "content": "pip install -r requirements.txt"},
    {"title": "Manual", "content": "Download and extract..."}
]' />}}
```

---

**Author**: Abdulaziz Al-Qadimi  
**Repository**: [MarkSite](https://github.com/Alqudimi/MarkSite)
