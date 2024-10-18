from pages.base_page import BasePage


class SmartfonyPage(BasePage):
    url = 'https://www.citilink.ru/catalog/smartfony/'

    def __init__(self, driver):
        super().__init__(driver, self.url)

    # LOCATORS
    price_from = "//div[@data-meta-name='FilterDropdown']//input[@name='input-min']"
    price_to = "//div[@data-meta-name='FilterDropdown']//input[@name='input-max']"
    price_discount_10 = "//div[@data-meta-value='Товары со скидкой']//div[@data-meta-value='10% и больше']"
    cellular_standart_4g = "//div[@data-meta-value='Стандарт связи']//div[@data-meta-value='Технология 4G']"
