import sys

from Objects.account import Account

sys.path.append(".")
import unittest
from Pages.login_page import LoginPage
from TestCases.base_test import BaseTest
from TestData.test_data import TestData
import time


class HerokuAppLogin1(BaseTest):
    """A sample test class to show how page object works"""

    @classmethod
    def setUp(self):
        super().setUp()

    @classmethod
    def tearDown(self):
        super().tearDown()

    #def test_login_successfully(self):
        #login_page = LoginPage(self.driver)
        #account = Account(TestData.USERNAME, TestData.PASSWORD)
        #login_page.login(account)


    #def test_login_account_locked_out_user(self):
        #account = Account(TestData.FAKE_USERNAME, TestData.PASSWORD)
        #login_page.login(account)
        #print(login_page.get_error_text())
        #self.assertEqual(login_page.get_error_text(), 'Epic sadface: Sorry, this user has been locked out.')

    def test_login_account_prolem_user(self):
        login_page = LoginPage(self.driver)
        account = Account(TestData.FAKE_USERNAME2, TestData.PASSWORD)
        login_page.login(account)
        login_page.click_img_erro(1)
        time.sleep(10)



    #def test_login_account_performance_glitch_user(self):
       # account = Account(TestData.FAKE_USERNAME3, TestData.PASSWORD)
       # login_page.login(account)




if __name__ == "__main__":
    unittest.main()
