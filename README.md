# MarkSite Dashboard

لوحة تحكم شاملة لإدارة مشروع **MarkSite** - مولد المواقع الثابتة الحديث.

## 🎯 المميزات

- **واجهة رسومية سهلة الاستخدام**: لوحة تحكم حديثة بدون تعقيدات
- **إدارة المحتوى**: إنشاء وتعديل وحذف ملفات Markdown بسهولة
- **إدارة الإعدادات**: تخصيص اسم الموقع والقالب والألوان
- **اختيار القوالب**: 24 قالب مختلف للاختيار من بينها
- **بناء الموقع**: بناء الموقع الثابت بضغطة زر واحدة
- **معاينة مباشرة**: معاينة الموقع المبني قبل النشر
- **ملفات ثابتة فقط**: واجهة HTML/CSS/JS بدون أطر عمل ثقيلة
- **API قوي**: API كامل يمكن استخدامه برمجياً

## 📋 المتطلبات

- Python 3.7+
- pip (مدير الحزم)

## 🚀 البدء السريع

### 1. تثبيت المتطلبات

```bash
pip install -r server/requirements.txt
```

### 2. تشغيل الخادم

**الطريقة الأولى (باستخدام السكريبت):**
```bash
./run_server.sh
```

**الطريقة الثانية (مباشرة):**
```bash
python3 server/app.py
```

### 3. الوصول إلى لوحة التحكم

افتح متصفحك وانتقل إلى:
```
http://localhost:8000
```

## 📁 هيكل المشروع

```
marksite-dashboard/
├── MarkSite/                    # مشروع MarkSite الأصلي
│   ├── content/                 # مجلد المحتوى (ملفات Markdown)
│   ├── site/                    # مجلد الإخراج (الموقع المبني)
│   ├── generator/               # محرك المولد
│   ├── config.yaml              # إعدادات الموقع
│   └── build.py                 # سكريبت البناء
├── server/
│   ├── app.py                   # تطبيق FastAPI الرئيسي
│   ├── requirements.txt          # المتطلبات
│   └── static/
│       ├── html/
│       │   └── index.html        # الواجهة الرئيسية
│       ├── css/
│       │   └── style.css         # الأنماط
│       └── js/
│           └── app.js            # منطق التطبيق
├── run_server.sh                # سكريبت التشغيل
└── README.md                    # هذا الملف
```

## 🎨 واجهة لوحة التحكم

### الصفحات المتاحة

1. **لوحة المعلومات** 📊
   - عرض إحصائيات المشروع
   - الملفات الأخيرة
   - الإجراءات السريعة

2. **الإعدادات** ⚙️
   - تعديل اسم الموقع
   - تعديل وصف الموقع
   - اختيار القالب
   - تعديل معلومات المؤلف
   - تخصيص الألوان

3. **إدارة المحتوى** 📝
   - عرض جميع ملفات Markdown
   - إنشاء ملفات جديدة
   - تعديل الملفات الموجودة
   - حذف الملفات
   - رفع ملفات جديدة

4. **بناء الموقع** 🔨
   - اختيار القالب
   - بدء عملية البناء
   - عرض سجل البناء
   - عرض نتائج البناء

5. **معاينة الموقع** 👁️
   - معاينة الموقع المبني
   - فتح المعاينة في نافذة جديدة

## 🔌 API Endpoints

### الإعدادات

```
GET  /api/config              # الحصول على الإعدادات
POST /api/config              # تحديث الإعدادات
GET  /api/templates           # قائمة القوالب المتاحة
```

### المحتوى

```
GET    /api/content                    # قائمة الملفات
GET    /api/content/{file_path}        # الحصول على محتوى ملف
POST   /api/content/{file_path}        # حفظ ملف
POST   /api/content/upload             # رفع ملف
DELETE /api/content/{file_path}        # حذف ملف
```

### البناء

```
POST /api/build                # بناء الموقع
GET  /api/build/status         # حالة البناء
GET  /api/build/preview        # معاينة الموقع
```

### الملفات والإحصائيات

```
GET /api/files                 # قائمة الملفات
GET /api/stats                 # إحصائيات المشروع
GET /api/health                # فحص صحة الخادم
```

## 📝 أمثلة الاستخدام

### الحصول على الإعدادات

```bash
curl http://localhost:8000/api/config
```

### تحديث الإعدادات

```bash
curl -X POST http://localhost:8000/api/config \
  -H "Content-Type: application/json" \
  -d '{
    "site_name": "موقعي الجديد",
    "site_description": "وصف الموقع",
    "template": "minimalist"
  }'
```

### إنشاء ملف جديد

```bash
curl -X POST http://localhost:8000/api/content/my-post.md \
  -F "content=# عنوان المقالة\n\nمحتوى المقالة"
```

### بناء الموقع

```bash
curl -X POST http://localhost:8000/api/build
```

### الحصول على الإحصائيات

```bash
curl http://localhost:8000/api/stats
```

## 🎨 القوالب المتاحة

يتوفر 24 قالب جميل للاختيار من بينها:

- default (الافتراضي)
- minimalist (بسيط)
- techblog (مدونة تقنية)
- documentation (توثيق)
- portfolio (محفظة)
- magazine (مجلة)
- landing (صفحة هبوط)
- creative (إبداعي)
- personalblog (مدونة شخصية)
- inkwell (حبر)
- futuristic (مستقبلي)
- monochrome (أحادي اللون)
- oasis (واحة)
- retrowave (موجة الثمانينات)
- serenity (هدوء)
- dark-nebula (سديم مظلم)
- vibrant-grid (شبكة نابضة)
- eco-green (أخضر بيئي)
- luxury-gold (ذهب فاخر)
- cyberpunk (سايبربانك)
- brutalist (بروتالي)
- oceanic (محيطي)
- autumn-whisper (همسة الخريف)
- neon-night (ليل نيون)

## 🛠️ التطوير والتخصيص

### تعديل الواجهة

الملفات الثابتة موجودة في:
- `server/static/html/index.html` - الهيكل
- `server/static/css/style.css` - الأنماط
- `server/static/js/app.js` - المنطق

### إضافة Endpoints جديدة

عدّل `server/app.py` وأضف الـ endpoints الجديدة:

```python
@app.get("/api/custom")
async def custom_endpoint():
    return JSONResponse({"success": True, "data": "..."})
```

### تعديل القوالب

القوالب موجودة في `MarkSite/generator/templates/`

## 🐛 استكشاف الأخطاء

### الخادم لا يبدأ

تأكد من:
1. تثبيت جميع المتطلبات: `pip install -r server/requirements.txt`
2. عدم استخدام المنفذ 8000 من قبل تطبيق آخر
3. وجود صلاحيات الكتابة في المجلد

### الملفات لا تُحفظ

تأكد من:
1. وجود صلاحيات الكتابة في مجلد `MarkSite/content/`
2. اسم الملف صحيح وينتهي بـ `.md`

### البناء يفشل

تأكد من:
1. وجود ملفات Markdown في مجلد `MarkSite/content/`
2. صيغة الملفات صحيحة (YAML frontmatter)
3. القالب المختار موجود

## 📚 الموارد الإضافية

- [MarkSite GitHub](https://github.com/Alqudimi/MarkSite)
- [Markdown Guide](https://www.markdownguide.org/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)

## 📄 الترخيص

هذا المشروع مرخص تحت MIT License

## 🤝 المساهمة

نرحب بالمساهمات! يرجى فتح issue أو pull request

## 📞 الدعم

للمساعدة والدعم، يرجى فتح issue على GitHub

---

**تم إنشاؤه بـ ❤️ لتسهيل إدارة المواقع الثابتة**
