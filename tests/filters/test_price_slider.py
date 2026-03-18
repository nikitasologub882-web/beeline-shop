from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 15)

driver.get("https://moskva.beeline.ru/shop/catalog/telefony/smartfony/")

print("Тест: проверка движения ползунка цены")

# ждем правый ползунок
right_slider = wait.until(
    EC.presence_of_element_located((By.XPATH, "(//div[@role='slider'])[2]"))
)

# берем начальное значение максимальной цены
start_value = int(right_slider.get_attribute("aria-valuenow"))
print("Начальное значение:", start_value)

# двигаем ползунок немного влево
ActionChains(driver).click_and_hold(right_slider).move_by_offset(-80, 0).release().perform()

# снова находим ползунок
right_slider = wait.until(
    EC.presence_of_element_located((By.XPATH, "(//div[@role='slider'])[2]"))
)

# берем новое значение
value_after_first_move = int(right_slider.get_attribute("aria-valuenow"))
print("После первого движения:", value_after_first_move)

# проверяем, что значение уменьшилось
assert value_after_first_move < start_value, "После первого движения значение не уменьшилось"

# двигаем еще раз влево
ActionChains(driver).click_and_hold(right_slider).move_by_offset(-80, 0).release().perform()

# снова находим ползунок
right_slider = wait.until(
    EC.presence_of_element_located((By.XPATH, "(//div[@role='slider'])[2]"))
)

# берем еще одно значение
value_after_second_move = int(right_slider.get_attribute("aria-valuenow"))
print("После второго движения:", value_after_second_move)

# проверяем, что значение снова уменьшилось
assert value_after_second_move < value_after_first_move, "После второго движения значение не уменьшилось"

print("Тест пройден")

driver.quit()