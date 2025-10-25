#!/usr/bin/env python3
import argparse
import sys
from pathlib import Path
from generator import StaticSiteGenerator


def main():
    parser = argparse.ArgumentParser(
        description='Static Site Generator - Convert Markdown to static HTML',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
  python build.py
  python build.py --input content --output site
  python build.py --config myconfig.yaml
        '''
    )
    
    parser.add_argument(
        '--input', '-i',
        default='content',
        help='Input directory containing Markdown files (default: content)'
    )
    
    parser.add_argument(
        '--output', '-o',
        default='site',
        help='Output directory for generated static site (default: site)'
    )
    
    parser.add_argument(
        '--config', '-c',
        default='config.yaml',
        help='Configuration file path (default: config.yaml)'
    )
    
    args = parser.parse_args()
    
    input_path = Path(args.input)
    if not input_path.exists():
        print(f"Error: Input directory '{args.input}' does not exist")
        sys.exit(1)
    
    try:
        generator = StaticSiteGenerator(
            input_dir=args.input,
            output_dir=args.output,
            config_file=args.config
        )
        
        generator.build()
        
        print("\n" + "="*50)
        print("Build completed successfully!")
        print("="*50)
        print(f"\nYour static site is ready in: {args.output}/")
        print("\nNext steps:")
        print(f"  1. Open {args.output}/index.html in your browser")
        print(f"  2. Deploy the '{args.output}' directory to:")
        print("     - GitHub Pages")
        print("     - Netlify")
        print("     - Vercel")
        print("     - Any static hosting service")
        
    except Exception as e:
        print(f"Error during build: {str(e)}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
