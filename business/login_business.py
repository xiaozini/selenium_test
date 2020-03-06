#coding:utf-8
#执行操作 调用Handle
from handle.login_handle import LoginHandle
from config.read_ini import ReadIni
from time import sleep

class LoginBusiness(object):
    def __init__(self,driver):
        self.read_ini = ReadIni()
        self.login_handle = LoginHandle(driver)

   #执行操作
    def login_user_error(self):
        user = self.read_ini.get_user("user_error")
        pwd = self.read_ini.get_user("pwd_true")
        self.login_base(user,pwd)
        if self.error_test() == "用户名或密码不对":
            print("用户检验成功")
            return True
        else:
            return False

    def login_pwd_error(self):
        user = self.read_ini.get_user("user_true")
        pwd = self.read_ini.get_user("pwd_error")
        self.login_base(user, pwd)
        if self.error_test() == "用户名或密码不对":
            print("密码检验成功")
            return True
        else:
            return False

    def login_base(self, user, pwd):

        self.login_handle.send_user_name(user)
        self.login_handle.send_user_pwd(pwd)
        self.login_handle.btn_submit()

    #登录成功
    def login_success(self):
        user = self.read_ini.get_user("user_true")
        pwd = self.read_ini.get_user("pwd_true")
        self.login_base(user, pwd)
        sleep(2)
        return self.logout_btn()

    def error_test(self):
        self.login_handle.send_msg()

    def logout_btn(self):
        return self.login_handle.logout_btn()

