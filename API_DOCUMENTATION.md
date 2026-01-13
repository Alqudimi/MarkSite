# MarkSite Dashboard - API Documentation

توثيق شامل لـ API الخاص بـ MarkSite Dashboard

## 📌 معلومات عامة

- **Base URL**: `http://localhost:8000/api`
- **Response Format**: JSON
- **Authentication**: غير مطلوبة حالياً
- **CORS**: مفعل لجميع النطاقات

## 🔍 Response Format

جميع الاستجابات تتبع الصيغة التالية:

```json
{
  "success": true,
  "data": {},
  "message": "Optional message"
}
```

## 📚 Endpoints

### 1. Health Check

#### GET `/api/health`

فحص صحة الخادم

**Response:**
```json
{
  "success": true,
  "status": "healthy",
  "timestamp": "2025-01-13T15:52:46.713921"
}
```

**Example:**
```bash
curl http://localhost:8000/api/health
```

---

### 2. Configuration Management

#### GET `/api/config`

الحصول على إعدادات الموقع الحالية

**Response:**
```json
{
  "success": true,
  "data": {
    "site_name": "My Static Site",
    "site_description": "A modern static site built with MarkSite",
    "site_url": "https://example.com",
    "template": "default",
    "theme": {
      "default_mode": "light",
      "primary_color": "#0d6efd",
      "secondary_color": "#6c757d"
    },
    "author": {
      "name": "Your Name",
      "email": "your.email@example.com"
    }
  }
}
```

**Example:**
```bash
curl http://localhost:8000/api/config
```

---

#### POST `/api/config`

تحديث إعدادات الموقع

**Request Body:**
```json
{
  "site_name": "My New Site",
  "site_description": "Updated description",
  "site_url": "https://mynewsite.com",
  "template": "minimalist",
  "author": {
    "name": "John Doe",
    "email": "john@example.com"
  },
  "theme": {
    "primary_color": "#ff0000",
    "secondary_color": "#00ff00"
  }
}
```

**Response:**
```json
{
  "success": true,
  "message": "Configuration updated successfully"
}
```

**Example:**
```bash
curl -X POST http://localhost:8000/api/config \
  -H "Content-Type: application/json" \
  -d '{
    "site_name": "My New Site",
    "template": "minimalist"
  }'
```

---

#### GET `/api/templates`

الحصول على قائمة القوالب المتاحة

**Response:**
```json
{
  "success": true,
  "templates": [
    "default",
    "minimalist",
    "techblog",
    "documentation",
    "portfolio",
    "magazine",
    "landing",
    "creative",
    "personalblog",
    "inkwell",
    "futuristic",
    "monochrome",
    "oasis",
    "retrowave",
    "serenity",
    "dark-nebula",
    "vibrant-grid",
    "eco-green",
    "luxury-gold",
    "cyberpunk",
    "brutalist",
    "oceanic",
    "autumn-whisper",
    "neon-night"
  ]
}
```

**Example:**
```bash
curl http://localhost:8000/api/templates
```

---

### 3. Content Management

#### GET `/api/content`

الحصول على قائمة جميع ملفات المحتوى

**Response:**
```json
{
  "success": true,
  "files": [
    {
      "name": "index",
      "path": "index.md",
      "full_path": "/path/to/content/index.md",
      "modified": "2025-01-13T15:49:00.000000"
    },
    {
      "name": "about",
      "path": "about.md",
      "full_path": "/path/to/content/about.md",
      "modified": "2025-01-13T14:30:00.000000"
    }
  ]
}
```

**Example:**
```bash
curl http://localhost:8000/api/content
```

---

#### GET `/api/content/{file_path}`

الحصول على محتوى ملف محدد

**Parameters:**
- `file_path` (string): مسار الملف (مثال: `index.md` أو `blog/post1.md`)

**Response:**
```json
{
  "success": true,
  "path": "index.md",
  "content": "---\ntitle: Home\n---\n\n# Welcome"
}
```

**Example:**
```bash
curl http://localhost:8000/api/content/index.md
```

---

#### POST `/api/content/{file_path}`

حفظ أو تحديث ملف محتوى

**Parameters:**
- `file_path` (string): مسار الملف

**Request Body (Form Data):**
- `content` (string): محتوى الملف

**Response:**
```json
{
  "success": true,
  "message": "File 'index.md' saved successfully"
}
```

**Example:**
```bash
curl -X POST http://localhost:8000/api/content/index.md \
  -F "content=---\ntitle: Home\n---\n\n# Welcome to my site"
```

---

#### POST `/api/content/upload`

رفع ملف محتوى جديد

**Request Body (Form Data):**
- `file` (file): ملف Markdown

**Response:**
```json
{
  "success": true,
  "message": "File 'myfile.md' uploaded successfully",
  "filename": "myfile.md"
}
```

**Example:**
```bash
curl -X POST http://localhost:8000/api/content/upload \
  -F "file=@myfile.md"
```

---

#### DELETE `/api/content/{file_path}`

حذف ملف محتوى

**Parameters:**
- `file_path` (string): مسار الملف

**Response:**
```json
{
  "success": true,
  "message": "File 'index.md' deleted successfully"
}
```

**Example:**
```bash
curl -X DELETE http://localhost:8000/api/content/index.md
```

---

### 4. Build Management

#### POST `/api/build`

بناء الموقع الثابت

**Request Body (Optional):**
```json
{
  "template": "minimalist"
}
```

**Response:**
```json
{
  "success": true,
  "message": "Site built successfully",
  "output_dir": "/path/to/site",
  "pages_count": 5
}
```

**Example:**
```bash
curl -X POST http://localhost:8000/api/build

# مع تحديد القالب
curl -X POST http://localhost:8000/api/build \
  -H "Content-Type: application/json" \
  -d '{"template": "minimalist"}'
```

---

#### GET `/api/build/status`

الحصول على حالة البناء الأخيرة

**Response (إذا كان الموقع مبني):**
```json
{
  "success": true,
  "built": true,
  "output_dir": "/path/to/site",
  "files_count": 15
}
```

**Response (إذا لم يكن الموقع مبني):**
```json
{
  "success": true,
  "built": false
}
```

**Example:**
```bash
curl http://localhost:8000/api/build/status
```

---

#### GET `/api/build/preview`

الحصول على معاينة الموقع (ملف HTML)

**Response:** ملف HTML

**Example:**
```bash
curl http://localhost:8000/api/build/preview > preview.html
```

---

### 5. Files and Statistics

#### GET `/api/files`

الحصول على قائمة جميع الملفات في المشروع

**Response:**
```json
{
  "success": true,
  "files": {
    "content": [
      "index.md",
      "about.md",
      "blog/post1.md"
    ],
    "output": [
      "index.html",
      "about/index.html",
      "blog/post1/index.html"
    ],
    "config": "/path/to/config.yaml"
  }
}
```

**Example:**
```bash
curl http://localhost:8000/api/files
```

---

#### GET `/api/stats`

الحصول على إحصائيات المشروع

**Response:**
```json
{
  "success": true,
  "stats": {
    "content_files": 5,
    "output_files": 8,
    "template": "default",
    "site_name": "My Static Site",
    "content_dir": "/path/to/content",
    "output_dir": "/path/to/site"
  }
}
```

**Example:**
```bash
curl http://localhost:8000/api/stats
```

---

## 🔐 Error Handling

### Error Response Format

```json
{
  "detail": "Error message describing what went wrong"
}
```

### Common HTTP Status Codes

| Code | Meaning |
|------|---------|
| 200 | OK - Request successful |
| 400 | Bad Request - Invalid parameters |
| 404 | Not Found - Resource not found |
| 500 | Internal Server Error - Server error |

### Examples

**File Not Found:**
```json
{
  "detail": "File not found"
}
```

**Invalid Template:**
```json
{
  "detail": "Invalid template: nonexistent"
}
```

---

## 💡 Usage Examples

### مثال 1: إنشاء موقع جديد

```bash
# 1. تحديث الإعدادات
curl -X POST http://localhost:8000/api/config \
  -H "Content-Type: application/json" \
  -d '{
    "site_name": "My Blog",
    "template": "personalblog"
  }'

# 2. إنشاء ملف محتوى
curl -X POST http://localhost:8000/api/content/index.md \
  -F "content=---\ntitle: Welcome\n---\n\n# Hello World"

# 3. بناء الموقع
curl -X POST http://localhost:8000/api/build

# 4. معاينة النتيجة
curl http://localhost:8000/api/build/preview > index.html
```

### مثال 2: إدارة المحتوى

```bash
# الحصول على قائمة الملفات
curl http://localhost:8000/api/content

# تعديل ملف موجود
curl -X POST http://localhost:8000/api/content/index.md \
  -F "content=# Updated Content"

# حذف ملف
curl -X DELETE http://localhost:8000/api/content/old-post.md
```

### مثال 3: تجربة القوالب المختلفة

```bash
# الحصول على قائمة القوالب
curl http://localhost:8000/api/templates

# بناء الموقع بقالب مختلف
curl -X POST http://localhost:8000/api/build \
  -H "Content-Type: application/json" \
  -d '{"template": "techblog"}'
```

---

## 🛠️ Integration Examples

### Python

```python
import requests
import json

BASE_URL = "http://localhost:8000/api"

# الحصول على الإعدادات
response = requests.get(f"{BASE_URL}/config")
config = response.json()

# تحديث الإعدادات
new_config = {
    "site_name": "My New Site",
    "template": "minimalist"
}
response = requests.post(f"{BASE_URL}/config", json=new_config)

# بناء الموقع
response = requests.post(f"{BASE_URL}/build")
result = response.json()
print(f"Pages built: {result['pages_count']}")
```

### JavaScript

```javascript
const BASE_URL = "http://localhost:8000/api";

// الحصول على الإعدادات
async function getConfig() {
  const response = await fetch(`${BASE_URL}/config`);
  return await response.json();
}

// تحديث الإعدادات
async function updateConfig(config) {
  const response = await fetch(`${BASE_URL}/config`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(config)
  });
  return await response.json();
}

// بناء الموقع
async function buildSite(template = null) {
  const response = await fetch(`${BASE_URL}/build`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ template })
  });
  return await response.json();
}
```

### cURL

```bash
# إنشاء متغير للـ URL الأساسي
BASE_URL="http://localhost:8000/api"

# الحصول على الإعدادات
curl $BASE_URL/config

# تحديث الإعدادات
curl -X POST $BASE_URL/config \
  -H "Content-Type: application/json" \
  -d '{"site_name":"New Name"}'

# بناء الموقع
curl -X POST $BASE_URL/build

# الحصول على الإحصائيات
curl $BASE_URL/stats
```

---

## 📝 Notes

- جميع مسارات الملفات نسبية بالنسبة لمجلد `MarkSite/content/`
- يمكن استخدام مسارات متداخلة مثل `blog/post1.md`
- الملفات يجب أن تنتهي بـ `.md` لكي تُعتبر ملفات محتوى
- القوالب يجب أن تكون من القائمة المتاحة

---

## 🔗 Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Markdown Guide](https://www.markdownguide.org/)
- [HTTP Status Codes](https://httpwg.org/specs/rfc7231.html#status.codes)

---

**آخر تحديث: 2025-01-13**
