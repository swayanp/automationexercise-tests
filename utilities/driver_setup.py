from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import tempfile

def create_driver():
    """Create and configure a Chrome WebDriver instance"""
    options = Options()
    
    # Essential options for Docker
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    # options.add_argument("--window-size=1920,1080")
    
    # Additional configuration
    options.add_argument("--incognito")
    options.add_argument("--start-maximized")
    # options.add_argument("--auto-open-devtools-for-tabs")  # Opens Chrome DevTools
    options.add_argument("--disable-gpu")
    
    # Create temporary user data directory
    user_data_dir = tempfile.mkdtemp()
    options.add_argument(f"--user-data-dir={user_data_dir}")
    
    # Set up service with automatic driver management
    service = Service(ChromeDriverManager().install())
    
    return webdriver.Chrome(service=service, options=options)