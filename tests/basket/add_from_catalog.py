# Добавление товара в корзину из каталога
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# ЛОКАТОРЫ
ADD_TO_BASKET_FROM_CATALOG = ("xpath","(//div[@data-t-id='components-Device'])[1]//button[.//span[text()='В корзину']]")
PRODUCT_IN_BASKET_IN_CATALOG = ("xpath","(//div[@data-t-id='components-Device'])[1]//button[.//span[text()='В корзине']]")

print("Тест: добавление товара в корзину из каталога")
# 1. Открываем каталог смартфонов
driver.get("https://moskva.beeline.ru/shop/catalog/telefony/smartfony/")
time.sleep(3)

# 2. Нажимаем кнопку "В корзину" у первого товара
driver.find_element(*ADD_TO_BASKET_FROM_CATALOG).click()
time.sleep(2)

# 3. Проверяем, что товар теперь в корзине
button_in_basket = driver.find_element(*PRODUCT_IN_BASKET_IN_CATALOG)
assert button_in_basket.is_displayed(), "После добавления товара кнопка 'В корзине' не отображается"
print("Результат: товар успешно добавлен в корзину из каталога")

driver.quit()