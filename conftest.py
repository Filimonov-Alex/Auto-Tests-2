import pytest
from selenium import webdriver


@pytest.fixture()
def init_browser(scope="session"):
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()
    return driver
