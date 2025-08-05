import subprocess
import sys
import os
import requests
import importlib.util
import tempfile
from pathlib import Path
import time

class Colors:
    RESET = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
    BLUE = '\033[34m'
    WHITE = '\033[37m'
    RED = '\033[31m'
    
    BRIGHT_BLUE = '\033[94m'
    BRIGHT_WHITE = '\033[97m'
    BRIGHT_RED = '\033[91m'
    BRIGHT_YELLOW = '\033[93m'
    BRIGHT_GREEN = '\033[92m'
    YELLOW = '\033[33m'
    
    BG_BLUE = '\033[44m'
    BG_WHITE = '\033[47m'
    BG_RED = '\033[41m'

def gradient_text(text, start_color, end_color):
    colors = [start_color, Colors.BOLD + start_color, Colors.BRIGHT_WHITE, end_color, Colors.BOLD + end_color]
    result = ""
    for i, char in enumerate(text):
        color_index = int((i / len(text)) * (len(colors) - 1))
        result += colors[color_index] + char
    return result + Colors.RESET

def french_flag_text(text):
    colors = [Colors.BLUE, Colors.WHITE, Colors.RED]
    result = ""
    for i, char in enumerate(text):
        color = colors[i % len(colors)]
        result += color + char
    return result + Colors.RESET

def loading_animation(text, duration=2):
    chars = "⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏"
    end_time = time.time() + duration
    
    while time.time() < end_time:
        for char in chars:
            sys.stdout.write(f'\r{Colors.BLUE}{char}{Colors.RESET} {text}')
            sys.stdout.flush()
            time.sleep(0.1)
    sys.stdout.write(f'\r{Colors.BRIGHT_BLUE}✅{Colors.RESET} {text} Complete!\n')

def print_banner():
    banner = """
                                                                                                     
,-.----.                                                                                             
\    /  \                                   ,--,     ,----..                                 ___     
|   :    \   ,--,                         ,--.'|    /   /   \                      .--.,   ,--.'|_   
|   |  .\ :,--.'|                         |  | :   |   :     :  __  ,-.          ,--.'  \  |  | :,'  
.   :  |: ||  |,     ,--,  ,--,           :  : '   .   |  ;. /,' ,'/ /|          |  | /\/  :  : ' :  
|   |   \ :`--'_     |'. \/ .`|    ,---.  |  ' |   .   ; /--` '  | |' | ,--.--.  :  : :  .;__,'  /   
|   : .   /,' ,'|    '  \/  / ;   /     \ '  | |   ;   | ;    |  |   ,'/       \ :  | |-,|  |   |    
;   | |`-' '  | |     \  \.' /   /    /  ||  | :   |   : |    '  :  / .--.  .-. ||  : :/|:__,'| :    
|   | ;    |  | :      \  ;  ;  .    ' / |'  : |__ .   | '___ |  | '   \__\/: . .|  |  .'  '  : |__  
:   ' |    '  : |__   / \  \  \ '   ;   /||  | '.'|'   ; : .'|;  : |   ," .--.; |'  : '    |  | '.'| 
:   : :    |  | '.'|./__;   ;  \'   |  / |;  :    ;'   | '/  :|  , ;  /  /  ,.  ||  | |    ;  :    ; 
|   | :    ;  :    ;|   :/\  \ ;|   :    ||  ,   / |   :    /  ---'  ;  :   .'   \  : \    |  ,   /  
`---'.|    |  ,   / `---'  `--`  \   \  /  ---`-'   \   \ .'         |  ,     .-./  |,'     ---`-'   
  `---`     ---`-'                `----'             `---`            `--`---'   `--'                
                                                                                                     
"""
    
    lines = banner.strip().split('\n')
    for i, line in enumerate(lines):
        if i < 3 or i >= len(lines) - 2:
            print(f"{Colors.BLUE}{line}{Colors.RESET}")
        elif i % 3 == 0:
            print(f"{Colors.BLUE}{line}{Colors.RESET}")
        elif i % 3 == 1:
            print(f"{Colors.WHITE}{line}{Colors.RESET}")
        else:
            print(f"{Colors.RED}{line}{Colors.RESET}")
        if i > 2 and i < len(lines) - 3:
            time.sleep(0.02)
    print()

def show_license():
    license_text = f"""
{Colors.BG_BLUE}{Colors.WHITE} PIXELCRAFT LICENSE AGREEMENT {Colors.RESET}

{Colors.BRIGHT_BLUE}AutoDraw License{Colors.RESET}
{Colors.WHITE}Copyright (c) 2025 kiro.of{Colors.RESET}
{Colors.WHITE}All rights reserved.{Colors.RESET}

{Colors.BRIGHT_RED}IMPORTANT - PLEASE READ CAREFULLY:{Colors.RESET}

{Colors.BLUE}1. Grant of License{Colors.RESET}
Subject to the terms and conditions of this License, kiro.of hereby grants you a 
non-transferable, non-sublicensable, and non-exclusive license to use the software/material 
solely for private, personal, non-commercial purposes.

{Colors.BLUE}2. Restrictions{Colors.RESET}
You expressly agree that you shall NOT, under any circumstances:

• Distribute, transmit, publicly display, or publicly perform the software/material
• Reproduce, copy, duplicate, modify, adapt, translate, create derivative works of
• Use the software/material for any commercial purpose or for monetary compensation
• Rent, lease, lend, sublicense, or transfer the software/material to any third party
• {Colors.BRIGHT_RED}ONLY THE ORIGINAL OWNERS ARE AUTHORIZED TO SELL THIS SOFTWARE{Colors.RESET}

{Colors.BLUE}3. Ownership{Colors.RESET}
The software/material is licensed, not sold. All rights, title, and interest remain with kiro.of.

{Colors.BLUE}4. Educational Use Only{Colors.RESET}
{Colors.BRIGHT_RED}THIS SOFTWARE IS FOR EDUCATIONAL PURPOSES ONLY{Colors.RESET}
{Colors.RED}The creator is NOT responsible for any bans, damage, or consequences caused by using this software{Colors.RESET}

{Colors.BLUE}5. Disclaimer{Colors.RESET}
The software/material is provided "AS IS", without warranty of any kind, express or implied.

{Colors.BRIGHT_RED}BY USING THIS SOFTWARE, YOU ACKNOWLEDGE THAT:
- YOU HAVE READ AND UNDERSTAND THIS LICENSE
- YOU AGREE TO ALL TERMS AND CONDITIONS
- YOU USE THIS SOFTWARE AT YOUR OWN RISK
- THE CREATOR IS NOT RESPONSIBLE FOR ANY CONSEQUENCES{Colors.RESET}
"""
    
    print(license_text)
    print(f"{Colors.BRIGHT_YELLOW}Do you accept these terms? (y/n): {Colors.RESET}", end="")
    
    while True:
        choice = input().strip().lower()
        if choice in ['y', 'yes']:
            print(f"{Colors.BRIGHT_GREEN}✅ License accepted! Starting PixelCraft...{Colors.RESET}")
            return True
        elif choice in ['n', 'no']:
            print(f"{Colors.RED}❌ License not accepted. Exiting...{Colors.RESET}")
            return False
        else:
            print(f"{Colors.BRIGHT_YELLOW}Please enter 'y' for yes or 'n' for no: {Colors.RESET}", end="")

def check_package_installed(package):
    try:
        __import__(package)
        return True
    except ImportError:
        package_mappings = {
            'Pillow': 'PIL',
            'pywin32': 'win32api',
            'pywebview': 'webview',
        }

        if package in package_mappings:
            try:
                __import__(package_mappings[package])
                return True
            except ImportError:
                pass
        return False

def install_package(package):
    try:
        print(f"{Colors.BRIGHT_BLUE}📦 Installing {package}...{Colors.RESET}")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package, "--quiet"])
        print(f"{Colors.BRIGHT_BLUE}✅ {package} installed successfully{Colors.RESET}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"{Colors.RED}❌ Failed to install {package}: {e}{Colors.RESET}")
        return False

def setup_dependencies():
    print(f"{Colors.BRIGHT_BLUE}🚀 Checking dependencies...{Colors.RESET}")

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

    for package in dependencies:
        if check_package_installed(package):
            already_installed.append(package)
            print(f"{Colors.BRIGHT_BLUE}✅ {package} already installed{Colors.RESET}")
        else:
            to_install.append(package)

    if already_installed:
        print(f"{Colors.WHITE}📋 Already installed: {', '.join(already_installed)}{Colors.RESET}")

    if to_install:
        print(f"{Colors.BRIGHT_RED}📦 Need to install: {', '.join(to_install)}{Colors.RESET}")
        failed_installs = []
        
        for package in to_install:
            if not install_package(package):
                failed_installs.append(package)
        
        if failed_installs:
            print(f"{Colors.RED}⚠️ Failed to install: {', '.join(failed_installs)}{Colors.RESET}")
            print("Please install these manually or check your internet connection")
            return False
    else:
        print(f"{Colors.BRIGHT_BLUE}🎉 All dependencies already installed!{Colors.RESET}")

    print(f"{Colors.BRIGHT_BLUE}✅ Dependency check completed!{Colors.RESET}")
    return True

def download_file(url, filename):
    try:
        print(f"{Colors.BRIGHT_BLUE}⬇️ Downloading from: {url}{Colors.RESET}")
        response = requests.get(url, stream=True, timeout=30)
        response.raise_for_status()

        with open(filename, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        
        file_size = os.path.getsize(filename)
        print(f"{Colors.BRIGHT_BLUE}✅ Downloaded successfully ({file_size} bytes){Colors.RESET}")
        return True
    except requests.exceptions.ConnectionError as e:
        print(f"{Colors.RED}🌐 Connection Error - Check your internet connection{Colors.RESET}")
        return False
    except requests.exceptions.HTTPError as e:
        print(f"{Colors.RED}📄 HTTP Error {response.status_code} - File might not exist{Colors.RESET}")
        return False
    except Exception as e:
        print(f"{Colors.RED}❌ Download failed: {e}{Colors.RESET}")
        return False

def download_encrypted_script():
    temp_dir = os.path.join(tempfile.gettempdir(), 'pixelcrafter')
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)
    
    pyd_filename = "lighter_script.pyd"
    local_path = os.path.join(temp_dir, pyd_filename)

    print(f"{Colors.WHITE}📁 Using temp directory: {temp_dir}{Colors.RESET}")

    if os.path.exists(local_path):
        try:
            os.remove(local_path)
            print(f"{Colors.BRIGHT_RED}🗑️ Removed old {pyd_filename} for update{Colors.RESET}")
        except Exception as e:
            print(f"{Colors.RED}⚠️ Could not remove old file: {e}{Colors.RESET}")

    download_sources = [
        "https://github.com/DarkmoonOnDiscord/AutoDraw/raw/refs/heads/main/lighter_script.pyd",
    ]

    for url in download_sources:
        print(f"{Colors.BRIGHT_BLUE}📥 Downloading from: {url}{Colors.RESET}")
        if download_file(url, local_path):
            return local_path
        print(f"{Colors.RED}❌ Download failed, trying next source...{Colors.RESET}")

    print(f"{Colors.RED}❌ Could not download {pyd_filename}{Colors.RESET}")
    print(f"{Colors.BRIGHT_RED}💡 Solutions:{Colors.RESET}")
    print("  1. Make your GitHub repo public, OR")
    print("  2. Host the file on a public server/CDN, OR") 
    print("  3. Place lighter_script.pyd in the temp/pixelcrafter folder manually")
    print("  4. Use a file sharing service like Google Drive with direct link")
    return None

def load_and_run_script():
    temp_dir = os.path.join(tempfile.gettempdir(), 'pixelcrafter')
    pyd_filename = "lighter_script.pyd"
    local_path = os.path.join(temp_dir, pyd_filename)

    if not os.path.exists(local_path):
        print(f"{Colors.RED}❌ {pyd_filename} not found in temp directory!{Colors.RESET}")
        return False

    try:
        print(f"{Colors.BRIGHT_BLUE}🔓 Loading encrypted script: {local_path}{Colors.RESET}")
        
        spec = importlib.util.spec_from_file_location("lighter_script", local_path)
        lighter_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(lighter_module)
        
        print(f"{Colors.BRIGHT_BLUE}✅ Encrypted script loaded successfully!{Colors.RESET}")
        
        if hasattr(lighter_module, 'main'):
            print(f"{Colors.BRIGHT_BLUE}🎨 Starting PixelCraft script...{Colors.RESET}")
            lighter_module.main()
        else:
            print(f"{Colors.RED}❌ No 'main' function found in lighter_script{Colors.RESET}")
            return False
        
        return True
        
    except Exception as e:
        print(f"{Colors.RED}❌ Error loading script: {e}{Colors.RESET}")
        return False

def main():
    print_banner()
    print(french_flag_text("🎨 PixelCraft Pro - Pixel Art Drawing Script Launcher"))
    print("=" * 60)
    
    if not show_license():
        sys.exit(1)
    
    print()

    loading_animation("Initializing PixelCraft system")
    
    if not setup_dependencies():
        print(f"{Colors.RED}❌ Dependency setup failed. Exiting...{Colors.RESET}")
        sys.exit(1)

    script_path = download_encrypted_script()
    if not script_path:
        print(f"{Colors.RED}❌ Script download failed. Exiting...{Colors.RESET}")
        sys.exit(1)

    try:
        if not load_and_run_script():
            print(f"{Colors.RED}❌ Failed to run encrypted script. Exiting...{Colors.RESET}")
            sys.exit(1)
        
        print(f"{Colors.BRIGHT_BLUE}Window closed, exiting script...{Colors.RESET}")
    except KeyboardInterrupt:
        print(f"\n{Colors.BRIGHT_RED}🛑 Script interrupted by user{Colors.RESET}")
    except Exception as e:
        print(f"{Colors.RED}❌ Unexpected error: {e}{Colors.RESET}")

if __name__ == "__main__":
    main()