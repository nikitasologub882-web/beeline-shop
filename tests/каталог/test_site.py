# Импорт фреймворка для тестирования pytest
import pytest
# Импорт Selenium WebDriver для управления браузером
from selenium import webdriver
# Импорт классов для поиска элементов (By.ID, By.CLASS_NAME, By.XPATH и т.д.)
from selenium.webdriver.common.by import By
# Импорт класса WebDriverWait для создания явных ожиданий
from selenium.webdriver.support.ui import WebDriverWait
# Импорт expected_conditions (сокращенно EC) для предопределенных условий ожидания
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture()
def browser():
    browser = webdriver.Chrome()
    browser.maximize_window()
    yield browser
    browser.quit()

def test_open_honor_X7c(browser):
    browser.get("https://moskva.beeline.ru/shop/")
    # Создание объекта ожидания с таймаутом 10 секунд
    wait = WebDriverWait(browser, 10)
    # Ожидание появления элемента с указанным классом на странице
    # EC.presence_of_element_located - условие "элемент присутствует в DOM"
    # (By.CLASS_NAME, "styles_img-container__psRuR") - локатор для поиска по классу
    honor_X7c = (wait.until
                 (EC.presence_of_element_located((By.CLASS_NAME, "styles_img-container__psRuR"))))
    # Клик по найденному элементу для перехода на страницу товара
    honor_X7c.click()

    # Поиск заголовка h1 на странице товара после клика
    # By.TAG_NAME - поиск по имени тега HTML (h1, div, span, a и т.д.)
    title = browser.find_element(By.TAG_NAME, "h1")
    # Вывод текста заголовка в консоль для отладки
    print(f"Заголовок страницы: {title.text}")




