import pytest
from utilities.driver_setup import create_driver

def test_open_automationexercise():
    """Test that Automation Exercise homepage loads correctly"""
    driver = create_driver()
    
    try:
        # Navigate to website
        driver.get("https://automationexercise.com")
        
        # Verify page title
        assert "Automation Exercise" in driver.title
        
    finally:
        # Ensure browser closes even if test fails
        driver.quit()