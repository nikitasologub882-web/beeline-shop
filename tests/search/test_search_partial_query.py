# Проверка: поиск работает при частичном вводе
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

    # ввести часть слова
    driver.switch_to.active_element.send_keys("ipho")
    time.sleep(3)

    # найти результаты поиска
    results = driver.find_elements(By.XPATH, "//a[@data-t-id='components-Cell']")

    # проверить что результаты появились
    assert len(results) > 0, "Поиск не работает по частичному вводу"

    time.sleep(3)

finally:
    driver.quit()