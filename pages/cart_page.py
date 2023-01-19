from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
import string


class Cart_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators

    cart_items = "//div[@class='cart-items__product']"
    items_names = "//a[@class='base-ui-link base-ui-link_gray_dark']"
    items_prices = "//span[@class='price__current']"

    # getters

    def get_cart_items(self):
        return WebDriverWait(self.driver, 30).until(EC.presence_of_all_elements_located((By.XPATH, self.cart_items)))

    def get_items_names(self):
        return WebDriverWait(self.driver, 30).until(EC.presence_of_all_elements_located((By.XPATH, self.items_names)))

    def get_items_prices(self):
        return WebDriverWait(self.driver, 30).until(EC.presence_of_all_elements_located((By.XPATH, self.items_prices)))

    # actions

    def print_cart_items_names(self):
        print("В корзине:")
        for element in self.get_items_names():
            print(element.text)

    def check_total_price(self):
        prices = []
        for element in self.get_items_prices():
            price = ''
            for i in element.text:
                if i in string.digits:
                    price += i
            prices += [int(price)]
        sum = 0
        for i in range(len(prices) - 1):
            sum += prices[i]
        assert sum == prices[-1]  # проверяем, верно ли посчиталась сумма
        print(f"Итоговая цена: {str(sum)}")

    # methods

    """Сценарий метода
    1. Выводим наименования всех товаров в корзине
    2. Сверяем цену и в случае успеха выводим её
    3. Делаем скриншот
    
    """
    def check_cart(self):
        self.print_cart_items_names()
        self.check_total_price()
        self.get_screenshot()
