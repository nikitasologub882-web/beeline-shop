import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Фикстура pytest - функция, которая выполняется перед тестом и возвращает объект браузера
@pytest.fixture()
def browser():
    # Создание экземпляра Chrome браузера
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.implicitly_wait(3)
    # Возврат браузера тестовой функции (до этой строки выполняется ДО теста)
    yield browser
    browser.quit()

def test_planshet(browser):
    browser.get("https://moskva.beeline.ru/shop/")
    planshet_link = browser.find_element(By.CSS_SELECTOR, ".styles_component__geONH.styles_active__P_ZXe")
    planshet_link.click()
    time.sleep(3)
    planshet = browser.find_elements(By.CSS_SELECTOR, ".styles_img-container__psRuR")
    assert len(planshet) == 20
