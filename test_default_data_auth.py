import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datafortests import default_auth_info
from PageObject import LoginPage


@pytest.mark.parametrize("login, password",
                         default_auth_info
                         )
def test_default_data_auth(init_browser, login, password):
    print("Тестирование на использование учетных данных по умолчанию:")
    login_page = LoginPage(driver)
    login_page.go_to_site
    assert login_page.opened, "Страница авторизации закрыта"
    print("Страница авторизации открыта")
    login_page.enter_login(login)
    login_page.enter_password(password)
    login_page.btn_click
    print("Данные загружены в форму и отправлены на сервер")
    if login_page.opened:
        print(f"Для пары значений по умолчанию: {
              login}/{password} аутентификация не произошла.")
    else:
        print(f"Для пары значений по умолчанию {
              login}/{password} произошла аутентификация.")
