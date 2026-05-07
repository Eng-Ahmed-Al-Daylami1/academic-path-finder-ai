@echo off
chcp 65001 >nul
echo ========================================
echo   تهيئة Git للمشروع
echo   Academic Path Finder AI
echo ========================================
echo.

echo [1/5] تهيئة مستودع Git...
git init
if %errorlevel% neq 0 (
    echo ❌ فشل: تأكد من تثبيت Git
    pause
    exit /b 1
)
echo ✅ تم

echo.
echo [2/5] إضافة الملفات...
git add .
echo ✅ تم

echo.
echo [3/5] عرض الملفات المضافة...
echo.
git status
echo.

echo [4/5] التحقق من الملفات المحمية...
git status | findstr ".env" >nul
if %errorlevel% equ 0 (
    echo ⚠️  تحذير: ملف .env موجود! يجب حذفه من Git
    pause
) else (
    echo ✅ ملف .env محمي
)

echo.
echo [5/5] إنشاء أول commit...
git commit -m "Initial commit: Academic Path Finder AI v2.0"
if %errorlevel% neq 0 (
    echo ⚠️  تحذير: قد تحتاج لإعداد Git config
    echo.
    echo نفذ الأوامر التالية:
    echo git config --global user.name "Your Name"
    echo git config --global user.email "your.email@example.com"
    echo.
    echo ثم أعد تشغيل هذا السكريبت
    pause
    exit /b 1
)
echo ✅ تم

echo.
echo ========================================
echo   ✅ Git جاهز!
echo ========================================
echo.
echo الخطوة التالية:
echo 1. أنشئ مستودع على GitHub
echo 2. نفذ الأمر التالي (استبدل YOUR_USERNAME):
echo.
echo    git remote add origin https://github.com/YOUR_USERNAME/academic-path-finder-ai.git
echo    git branch -M main
echo    git push -u origin main
echo.
pause
