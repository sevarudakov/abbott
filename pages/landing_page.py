import logging

from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from elements.base_element import BaseElement
from elements.dropdown import Dropdown
from helper.locator import Locator
from pages.base_page import BasePage
from pages.login_page import LoginPage

ACCEPT_COOKIES = Locator(By.CSS_SELECTOR, "button.trustarc-acceptall-btn")
SELECT_COUNTRY = Locator(By.ID, "country-select")
SELECT_LANGUAGE = Locator(By.ID, "language-select")
SUBMIT_BUTTON = Locator(By.ID, "submit-button")


class LandingPage(BasePage):
    url = "https://libreview.com"

    def accept_cookies_if_present(self):
        logging.info("Accepting cookies")
        try:
            BaseElement(self.driver, ACCEPT_COOKIES).click()
        except NoSuchElementException:
            logging.info("Cookie banner not found")
        except TimeoutException:
            logging.info("Accept cookies button not found")
        return self

    def select_country(self, country):
        logging.info(f"Select country: '{country}'")
        element = Dropdown(self.driver, SELECT_COUNTRY)
        element.select_by_visible_text(country)
        return self

    def select_language(self, language):
        logging.info(f"Select language: '{language}'")
        element = Dropdown(self.driver, SELECT_LANGUAGE)
        element.select_by_visible_text(language)
        return self

    def click_submit_button(self):
        logging.info(f"Click 'SUBMIT' button")
        BaseElement(self.driver, SUBMIT_BUTTON).click()
        return LoginPage(self.driver)
