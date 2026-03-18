from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 15)

print("Тест: пункты меню переключаются")
driver.get("https://moskva.beeline.ru/shop/")

menu_button = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='открыть боковое меню']"))
)
menu_button.click()
time.sleep(1)

# интернет и тв
internet_tv = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//span[@data-t-id='contexts-link' and contains(., 'интернет и тв')]"))
)
internet_tv.click()
time.sleep(1)
print("Клик по пункту: интернет и тв")
assert "primary-invert" in internet_tv.get_attribute("style"), "Пункт 'интернет и тв' не стал активным"

# сервисы и подписки
services = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//span[@data-t-id='contexts-link' and contains(., 'сервисы и подписки')]"))
)
services.click()
time.sleep(1)
print("Клик по пункту: сервисы и подписки")
assert "primary-invert" in services.get_attribute("style"), "Пункт 'сервисы и подписки' не стал активным"

# оплата
payment = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//span[@data-t-id='contexts-link' and contains(., 'оплата')]"))
)
payment.click()
time.sleep(1)
print("Клик по пункту: оплата")
assert "primary-invert" in payment.get_attribute("style"), "Пункт 'оплата' не стал активным"

# магазин
shop = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//span[@data-t-id='contexts-link' and contains(., 'магазин')]"))
)
shop.click()
time.sleep(1)
print("Клик по пункту: магазин")
assert "primary-invert" in shop.get_attribute("style"), "Пункт 'магазин' не стал активным"

print("Все пункты меню переключаются корректно ✅")

time.sleep(2)
driver.quit()