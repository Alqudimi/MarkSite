# دليل الإعداد والتثبيت

## المتطلبات الأساسية

- **Python 3.7 أو أحدث**
- **pip** (مدير حزم Python)
- **متصفح ويب حديث** (Chrome, Firefox, Safari, Edge)

## خطوات التثبيت

### 1. التحقق من تثبيت Python

```bash
python3 --version
```

يجب أن تحصل على إصدار 3.7 أو أحدث.

### 2. استنساخ أو تحميل المشروع

```bash
# إذا كنت تستخدم git
git clone <repository-url>
cd marksite-dashboard

# أو قم بتحميل الملفات مباشرة
```

### 3. تثبيت المتطلبات

```bash
pip install -r server/requirements.txt
```

أو إذا كنت تستخدم pip3:

```bash
pip3 install -r server/requirements.txt
```

### 4. التحقق من التثبيت

```bash
python3 -c "import fastapi; print('FastAPI installed successfully')"
```

## تشغيل الخادم

### الطريقة الأولى: استخدام السكريبت (الموصى به)

```bash
./run_server.sh
```

### الطريقة الثانية: تشغيل مباشر

```bash
python3 server/app.py
```

### الطريقة الثالثة: استخدام Uvicorn مباشرة

```bash
uvicorn server.app:app --host 0.0.0.0 --port 8000 --reload
```

## الوصول إلى التطبيق

بعد تشغيل الخادم، افتح متصفحك وانتقل إلى:

```
http://localhost:8000
```

### الروابط المهمة

| الرابط | الوصف |
|--------|-------|
| `http://localhost:8000/` | لوحة التحكم الرئيسية |
| `http://localhost:8000/docs` | توثيق API التفاعلي (Swagger) |
| `http://localhost:8000/redoc` | توثيق API البديل (ReDoc) |
| `http://localhost:8000/api/health` | فحص صحة الخادم |

## إعدادات متقدمة

### تغيير المنفذ

```bash
# تشغيل على منفذ مختلف
python3 server/app.py --port 9000
```

أو عدّل `server/app.py`:

```python
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=9000)
```

### تشغيل في بيئة الإنتاج

```bash
# استخدام gunicorn (يجب تثبيته أولاً)
pip install gunicorn

# التشغيل
gunicorn server.app:app --workers 4 --worker-class uvicorn.workers.UvicornWorker
```

### تفعيل CORS

CORS مفعل بالفعل في التطبيق، لكن يمكنك تعديله في `server/app.py`:

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://yourdomain.com"],  # حدد النطاقات المسموحة
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

## استكشاف الأخطاء

### المشكلة: "Address already in use"

**الحل:** المنفذ 8000 قيد الاستخدام. استخدم منفذ مختلف:

```bash
python3 server/app.py --port 8001
```

أو ابحث عن العملية التي تستخدم المنفذ:

```bash
# على Linux/Mac
lsof -i :8000

# على Windows
netstat -ano | findstr :8000
```

### المشكلة: "ModuleNotFoundError: No module named 'fastapi'"

**الحل:** المتطلبات لم تُثبت. قم بتشغيل:

```bash
pip install -r server/requirements.txt
```

### المشكلة: الملفات لا تُحفظ

**الحل:** تأكد من وجود صلاحيات الكتابة:

```bash
chmod -R 755 MarkSite/content/
```

### المشكلة: البناء يفشل

**الحل:** تأكد من:
1. وجود ملفات Markdown في `MarkSite/content/`
2. صيغة الملفات صحيحة
3. القالب المختار موجود

## التحديثات والصيانة

### تحديث المتطلبات

```bash
pip install --upgrade -r server/requirements.txt
```

### مسح ذاكرة التخزين المؤقت

```bash
# حذف مجلد الموقع المبني
rm -rf MarkSite/site/

# حذف ملفات Python المؤقتة
find . -type d -name __pycache__ -exec rm -r {} +
```

## التكامل مع خدمات أخرى

### نشر على Heroku

1. أنشئ ملف `Procfile`:
```
web: python3 server/app.py
```

2. أنشئ ملف `runtime.txt`:
```
python-3.10.0
```

3. ادفع إلى Heroku:
```bash
git push heroku main
```

### نشر على PythonAnywhere

1. انسخ الملفات إلى PythonAnywhere
2. أنشئ تطبيق WSGI جديد
3. أشر إلى `server.app:app`

### نشر على Docker

أنشئ ملف `Dockerfile`:

```dockerfile
FROM python:3.10

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python3", "server/app.py"]
```

ثم:

```bash
docker build -t marksite-dashboard .
docker run -p 8000:8000 marksite-dashboard
```

## الأمان

### نصائح الأمان

1. **غيّر المضيف في الإنتاج**: لا تستخدم `0.0.0.0` في الإنتاج
2. **استخدم HTTPS**: استخدم شهادة SSL/TLS
3. **حدّد CORS**: لا تسمح بجميع النطاقات
4. **قيّد الوصول**: استخدم جدار الحماية
5. **نسخ احتياطية**: احتفظ بنسخ احتياطية من المحتوى

## الدعم

إذا واجهت مشاكل:

1. تحقق من هذا الدليل
2. ابحث في المشاكل المعروفة
3. افتح issue جديد مع التفاصيل

---

**آخر تحديث: 2025-01-13**
