from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

from base.base_class import Base


class PLP_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    page_title = "//h1[@class='subcategory__page-title']"  # локатор заголовок раздела
    page_title_value = "ПК, ноутбуки, периферия"  # ожидаемый заголовок раздела
    accessories_button = "//span[@class='subcategory__title' and contains(., 'Периферия')]"  # кнопка "Периферия и
    # аксессуары"

    # getters

    def get_page_title(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.page_title)))

    def get_accessories_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.accessories_button)))

    # actions

    def assert_page_title(self):
        assert self.get_page_title().text == self.page_title_value
        print("Открыта корректная страница")

    def click_accessories(self):
        self.get_accessories_button().click()
        print("Открываем раздел с периферией")

    # method

    def open_accessories(self):
        self.assert_page_title()
        self.click_accessories()
