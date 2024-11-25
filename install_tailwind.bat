@echo off
echo Installing Tailwind CSS...

:: Check if Node.js is installed
node -v >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Node.js is not installed. Please install Node.js first.
    exit /b 1
)

:: Initialize npm and install Tailwind CSS
npm install -D tailwindcss
npx tailwindcss init
npx tailwindcss -i ./static/src/input.css -o ./static/src/output.css

echo Tailwind CSS installation and configuration complete.
pause