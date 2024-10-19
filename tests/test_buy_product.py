import time

import pytest
from chromedriver_py import binary_path
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains

from pages.main_page import MainPage
from pages.order_checkout_page import OrderCheckoutPage
from pages.order_page import OrderPage
from pages.smartfony_page import SmartfonyPage


class TestBuyProduct:
    @pytest.fixture(autouse=True)
    def setup(self):
        options = webdriver.ChromeOptions()
        options.page_load_strategy = "eager"  # подсмотрел в комментах. Нужно, чтобы быстрее работало :)
        # options.add_argument('--headless=new')  # раскомментить, если нужно запустить в "безголовом" режиме
        self.driver = webdriver.Chrome(service=(webdriver.ChromeService(executable_path=binary_path)), options=options)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_buy_product_1(self):
        price_from_value, price_to_value = '10000', '100000'
        cellular_standart_value = '4G'
        discount_value = '35'
        main_page = MainPage(self.driver)
        main_page.get()
        # сразу соглашаемся с печеньями, чтобы не мешали
        main_page.do_click(main_page.cookies_agree)
        # нажимаем кнопку Каталог товаров
        main_page.do_click(main_page.product_catalog)
        # проверяем, что шторка с каталогом открылась
        assert main_page.is_visible(main_page.product_catalog_popup) is True
        # наводим на Смартфоны и гаджеты
        main_page.move_to_element(main_page.smartfony_and_gadzhety)
        # нажимаем на Смартфоны
        main_page.do_click(main_page.catalog_smartfony)
        smartfony_page = SmartfonyPage(self.driver)
        # проверяем, что осуществлен переход на нужную нам страницу
        assert smartfony_page.url in smartfony_page.driver.current_url
        # заполняем фильтры
        smartfony_page.do_send_keys(smartfony_page.price_from, Keys.CONTROL + 'a')
        smartfony_page.do_send_keys(smartfony_page.price_from, price_from_value)
        smartfony_page.do_send_keys(smartfony_page.price_from, Keys.ENTER)
        smartfony_page.do_send_keys(smartfony_page.price_to, Keys.CONTROL + 'a')
        smartfony_page.do_send_keys(smartfony_page.price_to, price_to_value)
        smartfony_page.do_send_keys(smartfony_page.price_to, Keys.ENTER)
        smartfony_page.do_click(smartfony_page.price_discount_35)
        smartfony_page.do_click(smartfony_page.cellular_standart_4g)
        ActionChains(smartfony_page.driver).send_keys(Keys.HOME).perform()
        # проверяем описание товара
        assert cellular_standart_value in smartfony_page.get_element(smartfony_page.first_product_description).text
        # добавляем товар в корзину
        smartfony_page.do_click(smartfony_page.add_to_cart_first)
        # открылось диалоговое окно
        assert smartfony_page.is_visible(smartfony_page.product_added_dialog) is True
        # переходим в корзину
        smartfony_page.do_click(smartfony_page.dialog_go_basket)
        order_page = OrderPage(self.driver)
        # проверяем, что осуществлен переход на нужную нам страницу
        assert order_page.url in order_page.driver.current_url
        # проверяем данные, чтобы совпадали с фильтрами
        assert int(discount_value) <= int(order_page.get_element(order_page.discount_percentage).text[1:-1])
        assert int(price_from_value) <= int(
            order_page.get_element(order_page.product_price).text[:-1].replace(' ', '')) <= int(price_to_value)
        # проверяем, что в уведомлениях добавился товар (рядом с корзинкой вверху)
        assert order_page.get_element(order_page.notification_counter).text == '1'
        # нажимаем Оформить
        order_page.do_click(order_page.go_registration)
        # проверяем, что открылось диалоговое окно регистрации
        assert order_page.is_visible(order_page.dialog_popup) is True
        # нажимаем Продолжить как гость
        order_page.do_click(order_page.dialog_popup_continue_as_guest)
        order_checkout_page = OrderCheckoutPage(self.driver)
        # проверяем, что осуществлен переход на нужную нам страницу
        assert order_checkout_page.url in order_checkout_page.driver.current_url
