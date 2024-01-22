import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from basepage import BasePage
from datafortests import target


class LoginPage(BasePage):

    def __init__(self, driver):
        self.driver = driver

    def enter_login(self, login):
        self.driver.find_element(By.ID, "uid").send_keys(login)

    def enter_password(self, password):
        self.driver.find_element(By.ID, "passw").send_keys(password)

    def btn_click(self):
        self.driver.find_element(By.NAME, "btnSubmit").click()

    def opened(self):
        if self.driver.current_url == target:
            True
        else:
            False
