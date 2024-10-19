from pages.base_page import BasePage


class OrderPage(BasePage):
    url = 'https://www.citilink.ru/order/'

    def __init__(self, driver):
        super().__init__(driver, self.url)

    # LOCATORS
    discount_percentage = "(//div[@data-meta-name='AvailableProductStatus__price']//span)[1]"
    product_price = "//div[@data-meta-name='AvailableProductStatus__price']//span[@data-meta-price]"
    go_registration = "//button[@title='Перейти к оформлению']"
    dialog_popup = "//div[@data-meta-name='Popup']"
    dialog_popup_continue_as_guest = "//div[@data-meta-name='Popup']//button[span[text()='Продолжить как гость']]"
