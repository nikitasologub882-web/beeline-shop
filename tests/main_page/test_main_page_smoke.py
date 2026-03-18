from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

print("Тест 1: главная страница открывается")
driver.get("https://moskva.beeline.ru/shop/")
time.sleep(3)

assert "/shop/" in driver.current_url, "Главная страница не открылась"
print("URL:", driver.current_url)
print("Проверка пройдена ✅")


print("\nТест 2: заголовок страницы корректный")
print("Title:", driver.title)

assert "билайн" in driver.title.lower(), "Заголовок страницы некорректный"
print("Проверка пройдена ✅")


print("\nТест 3: логотип отображается")
logo = driver.find_elements(By.XPATH, "//img[contains(@alt, 'билайн')]")

print("Найдено логотипов:", len(logo))
assert len(logo) > 0, "Логотип не найден"
print("Проверка пройдена ✅")


print("\nТест 4: на главной есть товары")
products = driver.find_elements(By.XPATH, "//a[contains(@href, '/shop/details/')]")

print("Найдено товаров:", len(products))
assert len(products) > 0, "На главной нет товаров"
print("Проверка пройдена ✅")


print("\nТест 5: категории отображаются")
categories = driver.find_elements(By.XPATH, "//a[contains(@href, '/shop/catalog/')]")

print("Найдено категорий:", len(categories))
assert len(categories) > 0, "Категории не отображаются"
print("Проверка пройдена ✅")


print("\nТест 6: страница не пустая")
body_text = driver.find_element(By.TAG_NAME, "body").text

print("Длина текста страницы:", len(body_text))
assert len(body_text) > 100, "Страница выглядит пустой"
print("Проверка пройдена ✅")


print("\nТест 7: страница прокручивается")
start_scroll = driver.execute_script("return window.pageYOffset;")

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)

end_scroll = driver.execute_script("return window.pageYOffset;")

print("Скролл был:", start_scroll, "→", end_scroll)
assert end_scroll > start_scroll, "Страница не прокручивается"
print("Проверка пройдена ✅")


print("\nТест 8: футер отображается")
footer = driver.find_elements(By.XPATH, "//footer")

print("Найдено футеров:", len(footer))
assert len(footer) > 0, "Футер не отображается"
print("Проверка пройдена ✅")


time.sleep(3)
driver.quit()