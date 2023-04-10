from elements.base_element import BaseElement
from selenium.webdriver.support.ui import Select


class Dropdown(BaseElement):
    def __init__(self, driver, locator):
        super().__init__(driver, locator)
        self.select = Select(self.web_element)

    def select_by_visible_text(self, text):
        self.select.select_by_visible_text(text)

    def select_by_value(self, value):
        self.select.select_by_value(value)

    def select_by_index(self, index):
        self.select.select_by_index(index)
