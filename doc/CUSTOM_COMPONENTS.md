# Custom Components Guide

Learn how to create your own custom components for MarkSite, extending its functionality beyond the built-in components.

## Table of Contents

- [Overview](#overview)
- [Component Architecture](#component-architecture)
- [Creating a Custom Component](#creating-a-custom-component)
- [Advanced Components](#advanced-components)
- [Component Examples](#component-examples)
- [Best Practices](#best-practices)
- [Troubleshooting](#troubleshooting)

## Overview

MarkSite's component system is extensible. You can create custom components by:
1. Creating an HTML template
2. Registering the component
3. Using it in your Markdown files

### Prerequisites

Basic knowledge of:
- HTML/CSS
- Jinja2 templating
- Python (for registration)

## Component Architecture

### How Components Work

1. **Markdown**: You use shortcode syntax `{{< component />}}`
2. **Parser**: Shortcode parser extracts component and parameters
3. **Template**: Jinja2 renders HTML template with parameters
4. **Output**: HTML is inserted into final page

### Component Structure

```
generator/
├── components/          # Component HTML templates
│   ├── button.html
│   ├── card.html
│   └── your-component.html  ← Your custom component
└── shortcode_parser.py  # Component registry
```

## Creating a Custom Component

### Step 1: Create Template File

Create a new file in `generator/components/`:

**Example**: `generator/components/callout.html`

```html
<div class="callout callout-{{ variant|default('info') }}">
  {% if icon %}
  <i class="{{ icon }}"></i>
  {% endif %}
  <div class="callout-content">
    {% if title %}
    <h4 class="callout-title">{{ title }}</h4>
    {% endif %}
    <p class="callout-text">{{ content }}</p>
  </div>
</div>
```

### Step 2: Add CSS Styling

Add styles in `generator/static/css/styles.css`:

```css
.callout {
  padding: 1.5rem;
  margin: 1.5rem 0;
  border-left: 4px solid;
  border-radius: 4px;
  background: #f8f9fa;
}

.callout-info {
  border-color: #0dcaf0;
  background: #cff4fc;
}

.callout-warning {
  border-color: #ffc107;
  background: #fff3cd;
}

.callout-success {
  border-color: #198754;
  background: #d1e7dd;
}

.callout-danger {
  border-color: #dc3545;
  background: #f8d7da;
}

.callout-title {
  margin: 0 0 0.5rem 0;
  font-weight: 600;
}

.callout-text {
  margin: 0;
}

.callout i {
  margin-right: 0.5rem;
  font-size: 1.2rem;
}
```

### Step 3: Register Component

Edit `generator/shortcode_parser.py` and add to the `components` dictionary:

```python
components = {
    # ... existing components ...
    
    'callout': {
        'template': 'callout.html',
        'description': 'Highlighted callout box with optional icon and title',
        'params': {
            'content': 'Callout message content (required)',
            'variant': 'Style variant: info, warning, success, danger (default: info)',
            'title': 'Optional callout title',
            'icon': 'Optional Bootstrap icon class'
        },
        'example': '{{< callout content="Important information" variant="info" title="Note" icon="bi bi-info-circle" />}}'
    }
}
```

### Step 4: Use Your Component

In your Markdown files:

```markdown
{{< callout content="This is an important note!" variant="info" />}}

{{< callout 
    title="Pro Tip" 
    content="Always backup your data!" 
    variant="success" 
    icon="bi bi-lightbulb" 
/>}}
```

### Step 5: Build and Test

```bash
python build.py
python -m http.server -d site 8000
```

Visit your site and verify the component renders correctly.

## Advanced Components

### Component with Nested Content

For components that need rich content, you can use HTML in the content parameter:

**Template**: `generator/components/infobox.html`

```html
<div class="info-box info-box-{{ style|default('default') }}">
  <div class="info-box-header">
    {% if icon %}
    <i class="{{ icon }}"></i>
    {% endif %}
    <h3>{{ title }}</h3>
  </div>
  <div class="info-box-body">
    {{ content|safe }}
  </div>
  {% if footer %}
  <div class="info-box-footer">
    {{ footer }}
  </div>
  {% endif %}
</div>
```

**Usage**:
```markdown
{{< infobox 
    title="Rich Content Box" 
    content="<p>This supports <strong>HTML</strong>!</p><ul><li>Item 1</li><li>Item 2</li></ul>" 
    icon="bi bi-book" 
/>}}
```

### Component with Multiple Variations

**Template**: `generator/components/timeline.html`

```html
<div class="timeline">
  {% for item in items %}
  <div class="timeline-item">
    <div class="timeline-marker"></div>
    <div class="timeline-content">
      <h4>{{ item.title }}</h4>
      <p class="timeline-date">{{ item.date }}</p>
      <p>{{ item.description }}</p>
    </div>
  </div>
  {% endfor %}
</div>
```

**Note**: For complex data structures, you might need to modify the parser to handle JSON arrays.

### Conditional Rendering

Use Jinja2 conditionals for flexible components:

```html
<div class="feature-card {{ 'featured' if featured else '' }}">
  {% if image %}
  <img src="{{ image }}" alt="{{ title }}">
  {% endif %}
  
  <h3>{{ title }}</h3>
  <p>{{ description }}</p>
  
  {% if link %}
  <a href="{{ link }}" class="btn btn-primary">{{ link_text|default('Learn More') }}</a>
  {% endif %}
  
  {% if badge %}
  <span class="badge bg-{{ badge_variant|default('primary') }}">{{ badge }}</span>
  {% endif %}
</div>
```

## Component Examples

### Example 1: Progress Bar

**Template**: `generator/components/progress.html`

```html
<div class="progress-container">
  {% if label %}
  <label class="progress-label">{{ label }}</label>
  {% endif %}
  <div class="progress">
    <div class="progress-bar bg-{{ variant|default('primary') }}" 
         role="progressbar" 
         style="width: {{ percentage|default(0) }}%"
         aria-valuenow="{{ percentage|default(0) }}" 
         aria-valuemin="0" 
         aria-valuemax="100">
      {{ percentage|default(0) }}%
    </div>
  </div>
</div>
```

**CSS**:
```css
.progress-container {
  margin: 1rem 0;
}

.progress-label {
  display: block;
  margin-bottom: 0.5rem;
  font-weight: 600;
}
```

**Registration**:
```python
'progress': {
    'template': 'progress.html',
    'description': 'Progress bar component',
    'params': {
        'percentage': 'Progress percentage (0-100)',
        'label': 'Optional label text',
        'variant': 'Color variant (default: primary)'
    },
    'example': '{{< progress percentage="75" label="Installation" variant="success" />}}'
}
```

**Usage**:
```markdown
{{< progress percentage="75" label="Project Completion" variant="success" />}}
{{< progress percentage="45" label="Loading..." variant="info" />}}
```

### Example 2: Testimonial

**Template**: `generator/components/testimonial.html`

```html
<div class="testimonial">
  <div class="testimonial-content">
    <i class="bi bi-quote quote-icon"></i>
    <p class="testimonial-text">{{ quote }}</p>
  </div>
  <div class="testimonial-author">
    {% if image %}
    <img src="{{ image }}" alt="{{ name }}" class="testimonial-image">
    {% endif %}
    <div class="testimonial-info">
      <strong>{{ name }}</strong>
      {% if title %}
      <span class="testimonial-title">{{ title }}</span>
      {% endif %}
    </div>
  </div>
</div>
```

**CSS**:
```css
.testimonial {
  background: #f8f9fa;
  padding: 2rem;
  border-radius: 8px;
  margin: 2rem 0;
}

.quote-icon {
  font-size: 2rem;
  color: #0d6efd;
  opacity: 0.3;
}

.testimonial-text {
  font-size: 1.1rem;
  font-style: italic;
  margin: 1rem 0;
}

.testimonial-author {
  display: flex;
  align-items: center;
  margin-top: 1.5rem;
}

.testimonial-image {
  width: 60px;
  height: 60px;
  border-radius: 50%;
  margin-right: 1rem;
}

.testimonial-info {
  display: flex;
  flex-direction: column;
}

.testimonial-title {
  color: #6c757d;
  font-size: 0.9rem;
}
```

**Usage**:
```markdown
{{< testimonial 
    quote="MarkSite made building our documentation site incredibly easy!" 
    name="Sarah Johnson" 
    title="CTO, TechCorp"
    image="/static/images/sarah.jpg"
/>}}
```

### Example 3: Feature Grid

**Template**: `generator/components/feature.html`

```html
<div class="feature-item">
  <div class="feature-icon">
    <i class="{{ icon }}"></i>
  </div>
  <h3 class="feature-title">{{ title }}</h3>
  <p class="feature-description">{{ description }}</p>
</div>
```

**CSS**:
```css
.feature-item {
  text-align: center;
  padding: 2rem;
}

.feature-icon {
  width: 80px;
  height: 80px;
  margin: 0 auto 1rem;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
}

.feature-icon i {
  font-size: 2rem;
  color: white;
}

.feature-title {
  margin: 1rem 0 0.5rem;
  font-size: 1.5rem;
}

.feature-description {
  color: #6c757d;
}
```

**Usage**:
```markdown
<div class="row">
  <div class="col-md-4">
    {{< feature icon="bi bi-lightning-fill" title="Fast" description="Lightning-fast build times" />}}
  </div>
  <div class="col-md-4">
    {{< feature icon="bi bi-palette-fill" title="Beautiful" description="13 stunning templates" />}}
  </div>
  <div class="col-md-4">
    {{< feature icon="bi bi-code-square" title="Simple" description="Easy Markdown syntax" />}}
  </div>
</div>
```

## Best Practices

### 1. Naming Conventions

- Use lowercase, hyphenated names: `my-component`, not `MyComponent`
- Be descriptive: `testimonial`, not `tc`
- Avoid conflicts with built-in components

### 2. Template Design

- Use semantic HTML
- Include ARIA attributes for accessibility
- Support optional parameters with Jinja2 defaults
- Use Bootstrap classes when possible

### 3. Parameter Handling

```html
<!-- Good: Default values -->
<div class="component {{ variant|default('primary') }}">

<!-- Good: Optional parameters -->
{% if icon %}
<i class="{{ icon }}"></i>
{% endif %}

<!-- Good: Required check -->
{% if not title %}
<p class="error">Title is required</p>
{% else %}
<h3>{{ title }}</h3>
{% endif %}
```

### 4. CSS Organization

- Use component-specific class names
- Avoid global style conflicts
- Support both light and dark themes
- Make components responsive

### 5. Documentation

Always document your components:
```python
'mycomponent': {
    'template': 'mycomponent.html',
    'description': 'Clear description of what it does',
    'params': {
        'param1': 'Description and type',
        'param2': 'Description with default (default: value)',
    },
    'example': '{{< mycomponent param1="value" />}}'
}
```

### 6. Testing

Test your components:
- Different parameter combinations
- With and without optional parameters
- In light and dark modes
- On mobile and desktop
- With different templates

## Troubleshooting

### Component Not Rendering

**Problem**: Component shows as raw shortcode

**Solutions**:
1. Check component is registered in `shortcode_parser.py`
2. Verify template file exists in `generator/components/`
3. Ensure syntax is correct: `{{< component />}}`
4. Rebuild site: `python build.py`

### Styling Not Applied

**Problem**: Component renders but looks wrong

**Solutions**:
1. Check CSS is in `generator/static/css/styles.css`
2. Verify CSS selectors match HTML classes
3. Clear browser cache
4. Check browser console for CSS errors

### Parameters Not Working

**Problem**: Parameters don't affect output

**Solutions**:
1. Check Jinja2 syntax: `{{ parameter }}` not `{ parameter }`
2. Verify parameter names match registration
3. Use `|default()` for optional parameters
4. Check for typos in parameter names

### Template Errors

**Problem**: Build fails with Jinja2 error

**Solutions**:
1. Check Jinja2 syntax (matching `{% if %}`/`{% endif %}`)
2. Verify all variables are defined or have defaults
3. Check for unclosed tags
4. Review build error messages carefully

## Advanced Topics

### Custom JavaScript

For interactive components, add JavaScript:

**In your template**:
```html
<div class="counter" id="counter-{{ id }}">
  <button class="counter-btn" onclick="increment('{{ id }}')">+</button>
  <span class="counter-value">0</span>
  <button class="counter-btn" onclick="decrement('{{ id }}')">-</button>
</div>
```

**In `generator/static/js/components.js`**:
```javascript
function increment(id) {
  const counter = document.querySelector(`#counter-${id} .counter-value`);
  counter.textContent = parseInt(counter.textContent) + 1;
}

function decrement(id) {
  const counter = document.querySelector(`#counter-${id} .counter-value`);
  counter.textContent = Math.max(0, parseInt(counter.textContent) - 1);
}
```

### Component Composition

Components can include other components:

```html
<div class="super-card">
  {{ button_html|safe }}
  <div class="super-card-content">
    {{ content }}
  </div>
</div>
```

Though this requires parser modifications for full support.

## Resources

- [Jinja2 Documentation](https://jinja.palletsprojects.com/)
- [Bootstrap 5 Documentation](https://getbootstrap.com/)
- [Bootstrap Icons](https://icons.getbootstrap.com/)
- [MDN Web Docs](https://developer.mozilla.org/)

---

**Author**: Abdulaziz Al-Qadimi  
**Email**: eng7mi@gmail.com  
**Repository**: [MarkSite](https://github.com/Alqudimi/MarkSite)
