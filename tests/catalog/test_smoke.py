# Импортируем webdriver для управления браузером
from selenium import webdriver
# Импортируем By — используется для указания типа локатора (xpath, css и т.д.)
from selenium.webdriver.common.by import By
# Service нужен для запуска ChromeDriver
from selenium.webdriver.chrome.service import Service
# webdriver-manager автоматически скачивает подходящую версию ChromeDriver
from webdriver_manager.chrome import ChromeDriverManager
# WebDriverWait используется для ожидания появления элементов
from selenium.webdriver.support.ui import WebDriverWait
# expected_conditions содержит условия ожиданий (клик, появление элемента и т.д.)
from selenium.webdriver.support import expected_conditions as EC

# ЛОКАТОРЫ
# Ссылка на категорию "Смартфоны" на главной странице
# Используем href, так как он стабильнее динамических классов
SMARTPHONES_CATEGORY_LINK = (By.XPATH,
    "//a[@href='/shop/catalog/telefony/smartfony/']")

# Все карточки товаров в каталоге
# data-t-id='components-Device' — стабильный атрибут карточки товара
PRODUCT_CARDS = (By.XPATH,
    "//div[@data-t-id='components-Device']")

# Название товара внутри карточки
# Используем относительный xpath (начинается с .//)
# чтобы искать элемент внутри конкретной карточки
PRODUCT_NAME_IN_CARD = (By.XPATH,
    ".//a[contains(@href, '/shop/details/')]/p")

# Цена товара внутри карточки
# Проверяем наличие символа рубля ₽
PRODUCT_PRICE_IN_CARD = (By.XPATH,
    ".//div[contains(@class, 'styles_price-wrapper')]//p[contains(text(), '₽')]")

print("Тест: каталог смартфонов открывается и отображает товары")
# ЗАПУСК БРАУЗЕРА
# webdriver-manager скачивает нужный ChromeDriver
# и передает путь в Service
service = Service(executable_path=ChromeDriverManager().install())

# Запускаем браузер Chrome
driver = webdriver.Chrome(service=service)

# Разворачиваем окно браузера на весь экран
# чтобы элементы интерфейса не скрывались адаптивной версткой
driver.maximize_window()

# Создаем объект ожиданий
# максимальное ожидание любого элемента — 15 секунд
wait = WebDriverWait(driver, 15)


try:
    # 1. ОТКРЫВАЕМ ГЛАВНУЮ СТРАНИЦУ МАГАЗИНА
    driver.get("https://moskva.beeline.ru/shop/")
    # 2. ПЕРЕХОДИМ В КАТАЛОГ СМАРТФОНОВ
    print("Открываем раздел 'Смартфоны'")
    # Ждем пока ссылка станет кликабельной
    # (элемент появился и доступен для клика)
    smartphones_link = wait.until(
        EC.element_to_be_clickable(SMARTPHONES_CATEGORY_LINK))
    # Кликаем по категории
    smartphones_link.click()
    # 3. ПРОВЕРЯЕМ ЧТО ОТКРЫЛАСЬ НУЖНАЯ СТРАНИЦА
    # Ожидаем пока URL страницы изменится
    # и будет содержать путь каталога смартфонов
    wait.until(EC.url_contains("/shop/catalog/telefony/smartfony/"))
    print("Раздел смартфонов успешно открыт")

    # 4. ОЖИДАЕМ ПОЯВЛЕНИЯ КАРТОЧЕК ТОВАРОВ
    # presence_of_all_elements_located
    # означает что элементы появились в DOM
    # (они могут быть еще не видимы, но уже существуют)
    cards = wait.until(
        EC.presence_of_all_elements_located(PRODUCT_CARDS))

    # 5. ПРОВЕРЯЕМ ЧТО ТОВАРЫ ОТОБРАЗИЛИСЬ
    print(f"Найдено карточек товаров: {len(cards)}")
    # Если карточек нет — тест должен упасть
    assert len(cards) > 0, "Карточки товаров не отображаются"

    # 6. ПРОВЕРЯЕМ ДАННЫЕ ПЕРВОГО ТОВАРА
    # Берем первую карточку из списка
    first_card = cards[0]

    # Получаем название товара
    # * означает распаковку локатора (By.XPATH, xpath)
    product_name = first_card.find_element(*PRODUCT_NAME_IN_CARD).text

    # Получаем цену товара
    product_price = first_card.find_element(*PRODUCT_PRICE_IN_CARD).text

    # Выводим информацию в консоль
    print(f"Первый товар: {product_name}")
    print(f"Цена первого товара: {product_price}")

    # 7. ПРОВЕРКИ ДАННЫХ ТОВАРА
    # Проверяем что название товара не пустое
    assert product_name.strip() != "", "У товара отсутствует название"

    # Проверяем что цена содержит символ рубля
    assert "₽" in product_price, "У товара отсутствует цена или неверный формат цены"
    print("Проверка пройдена: каталог открылся и товары отображаются корректно")

finally:
    driver.quit()