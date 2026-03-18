# Импорт библиотек Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
# Импорт ожиданий
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# ЛОКАТОРЫ
# Ссылка на категорию смартфонов
SMARTPHONES_CATEGORY_LINK = (By.XPATH,
    "//a[@href='/shop/catalog/telefony/smartfony/']")
# Карточки товаров в каталоге
PRODUCT_CARDS = (By.XPATH,
    "//div[@data-t-id='components-Device']")
# Ссылка товара внутри карточки
PRODUCT_LINK_IN_CARD = (By.XPATH,
    ".//a[contains(@href, '/shop/details/')]")
# Заголовок товара на странице карточки
PRODUCT_TITLE = (By.XPATH,
    "//h1[@itemprop='name']")

print("Тест: переход из каталога в карточку товара")
# ЗАПУСК БРАУЗЕРА
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()
wait = WebDriverWait(driver, 15)

try:
    # 1. ОТКРЫВАЕМ ГЛАВНУЮ СТРАНИЦУ
    driver.get("https://moskva.beeline.ru/shop/")
    # 2. ПЕРЕХОДИМ В КАТАЛОГ СМАРТФОНОВ
    print("Открываем каталог смартфонов")
    smartphones = wait.until(
        EC.element_to_be_clickable(SMARTPHONES_CATEGORY_LINK))
    smartphones.click()

    # 3. ЖДЕМ ПОЯВЛЕНИЯ ТОВАРОВ
    cards = wait.until(
        EC.presence_of_all_elements_located(PRODUCT_CARDS))
    print(f"Найдено товаров: {len(cards)}")

    # 4. БЕРЕМ ПЕРВУЮ КАРТОЧКУ ТОВАРА
    first_card = cards[0]

    # Находим ссылку товара внутри карточки
    product_link = first_card.find_element(*PRODUCT_LINK_IN_CARD)
    product_name = product_link.text
    print(f"Открываем товар: {product_name}")

    # 5. ПЕРЕХОД В КАРТОЧКУ ТОВАРА
    product_link.click()

    # 6. ПРОВЕРЯЕМ ЧТО ОТКРЫЛАСЬ СТРАНИЦА ТОВАРА
    wait.until(EC.url_contains("/shop/details/"))
    print("Открылась страница товара")

    # 7. ПРОВЕРЯЕМ НАЛИЧИЕ НАЗВАНИЯ ТОВАРА
    title = wait.until(
        EC.visibility_of_element_located(PRODUCT_TITLE))
    product_title = title.text
    print(f"Название товара на странице: {product_title}")

    # Проверяем что заголовок не пустой
    assert product_title.strip() != "", "Название товара не отображается"
    print("Проверка пройдена: переход из каталога в карточку товара работает")

finally:
    driver.quit()