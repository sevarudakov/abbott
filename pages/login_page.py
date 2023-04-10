import logging
from selenium.webdriver.common.by import By
from elements.base_element import BaseElement
from helper.locator import Locator
from pages.verify_identity_page import VerifyIdentityPage
from pages.base_page import BasePage

INVALID_PASSWORD_MESSAGE = Locator(By.ID, "loginForm-password-input-error-text")
INVALID_EMAIL_MESSAGE = Locator(By.ID, "loginForm-email-input-error-text")
INVALID_EMAIL_PASSWORD_MESSAGE = Locator(By.ID, "error-message-text")
LOGIN_BUTTON = Locator(By.ID, "loginForm-submit-button")
PASSWORD_FIELD = Locator(By.ID, "loginForm-password-input")
EMAIL_FIELD = Locator(By.ID, "loginForm-email-input")


class LoginPage(BasePage):

    def enter_email(self, email):
        logging.info(f"Enter email: '{email}'")
        BaseElement(self.driver, EMAIL_FIELD).clear_and_type(email)
        return self

    def enter_password(self, password):
        logging.info(f"Enter password: '{password}'")
        BaseElement(self.driver, PASSWORD_FIELD).clear_and_type(password)
        return self

    def click_login_button(self):
        logging.info("Click 'LOGIN' button")
        BaseElement(self.driver, LOGIN_BUTTON).click()
        return self

    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()
        return VerifyIdentityPage(self.driver)

    def get_invalid_combination_error_message(self):
        return BaseElement(self.driver, INVALID_EMAIL_PASSWORD_MESSAGE).text()

    def get_invalid_email_format_error_message(self):
        return BaseElement(self.driver, INVALID_EMAIL_MESSAGE).text()

    def get_invalid_password_format_error_message(self):
        return BaseElement(self.driver, INVALID_PASSWORD_MESSAGE).text()
