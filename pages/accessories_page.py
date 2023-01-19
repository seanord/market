from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

from base.base_class import Base


class Accessories_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    page_title = "//h1[@class='subcategory__page-title']"  # локатор заголовок раздела
    page_title_value = "Периферия и аксессуары"  # ожидаемый заголовок раздела
    monitor_button = "//span[@class='subcategory__title' and contains(., 'Мониторы')]"
    keyboard_button = "//span[@class='subcategory__title' and contains(., 'Клавиатуры')]"
    mouse_button = "//span[@class='subcategory__title' and contains(., 'Мыши')]"

    # getters

    def get_page_title(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.page_title)))

    def get_monitor_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.monitor_button)))

    def get_keyboard_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.keyboard_button)))

    def get_mouse_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.mouse_button)))

    # actions

    def assert_page_title(self):
        assert self.get_page_title().text == self.page_title_value
        print("Открыта корректная страница")

    def click_monitor_button(self):
        self.get_monitor_button().click()
        print("Открываем раздел с мониторами")

    def click_keyboard_button(self):
        self.get_keyboard_button().click()
        print("Открываем раздел с клавиатурами")

    def click_mouse_button(self):
        self.get_mouse_button().click()
        print("Открываем раздел с мышами")

    # method

    def open_monitor(self):
        self.assert_page_title()
        self.click_monitor_button()

    def open_keyboard(self):
        self.assert_page_title()
        self.click_keyboard_button()

    def open_mouse(self):
        self.assert_page_title()
        self.click_mouse_button()
