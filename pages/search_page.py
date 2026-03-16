from locators.search_page_locators import SearchPageLocators


class SearchPage:

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("https://moskva.beeline.ru/shop/")

    def click_search_button(self):
        self.driver.find_element(*SearchPageLocators.SEARCH_BUTTON).click()