import logging
from selenium.webdriver.common.by import By
from elements.base_element import BaseElement
from helper.locator import Locator
from pages.base_page import BasePage
from pages.glucose_history_page import GlucoseHistoryPage

SECURITY_CODE_ERROR_MESSAGE = Locator(By.ID, "twoFactor-step2-code-input-error-text")
VERIFY_AND_LOGIN_BUTTON = Locator(By.ID, "twoFactor-step2-next-button")
VERIFICATION_CODE_FIELD = Locator(By.ID, "twoFactor-step2-code-input")
SEND_CODE_BUTTON = Locator(By.ID, "twoFactor-step1-next-button")


class VerifyIdentityPage(BasePage):
    def click_send_code_button(self):
        logging.info(f"Click 'SEND CODE' button")
        BaseElement(self.driver, SEND_CODE_BUTTON).click()
        return self

    def enter_verification_code(self, code):
        logging.info(f"Enter verification code '{code}'")
        BaseElement(self.driver, VERIFICATION_CODE_FIELD).type(code)
        return self

    def is_verify_and_login_button_enabled(self):
        return BaseElement(self.driver, VERIFY_AND_LOGIN_BUTTON).is_enabled()

    def click_verify_and_login_button(self):
        logging.info(f"Click 'VERIFY AND LOGIN' button")
        BaseElement(self.driver, VERIFY_AND_LOGIN_BUTTON).click()
        return GlucoseHistoryPage(self.driver)

    def get_security_code_error_message(self):
        return BaseElement(self.driver, SECURITY_CODE_ERROR_MESSAGE).text()
