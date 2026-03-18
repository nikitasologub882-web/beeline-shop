from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 15)

driver.get("https://moskva.beeline.ru/shop/catalog/telefony/smartfony/")

print("Тест: переключение категорий телефонов")
# =========================
# Apple iPhone
iphone = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//span[text()='Apple iPhone']"))
)
iphone.click()
wait.until(EC.url_contains("apple-iphone"))
print("Перешли в Apple iPhone:", driver.current_url)
assert "apple-iphone" in driver.current_url, "Не перешли в Apple iPhone"

# =========================
# Samsung Galaxy
samsung = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//span[text()='Samsung Galaxy']"))
)
samsung.click()
wait.until(EC.url_contains("samsung-galaxy"))
print("Перешли в Samsung Galaxy:", driver.current_url)
assert "samsung-galaxy" in driver.current_url, "Не перешли в Samsung Galaxy"

# =========================
# Xiaomi
xiaomi = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//span[text()='Xiaomi']"))
)
xiaomi.click()
wait.until(EC.url_contains("xiaomi"))
print("Перешли в Xiaomi:", driver.current_url)
assert "xiaomi" in driver.current_url, "Не перешли в Xiaomi"

# =========================
# Infinix
infinix = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//span[text()='Infinix']"))
)
infinix.click()
wait.until(EC.url_contains("infinix"))
print("Перешли в Infinix:", driver.current_url)
assert "infinix" in driver.current_url, "Не перешли в Infinix"

print("Тест пройден")
driver.quit()