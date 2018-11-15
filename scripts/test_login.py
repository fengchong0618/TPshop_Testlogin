import time

from base.base_action import BaseAction
from base.base_driver import init_driver
import pytest

from page.page import Page


class TestLogin:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(5)
        self.driver.quit()

    def test_login(self):
        self.page.home.click_my_button()
        self.page.home_mine.click_login_and_sign_up()






