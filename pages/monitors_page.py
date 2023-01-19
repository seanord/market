import time
import string

from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Monitor_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    ignored_exceptions = (NoSuchElementException, StaleElementReferenceException,)

    # locators

    page_title = "//h1[@class='title']"  # локатор заголовок раздела
    page_title_value = "Мониторы"  # ожидаемый заголовок раздела (часть)

    # фильтры
    # цена
    price_min = "(//input[@class='ui-input-small__input ui-input-small__input_list'])[1]"
    price_max = "(//input[@class='ui-input-small__input ui-input-small__input_list'])[2]"
    # диагональ
    size_expand = "//div[@data-id='fr[o7]']"
    size_min = "(//input[@class='ui-input-small__input ui-input-small__input_list'])[3]"
    size_max = "(//input[@class='ui-input-small__input ui-input-small__input_list'])[4]"
    # тип матрицы
    matrix_expand = "//div[@data-id='f[6nw]']"
    ips_matrix = "//label[@class='ui-checkbox ui-checkbox_list' and contains(.,'IPS')]"
    # наличие hdmi разъема
    hdmi_expand = "//div[@data-id='f[nl2q]']"
    hdmi = "//div[@data-id='f[nl2q]']//label[@class='ui-checkbox ui-checkbox_list' and contains(.,'есть')]"
    # применить фильтры
    apply_filters_button = "//button[@data-role='filters-submit']"

    # сортировка
    sorting = "(//span[@class ='top-filter__selected'])[1]"
    sorting_by_popular = "//span[@class='ui-radio__content' and contains(., 'Сначала популярные')]"

    # данные выбранного товара
    buy_button = "(//button[contains(., 'Купить')])[1]"
    item_name = "//a[@class='catalog-product__name ui-link ui-link_black'][1]"
    item_price = "(//div[@class='product-buy__price'])[1]"

    # всплывающее окошко корзины
    basket = "//div[@class='cart-modal cart-link-counter__modal']"

    # количество товаров в корзине
    items_number = "//span[@class='cart-group__header-title']"

    # если товаров не найдено
    no_items_found = "//h4[contains(.,'Странно, но ничего нет')]"

    # getters

    def get_page_title(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.page_title)))

    def get_price_min(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_min)))

    def get_price_max(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_max)))

    def get_size_expand(self):
        return WebDriverWait(self.driver, 30, ignored_exceptions=self.ignored_exceptions).until(
            EC.element_to_be_clickable((By.XPATH, self.size_expand)))

    def get_size_min(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.size_min)))

    def get_size_max(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.size_max)))

    def get_matrix_expand(self):
        return WebDriverWait(self.driver, 30, ignored_exceptions=self.ignored_exceptions).until(
            EC.element_to_be_clickable((By.XPATH, self.matrix_expand)))

    def get_ips_matrix(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.ips_matrix)))

    def get_hdmi_expand(self):
        return WebDriverWait(self.driver, 30, ignored_exceptions=self.ignored_exceptions).until(
            EC.element_to_be_clickable((By.XPATH, self.hdmi_expand)))

    def get_hdmi(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.hdmi)))

    def get_apply_filters_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.apply_filters_button)))

    def get_sorting(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.sorting)))

    def get_sorting_by_popular(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.sorting_by_popular)))

    def get_item_name(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.item_name)))

    def get_item_price(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.item_price)))

    def get_buy_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.buy_button)))

    def get_basket(self):
        return WebDriverWait(self.driver, 30).until(EC.invisibility_of_element_located((By.XPATH, self.basket)))

    def get_items_number(self, num):
        return WebDriverWait(self.driver, 30).until(
            EC.text_to_be_present_in_element((By.XPATH, self.items_number), str(num)))

    def get_no_items_found(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.no_items_found)))

    # actions

    def assert_page_title(self):
        assert self.page_title_value in self.get_page_title().text
        print("Открыта корректная страница")

    def send_min_price(self, min_price):
        action = ActionChains(self.driver)
        action.move_to_element(self.get_price_min()).perform()
        min_price_collar = self.get_price_min().get_attribute("min")
        self.get_price_min().send_keys(max(int(min_price_collar), min_price))
        print("Задаём минимальную цену")

    def send_max_price(self, max_price):
        max_price_collar = self.get_price_max().get_attribute("max")
        self.get_price_max().send_keys(min(int(max_price_collar), max_price))
        print("Задаём максимальную цену")

    def expand_size_filter(self):
        self.driver.execute_script('arguments[0].scrollIntoView()', self.get_size_expand())
        self.get_size_expand().click()

    def send_min_size(self, min_size):
        min_size_collar = self.get_size_min().get_attribute("min")
        self.get_size_min().send_keys(max(float(min_size_collar), min_size))

    def send_max_size(self, max_size):
        max_size_collar = self.get_size_max().get_attribute("max")
        self.get_size_max().send_keys(min(float(max_size_collar), max_size))

    def expand_matrix_filter(self):
        # actionChains здесь отказался работать
        self.driver.execute_script('arguments[0].scrollIntoView()', self.get_matrix_expand())
        self.get_matrix_expand().click()

    def select_ips_matrix(self):
        self.get_ips_matrix().click()
        print("Выбираем IPS матрицу")

    def expand_hdmi_filter(self):
        self.driver.execute_script('arguments[0].scrollIntoView()', self.get_hdmi_expand())
        self.get_hdmi_expand().click()

    def select_hdmi(self):
        self.get_hdmi().click()
        print("Выбираем монитор с HDMI разъёмом")

    def apply_filters(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.get_apply_filters_button()).perform()
        self.get_apply_filters_button().click()
        print("Применяем фильтры")

    def click_sorting(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.get_sorting()).perform()
        self.get_sorting().click()

    def click_sorting_by_popular(self):
        self.get_sorting_by_popular().click()
        print("Сортируем по популярности")

    def buy_top_item(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.get_buy_button()).perform()
        self.get_buy_button().click()
        print("Покупаем первый монитор из списка")

    def print_item_parameters(self):
        print(f"Выбранный товар:\n{self.get_item_name().text}\nЦена: {self.get_item_price().text}")

    def check_items_number(self, num):
        self.get_items_number(num)
        print("Товар добавлен в корзину")

    def check_if_no_items_found(self):
        self.get_no_items_found()
        print("Не найдено товаров, подходящих под фильтры")
        return True

    # methods

    def set_filters(self, min_price, max_price, min_size, max_size):
        min_price, max_price = self.check_min_max(min_price, max_price)
        self.send_min_price(min_price)
        self.send_max_price(max_price)
        self.expand_size_filter()
        min_size, max_size = self.check_min_max(min_size, max_size)
        self.send_min_size(min_size)
        self.send_max_size(max_size)
        self.expand_matrix_filter()
        self.select_ips_matrix()
        self.expand_hdmi_filter()
        self.select_hdmi()

    """Сценарий метода
    1. Проверяем заголовок страницы
    2. Задаём фильтры:
        2.1 Минимальная цена
        2.2 Максимальная цена 
            Если введенные минимальная или максимальная цены не удовлетворяют требованию сайта (аттрибуты min и max 
            у полей), то они заменяются на минимальное/максимальное значение, принимаемое сайтом
        2.3 Минимальный размер диагонали монитора
        2.4 Максимальный размер диагонали монитора
        2.5 Тип матрицы: IPS
        2.6. Наличие HDMI разъёма
    3. Применяем фильтры
    4. Сортируем список по популярности товаров
    5. Обновляем страницу после того, как сортировка применится (так как часто вылезало исключение, от которого не 
        удавалось избавиться
    6. Выводим параметры первого товара на странице
    7. Добавляем первый товар в корзину
    8. Проверяем, что товар добавился в корзину
    9. Переходим в раздел "Периферия и аксессуары"
    """

    def select_monitor(self, ap_url, min_price, max_price, min_size, max_size, num):
        # self.driver.maximize_window()
        self.assert_page_title()
        self.set_filters(min_price, max_price, min_size, max_size)
        self.apply_filters()
        self.click_sorting()
        self.click_sorting_by_popular()
        self.driver.refresh()
        try:
            self.print_item_parameters()
            self.buy_top_item()
            self.check_items_number(num+1)
            num += 1
        except TimeoutException:
            assert self.check_if_no_items_found() == True
        self.driver.get(ap_url)
        print(f"Выбрано товаров: {num}")
        return num

