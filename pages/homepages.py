from selenium.webdriver.common.by import By

class HomePage:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        browser().get("https://moskva.beeline.ru/customers/products/")

