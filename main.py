import subprocess
import sys
import os
import requests
import importlib.util
import tempfile
from pathlib import Path
import time

# ANSI Color Codes with Gradients
class Colors:
    RESET = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
    # Standard Colors
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    
    # Bright Colors
    BRIGHT_BLACK = '\033[90m'
    BRIGHT_RED = '\033[91m'
    BRIGHT_GREEN = '\033[92m'
    BRIGHT_YELLOW = '\033[93m'
    BRIGHT_BLUE = '\033[94m'
    BRIGHT_MAGENTA = '\033[95m'
    BRIGHT_CYAN = '\033[96m'
    BRIGHT_WHITE = '\033[97m'
    
    # Background Colors
    BG_BLACK = '\033[40m'
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'
    BG_MAGENTA = '\033[45m'
    BG_CYAN = '\033[46m'
    BG_WHITE = '\033[47m'

def gradient_text(text, start_color, end_color):
    """Create gradient text effect"""
    colors = [start_color, Colors.BOLD + start_color, Colors.BRIGHT_WHITE, end_color, Colors.BOLD + end_color]
    result = ""
    for i, char in enumerate(text):
        color_index = int((i / len(text)) * (len(colors) - 1))
        result += colors[color_index] + char
    return result + Colors.RESET

def rainbow_text(text):
    """Create rainbow text effect"""
    rainbow_colors = [
        Colors.RED, Colors.BRIGHT_RED,
        Colors.YELLOW, Colors.BRIGHT_YELLOW,
        Colors.GREEN, Colors.BRIGHT_GREEN,
        Colors.CYAN, Colors.BRIGHT_CYAN,
        Colors.BLUE, Colors.BRIGHT_BLUE,
        Colors.MAGENTA, Colors.BRIGHT_MAGENTA
    ]
    result = ""
    for i, char in enumerate(text):
        color = rainbow_colors[i % len(rainbow_colors)]
        result += color + char
    return result + Colors.RESET

def loading_animation(text, duration=2):
    """Display loading animation"""
    chars = "⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏"
    end_time = time.time() + duration
    
    while time.time() < end_time:
        for char in chars:
            sys.stdout.write(f'\r{Colors.CYAN}{char}{Colors.RESET} {text}')
            sys.stdout.flush()
            time.sleep(0.1)
    sys.stdout.write(f'\r{Colors.GREEN}✅{Colors.RESET} {text} Complete!\n')

def print_banner():
    """Display cool banner with gradients"""
    banner = [
        " █████╗ ██╗     ███████╗ ██████╗████████╗██╗███╗   ██╗ ██████╗ ",
        "██╔══██╗██║     ██╔════╝██╔════╝╚══██╔══╝██║████╗  ██║██╔════╝ ",
        "███████║██║     █████╗  ██║        ██║   ██║██╔██╗ ██║██║  ███╗",
        "██╔══██║██║     ██╔══╝  ██║        ██║   ██║██║╚██╗██║██║   ██║",
        "██║  ██║███████╗███████╗╚██████╗   ██║   ██║██║ ╚████║╚██████╔╝",
        "╚═╝  ╚═╝╚══════╝╚══════╝ ╚═════╝   ╚═╝   ╚═╝╚═╝  ╚═══╝ ╚═════╝ "
    ]
    
    print("\n")
    for line in banner:
        print(gradient_text(line, Colors.CYAN, Colors.MAGENTA))
        time.sleep(0.05)
    print("\n")

def check_package_installed(package):
    """Check if a package is already installed"""
    try:
        __import__(package)
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
        print(f"{Colors.BRIGHT_YELLOW}📦 Installing {package}...{Colors.RESET}")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package, "--quiet"])
        print(f"{Colors.BRIGHT_GREEN}✅ {package} installed successfully{Colors.RESET}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"{Colors.RED}❌ Failed to install {package}: {e}{Colors.RESET}")
        return False

def setup_dependencies():
    """Install all required dependencies"""
    print(f"{Colors.BRIGHT_CYAN}🚀 Checking dependencies...{Colors.RESET}")

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
            print(f"{Colors.BRIGHT_GREEN}✅ {package} already installed{Colors.RESET}")
        else:
            to_install.append(package)

    if already_installed:
        print(f"{Colors.BRIGHT_MAGENTA}📋 Already installed: {', '.join(already_installed)}{Colors.RESET}")

    # Install missing packages
    if to_install:
        print(f"{Colors.BRIGHT_YELLOW}📦 Need to install: {', '.join(to_install)}{Colors.RESET}")
        failed_installs = []
        
        for package in to_install:
            if not install_package(package):
                failed_installs.append(package)
        
        if failed_installs:
            print(f"{Colors.RED}⚠️ Failed to install: {', '.join(failed_installs)}{Colors.RESET}")
            print("Please install these manually or check your internet connection")
            return False
    else:
        print(f"{Colors.BRIGHT_GREEN}🎉 All dependencies already installed!{Colors.RESET}")

    print(f"{Colors.BRIGHT_GREEN}✅ Dependency check completed!{Colors.RESET}")
    return True

def download_file(url, filename):
    """Download a file from URL to specified directory"""
    try:
        print(f"{Colors.BRIGHT_CYAN}⬇️ Downloading from: {url}{Colors.RESET}")
        response = requests.get(url, stream=True, timeout=30)
        response.raise_for_status()

        with open(filename, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        
        file_size = os.path.getsize(filename)
        print(f"{Colors.BRIGHT_GREEN}✅ Downloaded successfully ({file_size} bytes){Colors.RESET}")
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
    """Download the lighter_script.pyd to temp directory"""
    # Create temp directory for pixelcraft
    temp_dir = os.path.join(tempfile.gettempdir(), 'pixelcraft')
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)
    
    pyd_filename = "lighter_script.pyd"
    local_path = os.path.join(temp_dir, pyd_filename)

    print(f"{Colors.BRIGHT_MAGENTA}📁 Using temp directory: {temp_dir}{Colors.RESET}")

    # Delete existing file to update it
    if os.path.exists(local_path):
        try:
            os.remove(local_path)
            print(f"{Colors.BRIGHT_YELLOW}🗑️ Removed old {pyd_filename} for update{Colors.RESET}")
        except Exception as e:
            print(f"{Colors.YELLOW}⚠️ Could not remove old file: {e}{Colors.RESET}")

    # Try multiple download sources
    download_sources = [
        # GitHub raw URL (if repo becomes public)
        "https://github.com/DarkmoonOnDiscord/AutoDraw/raw/refs/heads/main/lighter_script.pyd",
        
        # Alternative hosting options (add your own)
        # "https://your-server.com/lighter_script.pyd",
        # "https://drive.google.com/uc?id=YOUR_FILE_ID",  # Google Drive direct link
    ]

    for url in download_sources:
        print(f"{Colors.BRIGHT_CYAN}📥 Downloading from: {url}{Colors.RESET}")
        if download_file(url, local_path):
            return local_path
        print(f"{Colors.RED}❌ Download failed, trying next source...{Colors.RESET}")

    print(f"{Colors.RED}❌ Could not download {pyd_filename}{Colors.RESET}")
    print(f"{Colors.BRIGHT_YELLOW}💡 Solutions:{Colors.RESET}")
    print("  1. Make your GitHub repo public, OR")
    print("  2. Host the file on a public server/CDN, OR") 
    print("  3. Place lighter_script.pyd in the temp/pixelcraft folder manually")
    print("  4. Use a file sharing service like Google Drive with direct link")
    return None

def load_and_run_script():
    """Load the lighter_script.pyd from temp directory and run it"""
    # Look for the pyd file in temp directory
    temp_dir = os.path.join(tempfile.gettempdir(), 'pixelcraft')
    pyd_filename = "lighter_script.pyd"
    local_path = os.path.join(temp_dir, pyd_filename)

    if not os.path.exists(local_path):
        print(f"{Colors.RED}❌ {pyd_filename} not found in temp directory!{Colors.RESET}")
        return False

    try:
        print(f"{Colors.BRIGHT_CYAN}🔓 Loading encrypted script: {local_path}{Colors.RESET}")
        
        # Load the .pyd module
        spec = importlib.util.spec_from_file_location("lighter_script", local_path)
        lighter_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(lighter_module)
        
        print(f"{Colors.BRIGHT_GREEN}✅ Encrypted script loaded successfully!{Colors.RESET}")
        
        # Run using the pattern you specified
        if hasattr(lighter_module, 'main'):
            print(f"{Colors.BRIGHT_MAGENTA}🎨 Starting lighter script...{Colors.RESET}")
            # This calls the function you originally wrote as your app's entry point
            lighter_module.main()
        else:
            print(f"{Colors.RED}❌ No 'main' function found in lighter_script{Colors.RESET}")
            return False
        
        return True
        
    except Exception as e:
        print(f"{Colors.RED}❌ Error loading script: {e}{Colors.RESET}")
        return False

def main():
    """Main entry point"""
    # Display cool banner
    print_banner()
    print(gradient_text("🎨 Pixel Art Drawing Script Launcher", Colors.BRIGHT_CYAN, Colors.BRIGHT_MAGENTA))
    print("=" * 60)

    # Loading animations
    loading_animation("Initializing system")
    
    # Step 1: Install dependencies
    if not setup_dependencies():
        print(f"{Colors.RED}❌ Dependency setup failed. Exiting...{Colors.RESET}")
        sys.exit(1)

    # Step 2: Download encrypted script to temp directory
    script_path = download_encrypted_script()
    if not script_path:
        print(f"{Colors.RED}❌ Script download failed. Exiting...{Colors.RESET}")
        sys.exit(1)

    # Step 3: Load and run the encrypted script
    try:
        if not load_and_run_script():
            print(f"{Colors.RED}❌ Failed to run encrypted script. Exiting...{Colors.RESET}")
            sys.exit(1)
        
        print(f"{Colors.BRIGHT_GREEN}Window closed, exiting script...{Colors.RESET}")
    except KeyboardInterrupt:
        print(f"\n{Colors.BRIGHT_YELLOW}🛑 Script interrupted by user{Colors.RESET}")
    except Exception as e:
        print(f"{Colors.RED}❌ Unexpected error: {e}{Colors.RESET}")

if __name__ == "__main__":
    main()
