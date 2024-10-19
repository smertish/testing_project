from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:
    cookies_agree = "//button[span[text()='Я согласен']]"
    loading_icon = "//div[@data-meta-name='OverlayLoader__loader']"
    loading_icon_basket = "//div[@class='eqddkec0 app-catalog-1j37as7 e1xgzt690']"
    notification_counter = "//div[@data-meta-name='NotificationCounter']"

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def get(self):
        self.driver.get(self.url)

    def do_click(self, locator):
        self.__wait()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, locator))).click()
        self.__wait()

    def check_clickability(self, locator):
        self.__wait()
        try:
            element = WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable((By.XPATH, locator)))
        except TimeoutException as e:
            element = False
        return bool(element)

    def is_visible(self, locator):
        self.__wait()
        try:
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, locator)))
        except TimeoutException as e:
            element = False
        return bool(element)

    def move_to_element(self, locator):
        self.__wait()
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, locator)))
        ActionChains(self.driver).move_to_element(element).perform()
        self.__wait()

    def do_send_keys(self, locator, text):
        self.__wait()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, locator))).send_keys(text)
        self.__wait()

    def do_send_keys(self, locator, text):
        self.__wait()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, locator))).send_keys(text)
        self.__wait()

    def get_element(self, locator):
        self.__wait()
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, locator)))
        self.__wait()
        return element

    def __wait(self):
        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located((By.XPATH, self.loading_icon)))
        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located((By.XPATH, self.loading_icon_basket)))
