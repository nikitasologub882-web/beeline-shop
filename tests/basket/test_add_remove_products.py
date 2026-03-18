import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# Устанавливаем и запускаем ChromeDriver
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()


# ЛОКАТОРЫ
# Кнопка "В корзину" у первого товара в каталоге
ADD_TO_BASKET_BUTTON = (
    "xpath",
    "(//div[@data-t-id='components-Device'])[1]//button[.//span[text()='В корзину']]"
)

# Кнопка корзины в header
BASKET_BUTTON = (
    "xpath",
    "//span[contains(@style,'IconBasketFilled')]/ancestor::button"
)

# Кнопка увеличения количества товара (+)
PLUS_BUTTON = (
    "xpath",
    "//button[@aria-label='Добавить']"
)

# Количество товара в корзине
PRODUCT_COUNT = (
    "xpath",
    "//button[@aria-label='Добавить']/following-sibling::p"
)

# Кнопка уменьшения количества товара (-)
MINUS_BUTTON = (
    "xpath",
    "//button[@aria-label='Добавить']/following-sibling::p/following-sibling::button[@aria-label='Удалить']"
)


print("Тест: увеличение и уменьшение количества товара в корзине")

# 1. Открываем каталог смартфонов
driver.get("https://moskva.beeline.ru/shop/catalog/telefony/smartfony/")
time.sleep(3)

# 2. Добавляем первый товар в корзину
print("Добавляем первый товар в корзину")
driver.find_element(*ADD_TO_BASKET_BUTTON).click()
time.sleep(2)

# 3. Открываем корзину
print("Открываем корзину")
driver.find_element(*BASKET_BUTTON).click()
time.sleep(3)

# 4. Получаем количество товара до увеличения
count_before_increase = driver.find_element(*PRODUCT_COUNT).text
print("Количество до увеличения:", count_before_increase)

# 5. Нажимаем кнопку "+"
print("Увеличиваем количество товара")
driver.find_element(*PLUS_BUTTON).click()
time.sleep(2)

# 6. Получаем количество после увеличения
count_after_increase = driver.find_element(*PRODUCT_COUNT).text
print("Количество после увеличения:", count_after_increase)

# 7. Проверяем, что количество увеличилось
assert int(count_after_increase) > int(count_before_increase), "Количество товара не увеличилось"
print("Проверка пройдена: количество товара увеличилось")

# 8. Получаем количество до уменьшения
count_before_decrease = driver.find_element(*PRODUCT_COUNT).text
print("Количество до уменьшения:", count_before_decrease)

# 9. Нажимаем кнопку "-"
print("Уменьшаем количество товара")
driver.find_element(*MINUS_BUTTON).click()
time.sleep(2)

# 10. Получаем количество после уменьшения
count_after_decrease = driver.find_element(*PRODUCT_COUNT).text
print("Количество после уменьшения:", count_after_decrease)

# 11. Проверяем, что количество уменьшилось
assert int(count_after_decrease) < int(count_before_decrease), "Количество товара не уменьшилось"
print("Проверка пройдена: количество товара уменьшилось")

driver.quit()