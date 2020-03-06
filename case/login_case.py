#coding:utf-8
from business.login_business import LoginBusiness
from selenium import webdriver
import unittest
#登录的用例
class LoginTest(unittest.TestCase):


    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://h5-qa.admin.yuedaowang.com/#/driverSettle")
        self.login_busi = LoginBusiness(self.driver)

     #用户名错误
    def test_login_error_user(self):
        login_user = self.login_busi.login_user_error()
        if login_user == True:
            print("用户名错误，登录失败，此条case执行失败")

    #密码错误
    def test_login_errorb_pwd(self):
        login_pwd = self.login_busi.login_pwd_error()
        if login_pwd == True:
            print("密码错误，登录失败，此条case执行失败")

    #登录成功
    def test_login_success(self):
        success = self.login_busi.login_success()
        if success == True:
            print('登录成功')

    # @classmethod
    # def tearDownClass(cls):
    #     cls.driver.close()
    #     # pass

if __name__ == "__main__":
   unittest.main()