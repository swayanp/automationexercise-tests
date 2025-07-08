import pytest
from pages.login_page import LoginPage
from utilities.driver_setup import create_driver

@pytest.fixture
def driver():
    driver = create_driver()
    driver.get("https://automationexercise.com")
    yield driver
    driver.quit()

def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.open_login_page()
    login_page.login("practicetest@gmail.com", "Parctice@1234")
    assert login_page.is_logged_in()
