# Импорт webdriver для управления браузером
from selenium import webdriver

# Импорт By для работы с локаторами
from selenium.webdriver.common.by import By

# Service нужен для запуска ChromeDriver
from selenium.webdriver.chrome.service import Service

# webdriver-manager автоматически подбирает и скачивает ChromeDriver
from webdriver_manager.chrome import ChromeDriverManager

# WebDriverWait нужен для явных ожиданий
from selenium.webdriver.support.ui import WebDriverWait

# expected_conditions содержит готовые условия ожиданий
from selenium.webdriver.support import expected_conditions as EC


# =========================
# ЛОКАТОРЫ
# =========================

# Ссылка на категорию "Смартфоны" на главной странице
SMARTPHONES_CATEGORY_LINK = (
    By.XPATH,
    "//a[@href='/shop/catalog/telefony/smartfony/']"
)

# Все карточки товаров в каталоге
PRODUCT_CARDS = (
    By.XPATH,
    "//div[@data-t-id='components-Device']"
)

# Название товара внутри карточки
# Ищем внутри конкретной карточки, поэтому xpath относительный
PRODUCT_NAME_IN_CARD = (
    By.XPATH,
    ".//a[contains(@href, '/shop/details/')]/p"
)

# Кнопка пагинации "2"
PAGINATION_BUTTON_2 = (
    By.XPATH,
    "//button[@data-t-id='src-Pagination'][.//span[text()='2']]"
)

# Активная кнопка пагинации "2"
# У активной страницы появляется дополнительный класс active
ACTIVE_PAGE_2 = (
    By.XPATH,
    "//button[@data-t-id='src-Pagination' and contains(@class, 'active')][.//span[text()='2']]"
)


print("Тест: переход между страницами каталога работает корректно")


# =========================
# ЗАПУСК БРАУЗЕРА
# =========================

# Устанавливаем и запускаем ChromeDriver
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Открываем браузер на весь экран
driver.maximize_window()

# Создаем объект явного ожидания
wait = WebDriverWait(driver, 15)


try:
    # =========================
    # 1. ОТКРЫВАЕМ ГЛАВНУЮ СТРАНИЦУ
    # =========================

    driver.get("https://moskva.beeline.ru/shop/")



    # =========================
    # 2. ПЕРЕХОДИМ В КАТАЛОГ СМАРТФОНОВ
    # =========================

    print("Открываем каталог смартфонов")

    smartphones_link = wait.until(
        EC.element_to_be_clickable(SMARTPHONES_CATEGORY_LINK)
    )
    smartphones_link.click()



    # =========================
    # 3. ЖДЕМ ЗАГРУЗКУ ТОВАРОВ НА ПЕРВОЙ СТРАНИЦЕ
    # =========================

    cards_page_1 = wait.until(
        EC.presence_of_all_elements_located(PRODUCT_CARDS)
    )

    print(f"На первой странице найдено товаров: {len(cards_page_1)}")

    # Проверяем, что товары действительно появились
    assert len(cards_page_1) > 0, "На первой странице каталога нет товаров"



    # =========================
    # 4. ЗАПОМИНАЕМ ПЕРВЫЙ ТОВАР НА ПЕРВОЙ СТРАНИЦЕ
    # =========================

    first_product_page_1 = cards_page_1[0].find_element(*PRODUCT_NAME_IN_CARD).text.strip()

    print(f"Первый товар на странице 1: {first_product_page_1}")

    # Дополнительная проверка на случай пустого названия
    assert first_product_page_1 != "", "У первого товара на странице 1 отсутствует название"



    # =========================
    # 5. ПЕРЕХОДИМ НА ВТОРУЮ СТРАНИЦУ КАТАЛОГА
    # =========================

    print("Переходим на страницу 2")

    # Сначала просто ждем появления кнопки пагинации "2" в DOM
    page_2_button = wait.until(
        EC.presence_of_element_located(PAGINATION_BUTTON_2)
    )

    # Прокручиваем страницу к кнопке, чтобы Selenium мог с ней взаимодействовать
    driver.execute_script("arguments[0].scrollIntoView(true);", page_2_button)

    # После скролла ждем, пока кнопка станет кликабельной
    page_2_button = wait.until(
        EC.element_to_be_clickable(PAGINATION_BUTTON_2)
    )

    # Кликаем по странице "2"
    page_2_button.click()



    # =========================
    # 6. ЖДЕМ, ЧТО СТРАНИЦА 2 СТАНЕТ АКТИВНОЙ
    # =========================

    wait.until(
        EC.presence_of_element_located(ACTIVE_PAGE_2)
    )

    print("Страница 2 стала активной")



    # =========================
    # 7. ЖДЕМ ЗАГРУЗКУ ТОВАРОВ НА ВТОРОЙ СТРАНИЦЕ
    # =========================

    # Ждем, пока первый товар на странице изменится
    # Это нужно, чтобы убедиться, что контент реально обновился,
    # а не просто произошел клик по пагинации
    wait.until(
        lambda d: d.find_elements(*PRODUCT_CARDS)[0]
        .find_element(*PRODUCT_NAME_IN_CARD)
        .text.strip() != first_product_page_1
    )

    # После обновления страницы заново получаем список карточек
    cards_page_2 = driver.find_elements(*PRODUCT_CARDS)

    print(f"На второй странице найдено товаров: {len(cards_page_2)}")

    # Проверяем, что после перехода товары есть
    assert len(cards_page_2) > 0, "На второй странице каталога нет товаров"



    # =========================
    # 8. ПОЛУЧАЕМ ПЕРВЫЙ ТОВАР НА ВТОРОЙ СТРАНИЦЕ
    # =========================

    first_product_page_2 = cards_page_2[0].find_element(*PRODUCT_NAME_IN_CARD).text.strip()

    print(f"Первый товар на странице 2: {first_product_page_2}")

    # Проверяем, что название товара не пустое
    assert first_product_page_2 != "", "У первого товара на странице 2 отсутствует название"



    # =========================
    # 9. СРАВНИВАЕМ ПЕРВЫЙ ТОВАР ДО И ПОСЛЕ ПЕРЕХОДА
    # =========================

    assert first_product_page_1 != first_product_page_2, (
        "После перехода на страницу 2 первый товар не изменился"
    )

    print("Проверка пройдена: пагинация работает, страница и товары обновились")


finally:
    # Закрываем браузер в любом случае
    driver.quit()