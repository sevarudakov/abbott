import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import conftest

LOADING_LOGO = By.CSS_SELECTOR, ".pg-loading-logo"


class BasePage(object):
    url = None

    def __init__(self, driver):
        self.driver = driver

    def go(self):
        logging.info(f"Open url: {self.url}")
        self.driver.get(self.url)
        self.driver.implicitly_wait(0)
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located(LOADING_LOGO))
        self.driver.implicitly_wait(conftest.IMPLICIT_WAIT_TIME)
        return self
