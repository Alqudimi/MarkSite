#!/usr/bin/env python3
"""
MarkSite Dashboard Server
A FastAPI-based server for managing MarkSite static site generation
"""

import os
import json
import yaml
import shutil
import subprocess
from pathlib import Path
from datetime import datetime
from fastapi import FastAPI, HTTPException, File, UploadFile, Form
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import sys

# Add MarkSite generator to path
sys.path.insert(0, str(Path(__file__).parent.parent / "MarkSite"))
from generator import StaticSiteGenerator

# Initialize FastAPI app
app = FastAPI(
    title="MarkSite Dashboard",
    description="API for managing MarkSite static site generation",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configuration
PROJECT_ROOT = Path(__file__).parent.parent
MARKSITE_DIR = PROJECT_ROOT / "MarkSite"
CONTENT_DIR = PROJECT_ROOT / "MarkSite" / "content"
OUTPUT_DIR = PROJECT_ROOT / "MarkSite" / "site"
CONFIG_FILE = PROJECT_ROOT / "MarkSite" / "config.yaml"

# Create content directory if it doesn't exist
CONTENT_DIR.mkdir(parents=True, exist_ok=True)

# Available templates
AVAILABLE_TEMPLATES = [
    'default', 'minimalist', 'techblog', 'documentation', 'portfolio',
    'magazine', 'landing', 'creative', 'personalblog', 'inkwell',
    'futuristic', 'monochrome', 'oasis', 'retrowave', 'serenity',
    'dark-nebula', 'vibrant-grid', 'eco-green', 'luxury-gold',
    'cyberpunk', 'brutalist', 'oceanic', 'autumn-whisper', 'neon-night'
]


def load_config():
    """Load configuration from YAML file"""
    if CONFIG_FILE.exists():
        with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
    return get_default_config()


def get_default_config():
    """Get default configuration"""
    return {
        'site_name': 'My Static Site',
        'site_description': 'A modern static site built with MarkSite',
        'site_url': 'https://example.com',
        'template': 'default',
        'theme': {
            'default_mode': 'light',
            'primary_color': '#0d6efd',
            'secondary_color': '#6c757d'
        },
        'author': {
            'name': 'Your Name',
            'email': 'your.email@example.com'
        }
    }


def save_config(config):
    """Save configuration to YAML file"""
    with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
        yaml.dump(config, f, default_flow_style=False, allow_unicode=True)


# ============================================================================
# API Endpoints - Configuration Management
# ============================================================================

@app.get("/api/config")
async def get_config():
    """Get current site configuration"""
    try:
        config = load_config()
        return JSONResponse({"success": True, "data": config})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/api/config")
async def update_config(config: dict):
    """Update site configuration"""
    try:
        save_config(config)
        return JSONResponse({"success": True, "message": "Configuration updated successfully"})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/templates")
async def get_templates():
    """Get list of available templates"""
    return JSONResponse({
        "success": True,
        "templates": AVAILABLE_TEMPLATES
    })


# ============================================================================
# API Endpoints - Content Management
# ============================================================================

@app.get("/api/content")
async def list_content():
    """List all markdown files in content directory"""
    try:
        files = []
        if CONTENT_DIR.exists():
            for md_file in CONTENT_DIR.rglob('*.md'):
                rel_path = md_file.relative_to(CONTENT_DIR)
                files.append({
                    'name': md_file.stem,
                    'path': str(rel_path),
                    'full_path': str(md_file),
                    'modified': datetime.fromtimestamp(md_file.stat().st_mtime).isoformat()
                })
        return JSONResponse({"success": True, "files": sorted(files, key=lambda x: x['modified'], reverse=True)})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/content/{file_path:path}")
async def get_content(file_path: str):
    """Get content of a specific markdown file"""
    try:
        full_path = CONTENT_DIR / file_path
        if not full_path.exists() or not full_path.suffix == '.md':
            raise HTTPException(status_code=404, detail="File not found")
        
        with open(full_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        return JSONResponse({
            "success": True,
            "path": file_path,
            "content": content
        })
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/api/content/{file_path:path}")
async def save_content(file_path: str, content: str = Form(...)):
    """Save or update a markdown file"""
    try:
        full_path = CONTENT_DIR / file_path
        full_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(full_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return JSONResponse({
            "success": True,
            "message": f"File '{file_path}' saved successfully"
        })
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/api/content/upload")
async def upload_content(file: UploadFile = File(...)):
    """Upload a markdown file"""
    try:
        file_path = CONTENT_DIR / file.filename
        file_path.parent.mkdir(parents=True, exist_ok=True)
        
        content = await file.read()
        with open(file_path, 'wb') as f:
            f.write(content)
        
        return JSONResponse({
            "success": True,
            "message": f"File '{file.filename}' uploaded successfully",
            "filename": file.filename
        })
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.delete("/api/content/{file_path:path}")
async def delete_content(file_path: str):
    """Delete a markdown file"""
    try:
        full_path = CONTENT_DIR / file_path
        if not full_path.exists():
            raise HTTPException(status_code=404, detail="File not found")
        
        full_path.unlink()
        return JSONResponse({
            "success": True,
            "message": f"File '{file_path}' deleted successfully"
        })
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# ============================================================================
# API Endpoints - Build Management
# ============================================================================

@app.post("/api/build")
async def build_site(template: str = None):
    """Build the static site"""
    try:
        config = load_config()
        
        if template:
            if template not in AVAILABLE_TEMPLATES:
                raise HTTPException(status_code=400, detail=f"Invalid template: {template}")
            selected_template = template
        else:
            selected_template = config.get('template', 'default')
        
        # Create generator and build
        generator = StaticSiteGenerator(
            input_dir=str(CONTENT_DIR),
            output_dir=str(OUTPUT_DIR),
            config_file=str(CONFIG_FILE),
            template=selected_template
        )
        
        generator.build()
        
        return JSONResponse({
            "success": True,
            "message": "Site built successfully",
            "output_dir": str(OUTPUT_DIR),
            "pages_count": len(generator.pages)
        })
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/build/status")
async def build_status():
    """Get build status"""
    try:
        if OUTPUT_DIR.exists():
            files_count = len(list(OUTPUT_DIR.rglob('*.html')))
            return JSONResponse({
                "success": True,
                "built": True,
                "output_dir": str(OUTPUT_DIR),
                "files_count": files_count
            })
        else:
            return JSONResponse({
                "success": True,
                "built": False
            })
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/build/preview")
async def get_build_preview():
    """Get preview of the built site"""
    try:
        index_file = OUTPUT_DIR / "index.html"
        if not index_file.exists():
            raise HTTPException(status_code=404, detail="Site not built yet")
        
        return FileResponse(index_file, media_type="text/html")
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# ============================================================================
# API Endpoints - File Management
# ============================================================================

@app.get("/api/files")
async def list_files():
    """List all files in the project"""
    try:
        files = {
            'content': [],
            'output': [],
            'config': str(CONFIG_FILE) if CONFIG_FILE.exists() else None
        }
        
        if CONTENT_DIR.exists():
            for f in CONTENT_DIR.rglob('*'):
                if f.is_file():
                    files['content'].append(str(f.relative_to(CONTENT_DIR)))
        
        if OUTPUT_DIR.exists():
            for f in OUTPUT_DIR.rglob('*'):
                if f.is_file():
                    files['output'].append(str(f.relative_to(OUTPUT_DIR)))
        
        return JSONResponse({"success": True, "files": files})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/stats")
async def get_stats():
    """Get project statistics"""
    try:
        content_files = len(list(CONTENT_DIR.rglob('*.md'))) if CONTENT_DIR.exists() else 0
        output_files = len(list(OUTPUT_DIR.rglob('*.html'))) if OUTPUT_DIR.exists() else 0
        
        config = load_config()
        
        return JSONResponse({
            "success": True,
            "stats": {
                "content_files": content_files,
                "output_files": output_files,
                "template": config.get('template', 'default'),
                "site_name": config.get('site_name', 'Untitled'),
                "content_dir": str(CONTENT_DIR),
                "output_dir": str(OUTPUT_DIR)
            }
        })
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# ============================================================================
# Health Check
# ============================================================================

@app.get("/api/health")
async def health_check():
    """Health check endpoint"""
    return JSONResponse({
        "success": True,
        "status": "healthy",
        "timestamp": datetime.now().isoformat()
    })


# ============================================================================
# Serve Static Files
# ============================================================================

# Serve the dashboard HTML
@app.get("/")
async def serve_dashboard():
    """Serve the main dashboard"""
    dashboard_path = Path(__file__).parent / "static" / "html" / "index.html"
    if dashboard_path.exists():
        return FileResponse(dashboard_path, media_type="text/html")
    return JSONResponse({"message": "Dashboard not found"})


# Mount static files
static_dir = Path(__file__).parent / "static"
if static_dir.exists():
    app.mount("/static", StaticFiles(directory=str(static_dir)), name="static")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
