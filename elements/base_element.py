class BaseElement(object):
    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator
        self.web_element = None
        self.find()

    def find(self):
        self.web_element = self.driver.find_element(*self.locator)
        return self.web_element

    def click(self):
        self.find().click()
        return None

    def is_enabled(self):
        return self.web_element.is_enabled()

    def type(self, text):
        self.web_element.send_keys(text)
        return None

    def clear_and_type(self, text):
        self.web_element.clear()
        self.web_element.send_keys(text)
        return None

    def attribute(self, attr_name):
        return self.web_element.get_attribute(attr_name)

    def text(self):
        return self.web_element.text
