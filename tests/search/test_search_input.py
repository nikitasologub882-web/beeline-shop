# Проверка: поле поиска принимает ввод
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

    # ввести текст в поле поиска
    search_input = driver.switch_to.active_element
    search_input.send_keys("iphone")

    # проверить что текст появился в поле
    assert search_input.get_attribute("value") == "iphone", "Текст не появился в поле поиска"

    time.sleep(3)

finally:
    driver.quit()