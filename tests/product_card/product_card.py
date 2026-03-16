import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Устанавливаем и запускаем ChromeDriver
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# Переходим на страницу каталога смартфонов
driver.get("https://moskva.beeline.ru/shop/catalog/telefony/smartfony/")
time.sleep(3)

# ЛОКАТОРЫ
# Ссылка на первый товар в каталоге
FIRST_PRODUCT_LINK = (
    "xpath",
    "((//div[@data-t-id='components-Device'])[1]//a[contains(@href, '/shop/details/')])[1]"
)

# Название первого товара в каталоге
CATALOG_PRODUCT_NAME = (
    "xpath",
    "((//div[@data-t-id='components-Device'])[1]//a[contains(@href, '/shop/details/')]//p)[1]"
)

# Заголовок товара на странице карточки
PRODUCT_CARD_TITLE = (
    "xpath",
    "//h1"
)

# Кнопка добавления товара в корзину
ADD_TO_CART_BUTTON = (
    "xpath",
    "//button[.//span[contains(text(),'В корзину')]]"
)

# ФУНКЦИЯ ОТКРЫТИЯ КАРТОЧКИ ТОВАРА
def open_first_product_card():

    # Переходим в каталог смартфонов
    driver.get("https://moskva.beeline.ru/shop/catalog/telefony/smartfony/")
    time.sleep(3)

    # Находим первый товар в каталоге
    first_product = driver.find_element(*FIRST_PRODUCT_LINK)

    # Кликаем по товару для открытия карточки
    first_product.click()
    time.sleep(3)

# ----------------------------
# ТЕСТ 1
# Проверка: из каталога можно открыть карточку товара

print("Тест 1: Открытие карточки товара")
# Открываем карточку первого товара
open_first_product_card()

# Выводим текущий URL страницы
print("Текущий URL:", driver.current_url)

# Проверяем, что URL содержит адрес страницы товара
assert "/shop/details/" in driver.current_url, "Карточка товара не открылась"
print("Результат: карточка товара успешно открылась")
time.sleep(2)

# ----------------------------
# ТЕСТ 2
# Проверка: в карточке товара отображается название товара

print("\nТест 2: Проверка отображения названия товара")
# Открываем карточку товара
open_first_product_card()

# Находим заголовок товара
title = driver.find_element(*PRODUCT_CARD_TITLE)

# Получаем текст названия
title_text = title.text.strip()
print("Название товара:", title_text)

# Проверяем, что элемент названия отображается
assert title.is_displayed(), "Название товара не отображается"

# Проверяем, что текст названия не пустой
assert title_text != "", "Название товара пустое"
print("Результат: название товара отображается")
time.sleep(2)

# ----------------------------
# ТЕСТ 3
# Проверка: название товара в каталоге совпадает с названием в карточке товара

print("\nТест 3: Проверка совпадения названия товара")
# Открываем каталог смартфонов
driver.get("https://moskva.beeline.ru/shop/catalog/telefony/smartfony/")
time.sleep(3)

# Получаем название первого товара в каталоге
catalog_name = driver.find_element(*CATALOG_PRODUCT_NAME).text.strip()
print("Название в каталоге:", catalog_name)

# Открываем карточку этого товара
open_first_product_card()

# Получаем название товара в карточке
card_name = driver.find_element(*PRODUCT_CARD_TITLE).text.strip()
print("Название в карточке:", card_name)

# Проверяем, что названия не пустые
assert catalog_name != "", "Название товара в каталоге пустое"
assert card_name != "", "Название товара в карточке пустое"

# Проверяем совпадение названий
assert (
    catalog_name in card_name or card_name in catalog_name
), "Название товара в каталоге и карточке не совпадает"
print("Результат: названия совпадают")
time.sleep(2)

# ----------------------------
# ТЕСТ 4
# Проверка: в карточке товара отображается кнопка "В корзину"

print("\nТест 4: Проверка кнопки 'В корзину'")
# Открываем карточку товара
open_first_product_card()

# Находим кнопку добавления в корзину
button = driver.find_element(*ADD_TO_CART_BUTTON)

# Проверяем, что кнопка отображается
assert button.is_displayed(), "Кнопка 'В корзину' не отображается"
print("Результат: кнопка 'В корзину' отображается")
time.sleep(2)

# Закрываем браузер
driver.quit()