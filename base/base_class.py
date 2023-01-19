import datetime


class Base():

    def __init__(self, driver):
        self.driver = driver

    def get_current_url(self):
        get_url = self.driver.current_url
        # print(f"Current url: {get_url}")
        return get_url

    def get_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        self.driver.save_screenshot(f"screenshots\\screenshot_{now_date}.png")

    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result

    # проверка, что максимальное значение не ниже минимального (цена, диагональ экрана и т.д.)
    def check_min_max(self, min_value, max_value):
        return min(min_value, max_value), max(min_value, max_value)
