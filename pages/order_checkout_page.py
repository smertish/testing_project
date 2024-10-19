from pages.base_page import BasePage


class OrderCheckoutPage(BasePage):
    url = 'https://www.citilink.ru/order/checkout/'

    def __init__(self, driver):
        super().__init__(driver, self.url)

    # LOCATORS
