from base.base_action import BaseAction
from base.base_driver import init_driver
import pytest


class TestLogin:

    def setup(self):
        self.driver = init_driver()

    def teardown(self):
        self.driver.quit()

    def test_login(self):
        print("初始化")

    #
    # def test_login(self):
    #
    #     BaseAction.find_element()


