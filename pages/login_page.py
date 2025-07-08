from selenium.webdriver.common.by import By
from locators.login_locators import LoginLocators

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def open_login_page(self):
        self.driver.find_element(By.XPATH, LoginLocators.LOGIN_LINK).click()

    def login(self, email, password):
        self.driver.find_element(By.XPATH, LoginLocators.EMAIL_INPUT).send_keys(email)
        self.driver.find_element(By.XPATH, LoginLocators.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(By.XPATH, LoginLocators.LOGIN_BUTTON).click()

    def is_logged_in(self):
        return self.driver.find_element(By.XPATH, LoginLocators.LOGOUT_BUTTON).is_displayed()
