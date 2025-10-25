---
title: Component Demonstration
description: A comprehensive showcase of all available components and their variants
date: 2025-01-15
author: Documentation Team
tags: [components, examples, demo]
---

# Component Demonstration

This page demonstrates all available components with various configurations.

## Table of Contents

The table of contents is automatically generated from your headings!

## Button Components

### Basic Buttons

{{< button text="Click Me" variant="primary" />}}
{{< button text="Secondary" variant="secondary" />}}
{{< button text="Success" variant="success" />}}
{{< button text="Danger" variant="danger" />}}

### Button Sizes

{{< button text="Small" variant="primary" size="sm" />}}
{{< button text="Medium" variant="primary" size="md" />}}
{{< button text="Large" variant="primary" size="lg" />}}

### Buttons with Icons

{{< button text="Download" variant="success" icon="bi bi-download" />}}
{{< button text="Settings" variant="secondary" icon="bi bi-gear" />}}

### Link Buttons

{{< button text="External Link" href="https://github.com" variant="primary" target="_blank" />}}

## Alert Components

{{< alert content="Primary alert - Use for general information" variant="primary" />}}

{{< alert content="Success! Operation completed successfully" variant="success" icon="bi bi-check-circle-fill" />}}

{{< alert content="Warning: Please check your configuration" variant="warning" icon="bi bi-exclamation-triangle-fill" />}}

{{< alert content="Error: Something went wrong" variant="danger" icon="bi bi-x-circle-fill" />}}

{{< alert content="Dismissible alert - Click the X to close" variant="info" dismissible="true" />}}

## Card Components

{{< card title="Simple Card" content="This is a basic card with title and content." />}}

{{< card title="Card with Footer" content="This card has a footer section with additional information." footer="Updated: 2025-01-15" />}}

{{< card title="Primary Card" content="Cards can have different color variants to match your theme." variant="primary" />}}

{{< card title="Success Card" content="Perfect for highlighting positive outcomes and achievements." variant="success" />}}

## Code Sample Component

{{< code language="python" title="Hello World Example" content="def hello_world():
    print('Hello, World!')
    return True

if __name__ == '__main__':
    hello_world()" />}}

{{< code language="javascript" content="const greet = (name) => {
    console.log(`Hello, ${name}!`);
};

greet('World');" />}}

## Collapsible Components

{{< collapsible title="What is a Static Site Generator?" content="A static site generator is a tool that takes source content (like Markdown files) and transforms it into a complete static website consisting of HTML, CSS, and JavaScript files that can be deployed anywhere." />}}

{{< collapsible title="Why use components?" content="Components provide reusable, themeable UI elements that maintain consistency across your site while being easy to use within Markdown content." />}}

{{< collapsible title="Advanced Features" content="Our generator includes syntax highlighting, full-text search, responsive design, theme customization, automatic TOC generation, sitemap creation, and much more!" open="true" />}}

## Badge Components

Status: {{< badge text="Active" variant="success" />}}
Version: {{< badge text="v2.0.1" variant="primary" />}}
Priority: {{< badge text="High" variant="danger" />}}
Type: {{< badge text="Feature" variant="info" />}}

## Hero Component

{{< hero title="Welcome to Our Platform" subtitle="Build, deploy, and scale your static websites with ease" cta_text="Learn More" cta_link="/docs/" variant="primary" />}}

## Tabs Component

{{< tabs id="demo-tabs" tabs='[
    {"title": "Overview", "content": "This is the overview tab with general information about the topic."},
    {"title": "Features", "content": "Here are the key features: Fast performance, Easy to use, Fully customizable, SEO optimized"},
    {"title": "Documentation", "content": "Check out our comprehensive documentation for detailed guides and API references."}
]' />}}

## Markdown Features

### Lists

Unordered list:
- First item
- Second item
- Third item with nested items:
  - Nested item 1
  - Nested item 2

Ordered list:
1. First step
2. Second step
3. Third step

### Blockquote

> "The best way to predict the future is to invent it."
> 
> — Alan Kay

### Tables

| Feature | Description | Status |
|---------|-------------|--------|
| Markdown Support | Full CommonMark compatibility | {{< badge text="✓" variant="success" />}} |
| Components | Shortcode-based system | {{< badge text="✓" variant="success" />}} |
| Themes | Light/Dark mode | {{< badge text="✓" variant="success" />}} |
| Search | Client-side full-text | {{< badge text="✓" variant="success" />}} |

### Code Blocks

Inline code: `const example = true;`

Block code:

```python
class StaticSiteGenerator:
    def __init__(self, config):
        self.config = config
    
    def build(self):
        print("Building site...")
```

---

This is just a sample of what you can do with components. Visit the [Pattern Library](/pattern-library/) for complete documentation!
