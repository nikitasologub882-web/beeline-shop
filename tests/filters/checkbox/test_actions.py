import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://moskva.beeline.ru/shop/catalog/telefony/smartfony/")
time.sleep(2)

# Локаторы
CHECKBOX_1 = ("xpath", "//div[@class='styles_component__1AIbl']")
CHECKBOX_2 = ("xpath", "(//div[@class='styles_component__1AIbl'])[2]")
CHECKBOX_3 = ("xpath", "(//div[@class='styles_component__1AIbl'])[3]")
CHECKBOX_4 = ("xpath", "(//div[@class='styles_component__1AIbl'])[4]")
CHECKBOX_5 = ("xpath", "(//div[@class='styles_component__1AIbl'])[5]")
CHECKBOX_6 = ("xpath", "(//div[@class='styles_component__1AIbl'])[6]")
CHECKBOX_7 = ("xpath", "(//div[@class='styles_component__1AIbl'])[7]")
CHECKBOX_8 = ("xpath", "(//div[@class='styles_component__1AIbl'])[8]")
CHECKBOX_9 = ("xpath", "(//div[@class='styles_component__1AIbl'])[9]")
CHECKBOX_10 = ("xpath", "(//div[@class='styles_component__1AIbl'])[10]")
CHECKBOX_11 = ("xpath", "(//div[@class='styles_component__1AIbl'])[11]")
CHECKBOX_12 = ("xpath", "(//div[@class='styles_component__1AIbl'])[12]")
CHECKBOX_13 = ("xpath", "(//div[@class='styles_component__1AIbl'])[13]")
CHECKBOX_14 = ("xpath", "(//div[@class='styles_component__1AIbl'])[14]")
CHECKBOX_15 = ("xpath", "(//div[@class='styles_component__1AIbl'])[15]")
CHECKBOX_16 = ("xpath", "(//div[@class='styles_component__1AIbl'])[16]")
CHECKBOX_17 = ("xpath", "(//div[@class='styles_component__1AIbl'])[17]")
CHECKBOX_18 = ("xpath", "(//div[@class='styles_component__1AIbl'])[18]")

# Тест 1
print("Тест 1:")
checkbox = driver.find_element(*CHECKBOX_1)
inner = checkbox.find_element("xpath", ".//span[contains(@class, 'styles_checkbox')]")
print('До:', 'styles_checked' in inner.get_attribute('class'))
checkbox.click()
time.sleep(0.5)
print('После:', 'styles_checked' in inner.get_attribute('class'))
checkbox.click()
time.sleep(0.5)

# Тест 2
print("\nТест 2:")
checkbox = driver.find_element(*CHECKBOX_2)
inner = checkbox.find_element("xpath", ".//span[contains(@class, 'styles_checkbox')]")
print('До:', 'styles_checked' in inner.get_attribute('class'))
checkbox.click()
time.sleep(0.5)
print('После:', 'styles_checked' in inner.get_attribute('class'))
checkbox.click()
time.sleep(0.5)

# Тест 3
print("\nТест 3:")
checkbox = driver.find_element(*CHECKBOX_3)
inner = checkbox.find_element("xpath", ".//span[contains(@class, 'styles_checkbox')]")
print('До:', 'styles_checked' in inner.get_attribute('class'))
checkbox.click()
time.sleep(0.5)
print('После:', 'styles_checked' in inner.get_attribute('class'))
checkbox.click()
time.sleep(0.5)

# Тест 4
print("\nТест 4:")
checkbox = driver.find_element(*CHECKBOX_4)
inner = checkbox.find_element("xpath", ".//span[contains(@class, 'styles_checkbox')]")
print('До:', 'styles_checked' in inner.get_attribute('class'))
checkbox.click()
time.sleep(0.5)
print('После:', 'styles_checked' in inner.get_attribute('class'))
checkbox.click()
time.sleep(0.5)

# Тест 5
print("\nТест 5:")
checkbox = driver.find_element(*CHECKBOX_5)
inner = checkbox.find_element("xpath", ".//span[contains(@class, 'styles_checkbox')]")
print('До:', 'styles_checked' in inner.get_attribute('class'))
checkbox.click()
time.sleep(0.5)
print('После:', 'styles_checked' in inner.get_attribute('class'))
checkbox.click()
time.sleep(0.5)

# Локатор для кнопки "Показать всё"
SHOW_ALL_BUTTON = ("xpath", "//span[@class='styles_text__iSxH0' and text()='Показать всё']")

try:
    show_all_button = driver.find_element(*SHOW_ALL_BUTTON)
    print("Найдена кнопка 'Показать всё'")
    show_all_button.click()
    time.sleep(2)  # Ждем загрузки дополнительных чекбоксов
    print("Клик на 'Показать всё' выполнен")
except Exception as e:
    print(f"Не удалось найти или кликнуть 'Показать всё': {e}")

# Тест 6
print("\nТест 6:")
checkbox = driver.find_element(*CHECKBOX_6)
inner = checkbox.find_element("xpath", ".//span[contains(@class, 'styles_checkbox')]")
print('До:', 'styles_checked' in inner.get_attribute('class'))
checkbox.click()
time.sleep(0.5)
print('После:', 'styles_checked' in inner.get_attribute('class'))
checkbox.click()
time.sleep(0.5)

# Тест 7
print("Тест 7:")
checkbox = driver.find_element(*CHECKBOX_7)
inner = checkbox.find_element("xpath", ".//span[contains(@class, 'styles_checkbox')]")
print('До:', 'styles_checked' in inner.get_attribute('class'))
checkbox.click()
time.sleep(0.5)
print('После:', 'styles_checked' in inner.get_attribute('class'))
checkbox.click()
time.sleep(0.5)

# Тест 8
print("\nТест 8:")
checkbox = driver.find_element(*CHECKBOX_8)
inner = checkbox.find_element("xpath", ".//span[contains(@class, 'styles_checkbox')]")
print('До:', 'styles_checked' in inner.get_attribute('class'))
checkbox.click()
time.sleep(0.5)
print('После:', 'styles_checked' in inner.get_attribute('class'))
checkbox.click()
time.sleep(0.5)

# Тест 9
print("\nТест 9:")
checkbox = driver.find_element(*CHECKBOX_9)
inner = checkbox.find_element("xpath", ".//span[contains(@class, 'styles_checkbox')]")
print('До:', 'styles_checked' in inner.get_attribute('class'))
checkbox.click()
time.sleep(0.5)
print('После:', 'styles_checked' in inner.get_attribute('class'))
checkbox.click()
time.sleep(0.5)

# Тест 10
print("\nТест 10:")
checkbox = driver.find_element(*CHECKBOX_10)
inner = checkbox.find_element("xpath", ".//span[contains(@class, 'styles_checkbox')]")
print('До:', 'styles_checked' in inner.get_attribute('class'))
checkbox.click()
time.sleep(0.5)
print('После:', 'styles_checked' in inner.get_attribute('class'))
checkbox.click()
time.sleep(0.5)

# Тест 11
print("\nТест 11:")
checkbox = driver.find_element(*CHECKBOX_11)
inner = checkbox.find_element("xpath", ".//span[contains(@class, 'styles_checkbox')]")
print('До:', 'styles_checked' in inner.get_attribute('class'))
checkbox.click()
time.sleep(0.5)
print('После:', 'styles_checked' in inner.get_attribute('class'))
checkbox.click()
time.sleep(0.5)

# Тест 12
print("\nТест 12:")
checkbox = driver.find_element(*CHECKBOX_12)
inner = checkbox.find_element("xpath", ".//span[contains(@class, 'styles_checkbox')]")
print('До:', 'styles_checked' in inner.get_attribute('class'))
checkbox.click()
time.sleep(0.5)
print('После:', 'styles_checked' in inner.get_attribute('class'))
checkbox.click()
time.sleep(1)

# Тест 13
print("Тест 13:")
checkbox = driver.find_element(*CHECKBOX_13)
inner = checkbox.find_element("xpath", ".//span[contains(@class, 'styles_checkbox')]")
print('До:', 'styles_checked' in inner.get_attribute('class'))
checkbox.click()
time.sleep(0.5)
print('После:', 'styles_checked' in inner.get_attribute('class'))
checkbox.click()
time.sleep(0.5)

# Тест 14
print("\nТест 14:")
checkbox = driver.find_element(*CHECKBOX_14)
inner = checkbox.find_element("xpath", ".//span[contains(@class, 'styles_checkbox')]")
print('До:', 'styles_checked' in inner.get_attribute('class'))
checkbox.click()
time.sleep(0.5)
print('После:', 'styles_checked' in inner.get_attribute('class'))
checkbox.click()
time.sleep(0.5)

# Тест 15
print("\nТест 15:")
checkbox = driver.find_element(*CHECKBOX_15)
inner = checkbox.find_element("xpath", ".//span[contains(@class, 'styles_checkbox')]")
print('До:', 'styles_checked' in inner.get_attribute('class'))
checkbox.click()
time.sleep(0.5)
print('После:', 'styles_checked' in inner.get_attribute('class'))
checkbox.click()
time.sleep(0.5)

# Тест 16
print("\nТест 16:")
checkbox = driver.find_element(*CHECKBOX_16)
inner = checkbox.find_element("xpath", ".//span[contains(@class, 'styles_checkbox')]")
print('До:', 'styles_checked' in inner.get_attribute('class'))
checkbox.click()
time.sleep(0.5)
print('После:', 'styles_checked' in inner.get_attribute('class'))
checkbox.click()
time.sleep(0.5)

# Тест 17
print("\nТест 17:")
checkbox = driver.find_element(*CHECKBOX_17)
inner = checkbox.find_element("xpath", ".//span[contains(@class, 'styles_checkbox')]")
print('До:', 'styles_checked' in inner.get_attribute('class'))
checkbox.click()
time.sleep(0.5)
print('После:', 'styles_checked' in inner.get_attribute('class'))
checkbox.click()
time.sleep(0.5)

# Тест 18
print("\nТест 18:")
checkbox = driver.find_element(*CHECKBOX_18)
inner = checkbox.find_element("xpath", ".//span[contains(@class, 'styles_checkbox')]")
print('До:', 'styles_checked' in inner.get_attribute('class'))
checkbox.click()
time.sleep(0.5)
print('После:', 'styles_checked' in inner.get_attribute('class'))
checkbox.click()
time.sleep(1)