import time

import pytest
from chromedriver_py import binary_path
from selenium import webdriver

from pages.main_page import MainPage
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
        main_page = MainPage(self.driver)
        main_page.get()
        main_page.do_click(main_page.product_catalog)
        assert main_page.is_visible(main_page.product_catalog_popup) is True
        main_page.move_to_element(main_page.smartfony_and_gadzhety)
        main_page.do_click(main_page.catalog_smartfony)
        smartfony_page = SmartfonyPage(self.driver)
        assert smartfony_page.url in smartfony_page.driver.current_url


