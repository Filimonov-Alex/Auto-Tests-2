from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datafortests import target


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def go_to_site(self):
        self.driver.get(target)
