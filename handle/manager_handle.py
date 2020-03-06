#coding:utf-8
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page.manager_page import ManagerPage

#操作层--用来输入用户信息
class ManagerHandle(object):

    def __init__(self,driver):
        self.manager_page = ManagerPage(driver)


    #获取ifame的个数
    def get_manager_len(self):
        return self.manager_page.get_ul_manager()

    #获取iframe的值
    def get_manager_value(self):
        return self.manager_page.get_li_span()


