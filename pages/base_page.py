

class BasePage(object):
    def __init__(self, driver, base_url = "https://web.whatsapp.com/"):
        self.base_url = base_url
        self.driver = driver

        self.timeout = 10

        



    def find_element(self, *locator):
        return self.driver.find_element(*locator)

            