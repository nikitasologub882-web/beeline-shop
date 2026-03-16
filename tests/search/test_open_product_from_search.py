# Проверка: из поиска можно открыть карточку товара
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()

try:
    # открыть сайт
    driver.get("https://moskva.beeline.ru/shop/")
    time.sleep(3)

    # открыть поиск
    driver.find_element(By.XPATH, "//button[@aria-label='Открыть поиск']").click()
    time.sleep(2)

    # ввести поисковый запрос
    driver.switch_to.active_element.send_keys("iphone")
    time.sleep(3)

    # кликнуть первый результат
    first_result = driver.find_element(By.XPATH, "(//a[@data-t-id='components-Cell'])[1]")
    first_result.click()
    time.sleep(3)

    # проверить что открылась карточка товара
    assert "/shop/details/" in driver.current_url, "Карточка товара не открылась"

    time.sleep(3)

finally:
    driver.quit()