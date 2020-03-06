#coding:utf-8
#执行操作 调用Handle
from handle.manager_handle import ManagerHandle
from config.read_ini import ReadIni
from time import sleep

class IframeBusiness(object):
    def __init__(self,driver):
        self.read_ini = ReadIni()
        self.login_handle = ManagerHandle(driver)

   #span个数比较
    def manager_num(self):
        span_num = self.read_ini.get_user("span_num")
        if span_num == self.login_handle.get_manager_len():
            return True
        else:
            return False
            print('iframe的个数为：{}'.format(span_num))


    # def manager_value(self):
    #      list_span = self.read_ini.get_user("span_value")
    #      if list_span == self.login_handle.get_manager_value():
    #          return True
    #      else:
    #          return False
    #          print('iframe的值为：{}'.format(list_span))


