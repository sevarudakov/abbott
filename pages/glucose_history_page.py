from selenium.webdriver.common.by import By

from elements.base_element import BaseElement
from helper.locator import Locator
from pages.base_page import BasePage
from pages.upload_device_page import UploadDevicePage

UPLOAD_DEVICE_BUTTON = Locator(By.ID, "uploadCard-upload-button")


class GlucoseHistoryPage(BasePage):

    def is_upload_device_button_enabled(self):
        return BaseElement(self.driver, UPLOAD_DEVICE_BUTTON).is_enabled()

    def navigate_to_upload_device_page(self):
        BaseElement(self.driver, UPLOAD_DEVICE_BUTTON).click()
        return UploadDevicePage(self.driver)
