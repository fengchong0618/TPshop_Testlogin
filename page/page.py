from page.page_home import Home
from page.page_home_mine import HomeMine


class Page:

    def __init__(self, driver):
        self.driver = driver

    @property
    def home(self):
        return Home(self.driver)

    @property
    def home_mine(self):
        return HomeMine(self.driver)
