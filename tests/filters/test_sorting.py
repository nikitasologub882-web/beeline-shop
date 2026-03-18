from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# запускаем браузер
driver = webdriver.Chrome()
driver.maximize_window()
# создаем ожидание
wait = WebDriverWait(driver, 15)
driver.get("https://moskva.beeline.ru/shop/catalog/telefony/smartfony/")

print("Тест: переключение сортировки")
# 1. Проверяем текущую сортировку
# находим текст внутри кнопки сортировки
sort_text = wait.until(
    EC.presence_of_element_located(
        (By.XPATH, "//button[@data-t-id='Dropdown-components']//div[contains(@class,'label')]")
    )
)
print("Текущая сортировка:", sort_text.text)
# проверяем, что текст вообще есть
assert sort_text.text != "", "Сортировка не отображается"

# 2. Выбираем "По цене от дешевых"
# находим кнопку сортировки
sort_button = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//button[@data-t-id='Dropdown-components']")
    )
)
# кликаем по кнопке (открываем список)
driver.execute_script("arguments[0].click();", sort_button)
# находим вариант "По цене от дешевых"
cheap_option = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//div[text()='По цене от дешевых']")
    )
)
# кликаем по нему
driver.execute_script("arguments[0].click();", cheap_option)
# ждем, пока текст в кнопке изменится
wait.until(
    EC.text_to_be_present_in_element(
        (By.XPATH, "//button[@data-t-id='Dropdown-components']//div[contains(@class,'label')]"),
        "По цене от дешевых"
    )
)
# заново берем текст сортировки
sort_text = driver.find_element(
    By.XPATH,
    "//button[@data-t-id='Dropdown-components']//div[contains(@class,'label')]"
)
print("После выбора:", sort_text.text)
# проверяем результат
assert sort_text.text == "По цене от дешевых", \
    "Сортировка не переключилась на 'По цене от дешевых'"

# 3. Выбираем "По цене от дорогих"
# снова открываем список
sort_button = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//button[@data-t-id='Dropdown-components']")
    )
)
driver.execute_script("arguments[0].click();", sort_button)
# находим вариант "По цене от дорогих"
expensive_option = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//div[text()='По цене от дорогих']")
    )
)
# кликаем
driver.execute_script("arguments[0].click();", expensive_option)
# ждем обновления текста
wait.until(
    EC.text_to_be_present_in_element(
        (By.XPATH, "//button[@data-t-id='Dropdown-components']//div[contains(@class,'label')]"),
        "По цене от дорогих"
    )
)
# проверяем текст
sort_text = driver.find_element(
    By.XPATH,
    "//button[@data-t-id='Dropdown-components']//div[contains(@class,'label')]"
)
print("После выбора:", sort_text.text)
assert sort_text.text == "По цене от дорогих", \
    "Сортировка не переключилась на 'По цене от дорогих'"

# 4. Выбираем "По популярности"
# снова открываем список
sort_button = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//button[@data-t-id='Dropdown-components']")
    )
)
driver.execute_script("arguments[0].click();", sort_button)
# находим вариант "По популярности"
popular_option = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//div[text()='По популярности']")
    )
)
# кликаем
driver.execute_script("arguments[0].click();", popular_option)
# ждем обновления текста
wait.until(
    EC.text_to_be_present_in_element(
        (By.XPATH, "//button[@data-t-id='Dropdown-components']//div[contains(@class,'label')]"),
        "По популярности"
    )
)
# проверяем текст
sort_text = driver.find_element(
    By.XPATH,
    "//button[@data-t-id='Dropdown-components']//div[contains(@class,'label')]"
)
print("После выбора:", sort_text.text)
assert sort_text.text == "По популярности", \
    "Сортировка не переключилась на 'По популярности'"

print("Тест пройден")
driver.quit()