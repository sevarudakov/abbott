from selenium.webdriver.common.by import By
from elements.base_element import BaseElement
from helper.locator import Locator
from pages.base_page import BasePage

PRESS_TO_BEGIN_UPLOAD_BUTTON = Locator(By.ID, "meterUpload-linkedUpload-pat-button")


class UploadDevicePage(BasePage):

    def is_press_to_begin_upload_button_enabled(self):
        return BaseElement(self.driver, PRESS_TO_BEGIN_UPLOAD_BUTTON).is_enabled()
