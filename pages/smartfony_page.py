from pages.base_page import BasePage


class SmartfonyPage(BasePage):
    url = 'https://www.citilink.ru/catalog/smartfony/'

    def __init__(self, driver):
        super().__init__(driver, self.url)

    # LOCATORS
    price_from = "//div[@data-meta-name='FilterDropdown']//input[@name='input-min']"
    price_to = "//div[@data-meta-name='FilterDropdown']//input[@name='input-max']"
    price_discount_35 = "//div[@data-meta-value='Товары со скидкой']//div[@data-meta-value='35% и больше']"
    cellular_standart_4g = "//div[@data-meta-value='Технология 4G']//span[input]"
    add_to_cart_first = "(//div[button[@data-meta-name='Snippet__cart-button']])[1]"
    product_added_dialog = "//div[@data-meta-name='UpsaleBasketLayout']"
    dialog_go_basket = "(//div[@data-meta-name='UpsaleBasketLayout']//button[span[text()='Перейти в корзину']])[1]"
    first_product_description = ("(//div[@data-meta-name='ProductHorizontalSnippet'])[1]"
                                 "//div[@class='app-catalog-1o4umte ec53oil0']/ul")
