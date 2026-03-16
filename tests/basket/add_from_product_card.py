# Добавление товара в корзину из карточки товара
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# ЛОКАТОРЫ
FIRST_PRODUCT_LINK = ("xpath","((//div[@data-t-id='components-Device'])[1]//a[contains(@href, '/shop/details/')])[1]")
ADD_TO_BASKET_FROM_PRODUCT_CARD = ("xpath","//button[@data-t-id='src-Button'][.//span[text()='В корзину']]")
BASKET_BUTTON = ("xpath","//span[contains(@style,'IconBasketFilled')]/ancestor::button")

print("Тест: добавление товара в корзину из карточки товара")
# 1. Открываем каталог смартфонов
driver.get("https://moskva.beeline.ru/shop/catalog/telefony/smartfony/")
time.sleep(3)

# 2. Открываем карточку первого товара
driver.find_element(*FIRST_PRODUCT_LINK).click()
time.sleep(3)

# 3. Нажимаем кнопку "В корзину" на карточке товара
driver.find_element(*ADD_TO_BASKET_FROM_PRODUCT_CARD).click()
time.sleep(2)

# 4. Открываем корзину
driver.find_element(*BASKET_BUTTON).click()
time.sleep(3)

# 5. Проверяем, что открылась корзина
assert "/basket" in driver.current_url, "Корзина не открылась после добавления товара из карточки"
print("Результат: товар успешно добавлен в корзину из карточки товара")

driver.quit()