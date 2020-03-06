#coding:utf-8
from selenium import webdriver
from utils.read_ini import ReadIni
from base.find_element import FindElement

read_ini = ReadIni("User")
user = read_ini.get_value("user")
pwd = read_ini.get_value("pwd")

class LoginFunction(object):
    def __init__(self,url):
        self.driver = self.get_driver(url)

    def get_driver(self,url):
        driver = webdriver.Chrome()
        driver.get(url)
        driver.maximize_window()
        return driver

    #输入用户信息
    def send_user_info(self,element,data):
        element.send_keys(data)

    #定位用户信息
    def get_user_element(self,key):
        find_element = FindElement(self.driver)
        user_element = find_element.get_element(key)
        return user_element

    def main(self):
        eles = self.get_user_element('user_name')
        self.send_user_info(eles[0],user)
        self.send_user_info(eles[1],pwd)
        # eles[0].send_keys(user)
        # eles[1].send_keys(pwd)
        self.get_user_element('btn').click()
        self.driver.close()


if __name__ == '__main__':
    login_func = LoginFunction("https://h5-qa.admin.yuedaowang.com/#/login")
    login_func.main()
