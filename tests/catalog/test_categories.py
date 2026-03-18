from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# time нужен для небольших пауз при медленной загрузке сайта
import time

# URL КАТЕГОРИЙ
SMARTPHONES_URL = "https://moskva.beeline.ru/shop/catalog/telefony/smartfony/"
TABLETS_URL = "https://moskva.beeline.ru/shop/catalog/planshety/planshety-3/"
HEADPHONES_URL = "https://moskva.beeline.ru/shop/catalog/audio/naushniki/"

# ЛОКАТОРЫ
# Все карточки товаров в каталоге
PRODUCT_CARDS = (
    By.XPATH,
    "//div[@data-t-id='components-Device']")

# Название товара внутри карточки
PRODUCT_NAME_IN_CARD = (
    By.XPATH,
    ".//a[contains(@href, '/shop/details/')]/p")

print("Тест: категории каталога открываются по прямым ссылкам и отображают товары")
# ЗАПУСК БРАУЗЕРА
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()
# Увеличиваем ожидание полной загрузки страницы
driver.set_page_load_timeout(60)
# Увеличиваем явное ожидание элементов
wait = WebDriverWait(driver, 30)

try:
    # 1. ПРОВЕРЯЕМ КАТЕГОРИЮ "СМАРТФОНЫ"
    print("Открываем категорию: Смартфоны")
    driver.get(SMARTPHONES_URL)
    time.sleep(2)
    wait.until(EC.url_contains("/shop/catalog/telefony/smartfony/"))

    smartphone_cards = wait.until(
        EC.presence_of_all_elements_located(PRODUCT_CARDS))
    print(f"В категории 'Смартфоны' найдено карточек: {len(smartphone_cards)}")
    assert len(smartphone_cards) > 0, "В категории 'Смартфоны' не отображаются товары"
    first_smartphone = smartphone_cards[0].find_element(*PRODUCT_NAME_IN_CARD).text.strip()
    print(f"Первый товар в категории 'Смартфоны': {first_smartphone}")
    assert first_smartphone != "", "У первого товара в категории 'Смартфоны' нет названия"

    # 2. ПРОВЕРЯЕМ КАТЕГОРИЮ "ПЛАНШЕТЫ"
    print("Открываем категорию: Планшеты")
    driver.get(TABLETS_URL)
    time.sleep(2)
    wait.until(EC.url_contains("/shop/catalog/planshety/planshety-3/"))
    tablet_cards = wait.until(
        EC.presence_of_all_elements_located(PRODUCT_CARDS))
    print(f"В категории 'Планшеты' найдено карточек: {len(tablet_cards)}")
    assert len(tablet_cards) > 0, "В категории 'Планшеты' не отображаются товары"
    first_tablet = tablet_cards[0].find_element(*PRODUCT_NAME_IN_CARD).text.strip()
    print(f"Первый товар в категории 'Планшеты': {first_tablet}")
    assert first_tablet != "", "У первого товара в категории 'Планшеты' нет названия"

    # 3. ПРОВЕРЯЕМ КАТЕГОРИЮ "НАУШНИКИ И КОЛОНКИ"
    print("Открываем категорию: Наушники и колонки")
    driver.get(HEADPHONES_URL)
    time.sleep(2)
    wait.until(EC.url_contains("/shop/catalog/audio/naushniki/"))
    headphones_cards = wait.until(
        EC.presence_of_all_elements_located(PRODUCT_CARDS))
    print(f"В категории 'Наушники и колонки' найдено карточек: {len(headphones_cards)}")
    assert len(headphones_cards) > 0, "В категории 'Наушники и колонки' не отображаются товары"
    first_headphones = headphones_cards[0].find_element(*PRODUCT_NAME_IN_CARD).text.strip()
    print(f"Первый товар в категории 'Наушники и колонки': {first_headphones}")
    assert first_headphones != "", "У первого товара в категории 'Наушники и колонки' нет названия"

    # 4. ДОПОЛНИТЕЛЬНАЯ ПРОВЕРКА
    assert first_smartphone != first_tablet, (
        "Категории 'Смартфоны' и 'Планшеты' показывают одинаковый первый товар")
    print("Проверка пройдена: категории открываются и отображают разный контент")

finally:
    driver.quit()