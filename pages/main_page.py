from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Main_page(Base):
    url = "https://www.dns-shop.ru/"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators

    # сайт DNS может попросить подтвердить город проживания
    confirm_city = "//button[@class='base-ui-button_GWR base-ui-button_medium__Fr base-ui-button_brand_UhA " \
                   "base-ui-button_ico-none_Gf6 v-confirm-city__btn_hUa']"

    # выпадающий каталог
    catalog_button = "//span[@data-role='catalog-button']"

    # раздел с периферией
    plp_division = "//a[@class='catalog-menu__root-info catalog-menu__root-title' and contains(., " \
                   "'периферия')]"

    # getters

    def get_confirm_city(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.confirm_city)))

    def get_catalog_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.catalog_button)))

    def get_menu_division_plp(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.plp_division)))

    # actions

    def click_confirm_city(self):
        self.get_confirm_city().click()
        print("Подтверждаем город проживания")

    def click_catalog_button(self):
        self.get_catalog_button().click()
        print("Открываем выпадающий каталог")

    def click_plp(self):
        self.get_menu_division_plp().click()
        print("Выбираем раздел с ПК и периферией")

    # method

    """Сценарий метода:
    1. Открываем заданный url
    2. Разворачиваем браузер на полный экран
    3. Иногда вылезало окошко с просьбой подтвердить город проживания, в таком случае подтверждаем и обновляем страницу
    4. Открываем выпадающий каталог
    5. Открываем раздел с периферией
    """

    def open_plp(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        # если вылезло окошко с городом
        try:
            self.get_confirm_city()
            self.click_confirm_city()
            self.driver.refresh()  # перезагружаем страницу после подтверждения города
        except:
            pass
        self.click_catalog_button()
        self.click_plp()
