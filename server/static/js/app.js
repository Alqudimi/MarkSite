// ============================================================================
// MarkSite Dashboard - Main Application
// ============================================================================

const API_BASE = '/api';
let currentFile = null;
let uploadedFile = null;

// ============================================================================
// Initialization
// ============================================================================

document.addEventListener('DOMContentLoaded', () => {
    initializeEventListeners();
    loadDashboard();
    loadTemplates();
});

// ============================================================================
// Event Listeners
// ============================================================================

function initializeEventListeners() {
    // Navigation
    document.querySelectorAll('.nav-item').forEach(item => {
        item.addEventListener('click', (e) => {
            e.preventDefault();
            const page = item.dataset.page;
            navigateTo(page);
        });
    });

    // Dashboard buttons
    document.getElementById('refresh-btn').addEventListener('click', loadDashboard);
    document.getElementById('build-btn').addEventListener('click', () => navigateTo('build'));
    document.getElementById('new-content-btn').addEventListener('click', () => openNewFileModal());
    document.getElementById('build-quick-btn').addEventListener('click', buildSite);
    document.getElementById('preview-quick-btn').addEventListener('click', () => navigateTo('preview'));

    // Config form
    document.getElementById('config-form').addEventListener('submit', saveConfig);

    // Content management
    document.getElementById('new-file-btn').addEventListener('click', () => openNewFileModal());
    document.getElementById('upload-file-btn').addEventListener('click', () => openUploadModal());

    // Editor modal
    document.getElementById('close-editor').addEventListener('click', closeEditorModal);
    document.getElementById('cancel-editor').addEventListener('click', closeEditorModal);
    document.getElementById('save-editor').addEventListener('click', saveFile);

    // Upload modal
    document.getElementById('close-upload').addEventListener('click', closeUploadModal);
    document.getElementById('cancel-upload').addEventListener('click', closeUploadModal);
    document.getElementById('confirm-upload').addEventListener('click', uploadFile);

    // Upload area drag and drop
    const uploadArea = document.getElementById('upload-area');
    uploadArea.addEventListener('click', () => document.getElementById('file-input').click());
    uploadArea.addEventListener('dragover', (e) => {
        e.preventDefault();
        uploadArea.classList.add('drag-over');
    });
    uploadArea.addEventListener('dragleave', () => {
        uploadArea.classList.remove('drag-over');
    });
    uploadArea.addEventListener('drop', (e) => {
        e.preventDefault();
        uploadArea.classList.remove('drag-over');
        const files = e.dataTransfer.files;
        if (files.length > 0) {
            uploadedFile = files[0];
            document.getElementById('confirm-upload').disabled = false;
        }
    });

    document.getElementById('file-input').addEventListener('change', (e) => {
        if (e.target.files.length > 0) {
            uploadedFile = e.target.files[0];
            document.getElementById('confirm-upload').disabled = false;
        }
    });

    // Build page
    document.getElementById('start-build').addEventListener('click', buildSite);
    document.getElementById('open-preview').addEventListener('click', openPreview);
}

// ============================================================================
// Navigation
// ============================================================================

function navigateTo(page) {
    // Update active nav item
    document.querySelectorAll('.nav-item').forEach(item => {
        item.classList.remove('active');
        if (item.dataset.page === page) {
            item.classList.add('active');
        }
    });

    // Update page title
    const titles = {
        dashboard: 'لوحة المعلومات',
        config: 'الإعدادات',
        content: 'إدارة المحتوى',
        build: 'بناء الموقع',
        preview: 'معاينة الموقع'
    };
    document.getElementById('page-title').textContent = titles[page] || 'لوحة المعلومات';

    // Show/hide pages
    document.querySelectorAll('.page').forEach(p => p.classList.remove('active'));
    const targetPage = document.getElementById(`${page}-page`);
    if (targetPage) {
        targetPage.classList.add('active');
        
        // Load page-specific data
        if (page === 'config') {
            loadConfig();
        } else if (page === 'content') {
            loadContentList();
        } else if (page === 'build') {
            loadBuildStatus();
        }
    }
}

// ============================================================================
// Dashboard
// ============================================================================

async function loadDashboard() {
    try {
        const response = await fetch(`${API_BASE}/stats`);
        const data = await response.json();
        
        if (data.success) {
            const stats = data.stats;
            document.getElementById('stat-content').textContent = stats.content_files;
            document.getElementById('stat-pages').textContent = stats.output_files;
            document.getElementById('stat-template').textContent = stats.template;
            
            const status = stats.output_files > 0 ? 'مبني ✓' : 'غير مبني';
            document.getElementById('stat-status').textContent = status;
        }
        
        loadRecentFiles();
    } catch (error) {
        showToast('خطأ في تحميل البيانات', 'error');
        console.error(error);
    }
}

async function loadRecentFiles() {
    try {
        const response = await fetch(`${API_BASE}/content`);
        const data = await response.json();
        
        if (data.success) {
            const list = document.getElementById('recent-list');
            list.innerHTML = '';
            
            const files = data.files.slice(0, 5);
            if (files.length === 0) {
                list.innerHTML = '<li class="loading">لا توجد ملفات</li>';
                return;
            }
            
            files.forEach(file => {
                const li = document.createElement('li');
                li.innerHTML = `
                    <span class="file-item-name">📄 ${file.name}</span>
                    <span class="file-item-date">${new Date(file.modified).toLocaleDateString('ar-SA')}</span>
                `;
                list.appendChild(li);
            });
        }
    } catch (error) {
        console.error(error);
    }
}

// ============================================================================
// Configuration
// ============================================================================

async function loadConfig() {
    try {
        const response = await fetch(`${API_BASE}/config`);
        const data = await response.json();
        
        if (data.success) {
            const config = data.data;
            document.getElementById('site-name').value = config.site_name || '';
            document.getElementById('site-description').value = config.site_description || '';
            document.getElementById('site-url').value = config.site_url || '';
            document.getElementById('template').value = config.template || 'default';
            
            if (config.author) {
                document.getElementById('author-name').value = config.author.name || '';
                document.getElementById('author-email').value = config.author.email || '';
            }
            
            if (config.theme) {
                document.getElementById('primary-color').value = config.theme.primary_color || '#0d6efd';
            }
        }
    } catch (error) {
        showToast('خطأ في تحميل الإعدادات', 'error');
        console.error(error);
    }
}

async function saveConfig(e) {
    e.preventDefault();
    
    try {
        const config = {
            site_name: document.getElementById('site-name').value,
            site_description: document.getElementById('site-description').value,
            site_url: document.getElementById('site-url').value,
            template: document.getElementById('template').value,
            author: {
                name: document.getElementById('author-name').value,
                email: document.getElementById('author-email').value
            },
            theme: {
                primary_color: document.getElementById('primary-color').value,
                secondary_color: '#6c757d'
            }
        };
        
        const response = await fetch(`${API_BASE}/config`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(config)
        });
        
        const data = await response.json();
        
        if (data.success) {
            showToast('تم حفظ الإعدادات بنجاح', 'success');
        } else {
            showToast('خطأ في حفظ الإعدادات', 'error');
        }
    } catch (error) {
        showToast('خطأ في حفظ الإعدادات', 'error');
        console.error(error);
    }
}

// ============================================================================
// Templates
// ============================================================================

async function loadTemplates() {
    try {
        const response = await fetch(`${API_BASE}/templates`);
        const data = await response.json();
        
        if (data.success) {
            const templates = data.templates;
            
            // Update config template selector
            const configSelect = document.getElementById('template');
            templates.forEach(template => {
                if (!configSelect.querySelector(`option[value="${template}"]`)) {
                    const option = document.createElement('option');
                    option.value = template;
                    option.textContent = template;
                    configSelect.appendChild(option);
                }
            });
            
            // Update build template selector
            const buildSelect = document.getElementById('build-template');
            templates.forEach(template => {
                if (!buildSelect.querySelector(`option[value="${template}"]`)) {
                    const option = document.createElement('option');
                    option.value = template;
                    option.textContent = template;
                    buildSelect.appendChild(option);
                }
            });
        }
    } catch (error) {
        console.error(error);
    }
}

// ============================================================================
// Content Management
// ============================================================================

async function loadContentList() {
    try {
        const response = await fetch(`${API_BASE}/content`);
        const data = await response.json();
        
        if (data.success) {
            const list = document.getElementById('content-list');
            list.innerHTML = '';
            
            if (data.files.length === 0) {
                list.innerHTML = '<li class="loading">لا توجد ملفات</li>';
                return;
            }
            
            data.files.forEach(file => {
                const li = document.createElement('li');
                const date = new Date(file.modified).toLocaleDateString('ar-SA');
                li.innerHTML = `
                    <span class="file-item-name">📄 ${file.name}</span>
                    <span class="file-item-date">${date}</span>
                    <div class="file-item-actions">
                        <button class="btn btn-secondary" onclick="editFile('${file.path}')">✏️ تعديل</button>
                        <button class="btn btn-danger" onclick="deleteFile('${file.path}')">🗑️ حذف</button>
                    </div>
                `;
                list.appendChild(li);
            });
        }
    } catch (error) {
        showToast('خطأ في تحميل قائمة الملفات', 'error');
        console.error(error);
    }
}

function openNewFileModal() {
    currentFile = null;
    document.getElementById('editor-title').textContent = 'ملف جديد';
    document.getElementById('file-editor').value = '';
    document.getElementById('editor-modal').classList.add('active');
}

async function editFile(filePath) {
    try {
        const response = await fetch(`${API_BASE}/content/${filePath}`);
        const data = await response.json();
        
        if (data.success) {
            currentFile = filePath;
            document.getElementById('editor-title').textContent = `تعديل: ${filePath}`;
            document.getElementById('file-editor').value = data.content;
            document.getElementById('editor-modal').classList.add('active');
        }
    } catch (error) {
        showToast('خطأ في تحميل الملف', 'error');
        console.error(error);
    }
}

function closeEditorModal() {
    document.getElementById('editor-modal').classList.remove('active');
    currentFile = null;
}

async function saveFile() {
    try {
        const content = document.getElementById('file-editor').value;
        
        if (!currentFile) {
            // New file
            const fileName = prompt('أدخل اسم الملف (بدون امتداد):');
            if (!fileName) return;
            currentFile = fileName + '.md';
        }
        
        const formData = new FormData();
        formData.append('content', content);
        
        const response = await fetch(`${API_BASE}/content/${currentFile}`, {
            method: 'POST',
            body: formData
        });
        
        const data = await response.json();
        
        if (data.success) {
            showToast('تم حفظ الملف بنجاح', 'success');
            closeEditorModal();
            loadContentList();
        } else {
            showToast('خطأ في حفظ الملف', 'error');
        }
    } catch (error) {
        showToast('خطأ في حفظ الملف', 'error');
        console.error(error);
    }
}

async function deleteFile(filePath) {
    if (!confirm('هل أنت متأكد من حذف هذا الملف؟')) return;
    
    try {
        const response = await fetch(`${API_BASE}/content/${filePath}`, {
            method: 'DELETE'
        });
        
        const data = await response.json();
        
        if (data.success) {
            showToast('تم حذف الملف بنجاح', 'success');
            loadContentList();
        } else {
            showToast('خطأ في حذف الملف', 'error');
        }
    } catch (error) {
        showToast('خطأ في حذف الملف', 'error');
        console.error(error);
    }
}

function openUploadModal() {
    uploadedFile = null;
    document.getElementById('confirm-upload').disabled = true;
    document.getElementById('upload-modal').classList.add('active');
}

function closeUploadModal() {
    document.getElementById('upload-modal').classList.remove('active');
    uploadedFile = null;
}

async function uploadFile() {
    if (!uploadedFile) {
        showToast('يرجى اختيار ملف', 'error');
        return;
    }
    
    try {
        const formData = new FormData();
        formData.append('file', uploadedFile);
        
        const response = await fetch(`${API_BASE}/content/upload`, {
            method: 'POST',
            body: formData
        });
        
        const data = await response.json();
        
        if (data.success) {
            showToast('تم رفع الملف بنجاح', 'success');
            closeUploadModal();
            loadContentList();
        } else {
            showToast('خطأ في رفع الملف', 'error');
        }
    } catch (error) {
        showToast('خطأ في رفع الملف', 'error');
        console.error(error);
    }
}

// ============================================================================
// Build Management
// ============================================================================

async function loadBuildStatus() {
    try {
        const response = await fetch(`${API_BASE}/build/status`);
        const data = await response.json();
        
        if (data.success) {
            if (data.built) {
                document.getElementById('open-preview').style.display = 'inline-flex';
            }
        }
    } catch (error) {
        console.error(error);
    }
}

async function buildSite() {
    try {
        document.getElementById('build-log').style.display = 'block';
        document.getElementById('log-content').textContent = 'جاري البناء...';
        document.getElementById('build-result').style.display = 'none';
        
        const template = document.getElementById('build-template').value || null;
        
        const response = await fetch(`${API_BASE}/build`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ template })
        });
        
        const data = await response.json();
        
        if (data.success) {
            document.getElementById('log-content').textContent = `✓ تم بناء الموقع بنجاح!\n\nعدد الصفحات: ${data.pages_count}\nمجلد الإخراج: ${data.output_dir}`;
            document.getElementById('build-result').style.display = 'block';
            document.getElementById('result-content').innerHTML = `
                <p><strong>✓ نجح البناء!</strong></p>
                <p>عدد الصفحات: <strong>${data.pages_count}</strong></p>
                <p>مجلد الإخراج: <code>${data.output_dir}</code></p>
            `;
            showToast('تم بناء الموقع بنجاح', 'success');
            loadDashboard();
        } else {
            document.getElementById('log-content').textContent = `✗ خطأ في البناء:\n${data.detail || 'خطأ غير معروف'}`;
            showToast('خطأ في بناء الموقع', 'error');
        }
    } catch (error) {
        document.getElementById('log-content').textContent = `✗ خطأ في البناء:\n${error.message}`;
        showToast('خطأ في بناء الموقع', 'error');
        console.error(error);
    }
}

function openPreview() {
    window.open('/api/build/preview', '_blank');
}

// ============================================================================
// Toast Notifications
// ============================================================================

function showToast(message, type = 'info') {
    const toast = document.getElementById('toast');
    toast.textContent = message;
    toast.className = `toast show ${type}`;
    
    setTimeout(() => {
        toast.classList.remove('show');
    }, 3000);
}

// ============================================================================
// Utilities
// ============================================================================

function formatDate(dateString) {
    return new Date(dateString).toLocaleDateString('ar-SA');
}
