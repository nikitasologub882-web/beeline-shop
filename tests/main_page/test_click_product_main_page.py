from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

print("Тест: клик по товару открывает карточку")
driver.get("https://moskva.beeline.ru/shop/")
time.sleep(3)

current_url = driver.current_url

print("Кликаем по первому товару")
driver.find_element("class name", "styles_module_img-container__c_wVl").click()
time.sleep(3)

print("Текущий URL:", driver.current_url)
assert "/shop/details/" in driver.current_url, "Карточка товара не открылась"
print("Проверка пройдена ✅")
time.sleep(5)
driver.quit()