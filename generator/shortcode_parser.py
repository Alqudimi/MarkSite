import re
from typing import Dict, Any, List


class ShortcodeParser:
    def __init__(self, jinja_env):
        self.jinja_env = jinja_env
        
        self.components = {
            'button': {
                'template': 'button.html',
                'description': 'Renders a styled button with various variants',
                'params': {
                    'text': 'Button text',
                    'href': 'Link URL (optional)',
                    'variant': 'Button variant: primary, secondary, success, danger, warning, info, light, dark, outline-primary, etc.',
                    'size': 'Button size: sm, md, lg (default: md)',
                    'icon': 'Icon class (optional)',
                    'disabled': 'Disable button (optional)'
                },
                'example': '{{< button text="Get Started" href="/docs" variant="primary" size="lg" />}}'
            },
            'card': {
                'template': 'card.html',
                'description': 'Renders a card component with optional header, body, and footer',
                'params': {
                    'title': 'Card title',
                    'content': 'Card body content',
                    'footer': 'Card footer text (optional)',
                    'variant': 'Card variant: primary, secondary, success, danger, warning, info (optional)',
                    'image': 'Card image URL (optional)'
                },
                'example': '{{< card title="Welcome" content="This is a card component" variant="primary" />}}'
            },
            'alert': {
                'template': 'alert.html',
                'description': 'Renders an alert message box',
                'params': {
                    'content': 'Alert message content',
                    'variant': 'Alert type: primary, secondary, success, danger, warning, info, light, dark',
                    'dismissible': 'Make alert dismissible (optional)',
                    'icon': 'Icon class (optional)'
                },
                'example': '{{< alert content="Important information!" variant="info" dismissible="true" />}}'
            },
            'code': {
                'template': 'code-sample.html',
                'description': 'Renders a code block with syntax highlighting and copy button',
                'params': {
                    'content': 'Code content',
                    'language': 'Programming language for syntax highlighting',
                    'title': 'Code block title (optional)',
                    'copy': 'Show copy button (default: true)'
                },
                'example': '{{< code language="python" title="Hello World" content="print(\'Hello, World!\')" />}}'
            },
            'hero': {
                'template': 'hero.html',
                'description': 'Renders a hero section with title, subtitle, and call-to-action',
                'params': {
                    'title': 'Hero title',
                    'subtitle': 'Hero subtitle',
                    'cta_text': 'Call-to-action button text (optional)',
                    'cta_link': 'Call-to-action button link (optional)',
                    'image': 'Background image URL (optional)',
                    'variant': 'Hero variant: primary, secondary, dark, light (default: primary)'
                },
                'example': '{{< hero title="Welcome" subtitle="Build amazing sites" cta_text="Get Started" cta_link="/docs" />}}'
            },
            'tabs': {
                'template': 'tabs.html',
                'description': 'Renders tabbed content sections',
                'params': {
                    'tabs': 'JSON array of tab objects with title and content',
                    'id': 'Unique ID for the tabs component'
                },
                'example': '{{< tabs id="example" tabs=\'[{"title":"Tab 1","content":"Content 1"},{"title":"Tab 2","content":"Content 2"}]\' />}}'
            },
            'collapsible': {
                'template': 'collapsible.html',
                'description': 'Renders a collapsible accordion component',
                'params': {
                    'title': 'Collapsible section title',
                    'content': 'Collapsible content',
                    'open': 'Start expanded (optional)',
                    'variant': 'Variant style (optional)'
                },
                'example': '{{< collapsible title="Click to expand" content="Hidden content here" />}}'
            },
            'badge': {
                'template': 'badge.html',
                'description': 'Renders a small badge or label',
                'params': {
                    'text': 'Badge text',
                    'variant': 'Badge variant: primary, secondary, success, danger, warning, info, light, dark'
                },
                'example': '{{< badge text="New" variant="success" />}}'
            }
        }
        
        self.shortcode_pattern = re.compile(
            r'\{\{<\s*(\w+)\s*([^>]*?)\s*/?\s*>\}\}',
            re.DOTALL
        )
    
    def parse_params(self, param_string: str) -> Dict[str, Any]:
        params = {}
        
        param_pattern = re.compile(r'(\w+)=(["\'])([^\2]*?)\2')
        
        for match in param_pattern.finditer(param_string):
            key = match.group(1)
            value = match.group(3)
            
            if value.lower() == 'true':
                params[key] = True
            elif value.lower() == 'false':
                params[key] = False
            else:
                params[key] = value
        
        return params
    
    def render_component(self, component_name: str, params: Dict[str, Any]) -> str:
        if component_name not in self.components:
            return f'[Unknown component: {component_name}]'
        
        component_info = self.components[component_name]
        template_name = component_info['template']
        
        try:
            template = self.jinja_env.get_template(template_name)
            return template.render(**params)
        except Exception as e:
            return f'[Error rendering {component_name}: {str(e)}]'
    
    def parse(self, content: str) -> str:
        def replace_shortcode(match):
            component_name = match.group(1)
            param_string = match.group(2)
            params = self.parse_params(param_string)
            return self.render_component(component_name, params)
        
        return self.shortcode_pattern.sub(replace_shortcode, content)
    
    def get_component_docs(self) -> List[Dict[str, Any]]:
        docs = []
        for name, info in self.components.items():
            docs.append({
                'name': name,
                'description': info['description'],
                'params': info['params'],
                'example': info['example'],
                'template': info['template']
            })
        return docs
