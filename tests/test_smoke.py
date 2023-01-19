import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.accessories_page import Accessories_page
from pages.cart_page import Cart_page
from pages.keyboards_page import Keyboard_page
from pages.main_page import Main_page
from pages.mice_page import Mouse_page
from pages.monitors_page import Monitor_page
from pages.pc_laptops_periphery_page import PLP_page


def test_1():

    """
    Тест:
    Ищем периферийные устройства (монитор, клавиатура, мышь) по фильтрам, 
    добавляем в корзину первый товар по популярности из каждого раздела (если товар не найден, то из этого раздела не берем)
    """
    
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome('C:\\Users\\grame\\PycharmProjects\\resource\\chromedriver.exe', options=options)
    print("Начало теста")

    mp = Main_page(driver)
    mp.open_plp()

    plp = PLP_page(driver)
    plp.open_accessories()

    ap = Accessories_page(driver)
    ap_url = ap.get_current_url()
    ap.click_monitor_button()

    monp = Monitor_page(driver)
    # функция вернет кол-во товаров, которое должно быть в корзине
    num = monp.select_monitor(ap_url, min_price=20000, max_price=50000, min_size=23, max_size=28, num=0)

    ap.click_keyboard_button()

    kp = Keyboard_page(driver)
    # функция вернет кол-во товаров, которое должно быть в корзине
    num = kp.select_keyboard(ap_url, min_price=1000, max_price=5000, num=num)

    ap.click_mouse_button()

    moup = Mouse_page(driver)
    moup.select_mouse(min_price=1500, max_price=4500, num=num)

    cartp = Cart_page(driver)
    cartp.check_cart()

    time.sleep(10)
    driver.quit()
    print("Конец теста")
