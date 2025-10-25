import os
import re
import json
import yaml
import markdown
import frontmatter
from pathlib import Path
from datetime import datetime
from jinja2 import Environment, FileSystemLoader, select_autoescape
from bs4 import BeautifulSoup
from pygments.formatters import HtmlFormatter
from .shortcode_parser import ShortcodeParser


class StaticSiteGenerator:
    def __init__(self, input_dir='content', output_dir='site', config_file='config.yaml'):
        self.input_dir = Path(input_dir)
        self.output_dir = Path(output_dir)
        self.config = self.load_config(config_file)
        
        self.jinja_env = Environment(
            loader=FileSystemLoader(['generator/templates', 'generator/components']),
            autoescape=select_autoescape(['html', 'xml'])
        )
        
        self.shortcode_parser = ShortcodeParser(self.jinja_env)
        
        self.md = markdown.Markdown(extensions=[
            'extra',
            'codehilite',
            'toc',
            'tables',
            'fenced_code',
            'attr_list'
        ], extension_configs={
            'codehilite': {
                'css_class': 'highlight',
                'linenums': False,
                'guess_lang': False
            },
            'toc': {
                'permalink': True,
                'toc_depth': '2-4'
            }
        })
        
        self.pages = []
        self.search_index = []
        
    def load_config(self, config_file):
        if os.path.exists(config_file):
            with open(config_file, 'r', encoding='utf-8') as f:
                return yaml.safe_load(f)
        return self.get_default_config()
    
    def get_default_config(self):
        return {
            'site_name': 'My Static Site',
            'site_description': 'A modern static site built with Flask',
            'site_url': 'https://example.com',
            'theme': {
                'default_mode': 'light',
                'primary_color': '#0d6efd',
                'secondary_color': '#6c757d'
            }
        }
    
    def scan_markdown_files(self):
        md_files = []
        for md_file in self.input_dir.rglob('*.md'):
            if md_file.is_file():
                md_files.append(md_file)
        return sorted(md_files)
    
    def parse_markdown_file(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            post = frontmatter.load(f)
        
        content = post.content
        
        content = self.shortcode_parser.parse(content)
        
        self.md.reset()
        html_content = self.md.convert(content)
        toc = getattr(self.md, 'toc', '')
        
        metadata = post.metadata
        metadata.setdefault('title', file_path.stem.replace('-', ' ').replace('_', ' ').title())
        metadata.setdefault('date', datetime.now().strftime('%Y-%m-%d'))
        metadata.setdefault('description', '')
        
        return {
            'content': html_content,
            'toc': toc,
            'metadata': metadata,
            'source_file': file_path
        }
    
    def get_output_path(self, input_file):
        rel_path = input_file.relative_to(self.input_dir)
        
        if input_file.stem == 'index':
            output_path = self.output_dir / rel_path.parent / 'index.html'
        else:
            output_path = self.output_dir / rel_path.parent / input_file.stem / 'index.html'
        
        return output_path
    
    def get_url_path(self, output_path):
        rel_path = output_path.relative_to(self.output_dir)
        url_path = '/' + str(rel_path.parent).replace('\\', '/')
        if url_path.endswith('/'):
            return url_path
        return url_path + '/'
    
    def generate_page(self, page_data):
        template = self.jinja_env.get_template('page.html')
        
        html = template.render(
            page=page_data,
            config=self.config,
            site_name=self.config['site_name'],
            site_description=self.config['site_description']
        )
        
        output_path = page_data['output_path']
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html)
    
    def generate_index_page(self):
        template = self.jinja_env.get_template('index.html')
        
        sorted_pages = sorted(
            self.pages,
            key=lambda x: x['metadata'].get('date', ''),
            reverse=True
        )
        
        html = template.render(
            pages=sorted_pages,
            config=self.config,
            site_name=self.config['site_name'],
            site_description=self.config['site_description']
        )
        
        index_path = self.output_dir / 'index.html'
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(html)
    
    def generate_pattern_library(self):
        template = self.jinja_env.get_template('pattern-library.html')
        
        components = self.shortcode_parser.get_component_docs()
        
        html = template.render(
            components=components,
            config=self.config,
            site_name=self.config['site_name']
        )
        
        pattern_path = self.output_dir / 'pattern-library' / 'index.html'
        pattern_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(pattern_path, 'w', encoding='utf-8') as f:
            f.write(html)
    
    def generate_search_index(self):
        search_data = []
        for page in self.pages:
            soup = BeautifulSoup(page['content'], 'html.parser')
            text_content = soup.get_text()
            
            search_data.append({
                'title': page['metadata']['title'],
                'url': page['url'],
                'content': text_content[:500],
                'description': page['metadata'].get('description', '')
            })
        
        search_path = self.output_dir / 'static' / 'js' / 'search-index.json'
        search_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(search_path, 'w', encoding='utf-8') as f:
            json.dump(search_data, f, ensure_ascii=False, indent=2)
    
    def generate_sitemap(self):
        sitemap_lines = ['<?xml version="1.0" encoding="UTF-8"?>']
        sitemap_lines.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')
        
        base_url = self.config.get('site_url', 'https://example.com').rstrip('/')
        
        for page in self.pages:
            sitemap_lines.append('  <url>')
            sitemap_lines.append(f'    <loc>{base_url}{page["url"]}</loc>')
            sitemap_lines.append(f'    <lastmod>{page["metadata"].get("date", datetime.now().strftime("%Y-%m-%d"))}</lastmod>')
            sitemap_lines.append('  </url>')
        
        sitemap_lines.append('</urlset>')
        
        sitemap_path = self.output_dir / 'sitemap.xml'
        with open(sitemap_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(sitemap_lines))
    
    def copy_static_files(self):
        import shutil
        
        static_src = Path('generator/static')
        static_dest = self.output_dir / 'static'
        
        if static_src.exists():
            if static_dest.exists():
                shutil.rmtree(static_dest)
            shutil.copytree(static_src, static_dest)
    
    def generate_pygments_css(self):
        css_path = self.output_dir / 'static' / 'css' / 'pygments.css'
        css_path.parent.mkdir(parents=True, exist_ok=True)
        
        formatter = HtmlFormatter(style='monokai')
        with open(css_path, 'w', encoding='utf-8') as f:
            f.write(formatter.get_style_defs('.highlight'))
    
    def build(self):
        print(f"Building site from {self.input_dir} to {self.output_dir}...")
        
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        md_files = self.scan_markdown_files()
        print(f"Found {len(md_files)} Markdown files")
        
        for md_file in md_files:
            print(f"Processing: {md_file}")
            page_data = self.parse_markdown_file(md_file)
            page_data['output_path'] = self.get_output_path(md_file)
            page_data['url'] = self.get_url_path(page_data['output_path'])
            
            self.pages.append(page_data)
            self.generate_page(page_data)
        
        print("Generating index page...")
        self.generate_index_page()
        
        print("Generating pattern library...")
        self.generate_pattern_library()
        
        print("Copying static files...")
        self.copy_static_files()
        
        print("Generating Pygments CSS...")
        self.generate_pygments_css()
        
        print("Generating search index...")
        self.generate_search_index()
        
        print("Generating sitemap...")
        self.generate_sitemap()
        
        print(f"\n✓ Site generated successfully in {self.output_dir}/")
        print(f"  Total pages: {len(self.pages)}")
        print(f"  Open {self.output_dir}/index.html to view your site")
