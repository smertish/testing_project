from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class MainPage(BasePage):
    url = 'https://www.citilink.ru/'

    def __init__(self, driver):
        super().__init__(driver, self.url)

    # LOCATORS
    product_catalog = "//a[@href='/catalog/']"
    product_catalog_popup = "//div[@data-meta-name='Popup']"
    smartfony_and_gadzhety = "//div[contains(@data-meta-name, 'menu')]//a[contains(@href, 'smartfony-i-gadzhety')]"
    catalog_smartfony = "//a[span[text()='Смартфоны']]"
