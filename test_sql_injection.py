import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datafortests import sql_injections
from PageObject import LoginPage


@pytest.mark.parametrize("login, password",
                         sql_injections
                         )
def test_sql_injection(init_browser, login, password):
    print("Тестирование на защиту от sql-инъекций:")
    login_page = LoginPage()
    login_page.go_to_site
    assert login_page.opened, "Страница авторизации закрыта"
    print("Страница авторизации открыта")
    login_page.enter_login(login)
    login_page.enter_password(password)
    login_page.btn_click
    print("Данные загружены в форму и отправлены на сервер")
    if login_page.opened:
        print(
            f"Для SQL-инъекции {login}/{password} сработала защита, аутентификация не прошла.")
    else:
        print(
            f"Для SQL-инъекции {login}/{password} атака прошла успешно. Произошла аутентификация")
