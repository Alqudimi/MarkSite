#!/bin/bash

# ============================================================================
# MarkSite Dashboard Server Launcher
# ============================================================================

set -e

PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$PROJECT_DIR"

echo "╔════════════════════════════════════════════════════════════════╗"
echo "║         MarkSite Dashboard - Server Launcher                   ║"
echo "╚════════════════════════════════════════════════════════════════╝"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ خطأ: Python 3 غير مثبت"
    exit 1
fi

# Check if requirements are installed
echo "📦 التحقق من المتطلبات..."
if ! python3 -c "import fastapi" 2>/dev/null; then
    echo "📥 تثبيت المتطلبات..."
    pip3 install -r server/requirements.txt
fi

echo ""
echo "✓ المتطلبات جاهزة"
echo ""
echo "🚀 بدء تشغيل الخادم..."
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "📍 الخادم يعمل على: http://localhost:8000"
echo "📊 لوحة التحكم: http://localhost:8000/"
echo "📚 توثيق API: http://localhost:8000/docs"
echo ""
echo "اضغط Ctrl+C لإيقاف الخادم"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# Run the server
python3 server/app.py
