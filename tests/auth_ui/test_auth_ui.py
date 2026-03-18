from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


print("Тест: авторизация UI")

driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 15)

try:
    driver.get("https://moskva.beeline.ru/shop/")

    print("Шаг 1: нажимаем кнопку 'войти'")
    wait.until(
        EC.element_to_be_clickable((By.CLASS_NAME, "login-button"))
    ).click()

    print("Шаг 2: нажимаем 'на сайте'")
    wait.until(
        EC.element_to_be_clickable((By.XPATH, "//a[@href='/login/']"))
    ).click()

    print("Шаг 3: проверяем, что открылась страница авторизации")
    wait.until(
        EC.presence_of_element_located((By.XPATH, "//button[.//span[contains(text(), 'Мобильный ID')]]"))
    )

    assert "/login" in driver.current_url
    print("Проверка пройдена: страница авторизации открылась ✅")

    print("\nШаг 4: переключаемся на вкладку 'СМС'")
    sms_tab = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[.//span[normalize-space()='СМС']]")
        )
    )
    sms_tab.click()

    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[contains(@class, 'selected')][.//span[normalize-space()='СМС']]")
        )
    )
    print("Проверка пройдена: вкладка 'СМС' открылась ✅")

    print("\nШаг 5: переключаемся на вкладку 'Логин'")
    login_tab = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[.//span[normalize-space()='Логин']]")
        )
    )
    login_tab.click()

    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[contains(@class, 'selected')][.//span[normalize-space()='Логин']]")
        )
    )
    print("Проверка пройдена: вкладка 'Логин' открылась ✅")

    print("\nШаг 6: возвращаемся на вкладку 'Мобильный ID'")
    mobile_id_tab = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[.//span[contains(text(), 'Мобильный ID')]]")
        )
    )
    mobile_id_tab.click()

    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[contains(@class, 'selected')][.//span[contains(text(), 'Мобильный ID')]]")
        )
    )
    print("Проверка пройдена: вкладка 'Мобильный ID' открылась ✅")

finally:
    driver.quit()