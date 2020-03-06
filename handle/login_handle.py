#coding:utf-8
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page.login_page import LoginPage

#操作层--用来输入用户信息
class LoginHandle(object):

    def __init__(self,driver):
        self.login_page = LoginPage(driver)

    #输入用户名
    def send_user_name(self,user):
        login_user = self.login_page.get_user_element()
        login_user.clear()
        login_user.send_keys(user)

    # 输入密码
    def send_user_pwd(self,pwd):
        login_pwd = self.login_page.get_pwd_element()
        login_pwd.clear()
        login_pwd.send_keys(pwd)

     #获取提示信息内容
    def send_msg(self):
        return self.login_page.get_text_element()

        # 点击按钮
    def btn_submit(self):
        try:
            self.login_page.get_btn_element().click()
        except StaleElementReferenceException:
            self.login_page.get_btn_element().click()

    def submit(self):
        self.login_page.get_btn_element().click()

    #退出登录按钮
    def logout_btn(self):
        return self.login_page.get_logout_btn()
