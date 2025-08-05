import subprocess
import sys
import os
import requests
import importlib.util
from pathlib import Path

def check_package_installed(package):
"""Check if a package is already installed"""
try:
import(package)
return True
except ImportError:
# Handle special package name mappings
package_mappings = {
'Pillow': 'PIL',
'pywin32': 'win32api',
}



    if package in package_mappings:
        try:
            __import__(package_mappings[package])
            return True
        except ImportError:
            pass
    return False
def install_package(package):
"""Install a package using pip"""
try:
print(f"📦 Installing {package}...")
subprocess.check_call([sys.executable, "-m", "pip", "install", package, "--quiet"])
print(f"✅ {package} installed successfully")
return True
except subprocess.CalledProcessError as e:
print(f"❌ Failed to install {package}: {e}")
return False

def setup_dependencies():
"""Install all required dependencies"""
print("🚀 Checking dependencies...")



# List of required packages
dependencies = [
    "gradio",
    "numpy", 
    "Pillow",
    "pyautogui",
    "pywin32",
    "pyperclip",
    "pywebview",
    "requests",
    "cryptography",
    "keyboard"
]

to_install = []
already_installed = []

# Check which packages are already installed
for package in dependencies:
    if check_package_installed(package):
        already_installed.append(package)
        print(f"✅ {package} already installed")
    else:
        to_install.append(package)

if already_installed:
    print(f"📋 Already installed: {', '.join(already_installed)}")

# Install missing packages
if to_install:
    print(f"📦 Need to install: {', '.join(to_install)}")
    failed_installs = []
    
    for package in to_install:
        if not install_package(package):
            failed_installs.append(package)
    
    if failed_installs:
        print(f"⚠️ Failed to install: {', '.join(failed_installs)}")
        print("Please install these manually or check your internet connection")
        return False
else:
    print("🎉 All dependencies already installed!")

print("✅ Dependency check completed!")
return True
def download_file(url, filename):
"""Download a file from URL to current directory"""
try:
print(f"⬇️ Downloading from: {url}")
response = requests.get(url, stream=True, timeout=30)
response.raise_for_status()



    with open(filename, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)
    
    file_size = os.path.getsize(filename)
    print(f"✅ Downloaded successfully ({file_size} bytes)")
    return True
except requests.exceptions.ConnectionError as e:
    print(f"🌐 Connection Error - Check your internet connection")
    return False
except requests.exceptions.HTTPError as e:
    print(f"📄 HTTP Error {response.status_code} - File might not exist")
    return False
except Exception as e:
    print(f"❌ Download failed: {e}")
    return False
def download_encrypted_script():
"""Download the lighter_script.pyd to current directory"""
pyd_filename = "lighter_script.pyd"
local_path = os.path.join(os.getcwd(), pyd_filename)



# Delete existing file to update it
if os.path.exists(local_path):
    try:
        os.remove(local_path)
        print(f"🗑️ Removed old {pyd_filename} for update")
    except Exception as e:
        print(f"⚠️ Could not remove old file: {e}")

# Try multiple download sources
download_sources = [
    # GitHub raw URL (if repo becomes public)
    "https://github.com/DarkmoonOnDiscord/AutoDraw/raw/refs/heads/main/lighter_script.pyd",
    
    # Alternative hosting options (add your own)
    # "https://your-server.com/lighter_script.pyd",
    # "https://drive.google.com/uc?id=YOUR_FILE_ID",  # Google Drive direct link
]

for url in download_sources:
    print(f"📥 Downloading from: {url}")
    if download_file(url, local_path):
        return local_path
    print("❌ Download failed, trying next source...")

print(f"❌ Could not download {pyd_filename}")
print("💡 Solutions:")
print("  1. Make your GitHub repo public, OR")
print("  2. Host the file on a public server/CDN, OR") 
print("  3. Place lighter_script.pyd in the same folder as main.py manually")
print("  4. Use a file sharing service like Google Drive with direct link")
return None
def load_and_run_script():
"""Load the lighter_script.pyd and run it"""
pyd_filename = "lighter_script.pyd"
local_path = os.path.join(os.getcwd(), pyd_filename)



if not os.path.exists(local_path):
    print(f"❌ {pyd_filename} not found!")
    return False

try:
    print(f"🔓 Loading encrypted script: {local_path}")
    
    # Load the .pyd module
    spec = importlib.util.spec_from_file_location("lighter_script", local_path)
    lighter_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(lighter_module)
    
    print("✅ Encrypted script loaded successfully!")
    
    # Run using the pattern you specified
    if hasattr(lighter_module, 'main'):
        print("🎨 Starting lighter script...")
        # This calls the function you originally wrote as your app's entry point
        lighter_module.main()
    else:
        print("❌ No 'main' function found in lighter_script")
        return False
    
    return True
    
except Exception as e:
    print(f"❌ Error loading script: {e}")
    return False
def main():
"""Main entry point"""
print("🎨 Pixel Art Drawing Script Launcher")
print("=" * 50)



# Step 1: Install dependencies
if not setup_dependencies():
    print("❌ Dependency setup failed. Exiting...")
    sys.exit(1)

# Step 2: Download encrypted script to current directory
script_path = download_encrypted_script()
if not script_path:
    print("❌ Script download failed. Exiting...")
    sys.exit(1)

# Step 3: Load and run the encrypted script
try:
    if not load_and_run_script():
        print("❌ Failed to run encrypted script. Exiting...")
        sys.exit(1)
    
    print("Window closed, exiting script...")
except KeyboardInterrupt:
    print("\n🛑 Script interrupted by user")
except Exception as e:
    print(f"❌ Unexpected error: {e}")
if name == "main":
main()