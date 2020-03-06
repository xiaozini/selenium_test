#coding:utf-8
import os
import configparser

proDir = os.path.dirname(os.path.abspath(__file__))
configPath = os.path.join(proDir,"config.ini")


class ReadIni(object):

    def __init__(self):
        self.cf = configparser.ConfigParser()
        self.cf.read(configPath)

    def get_element(self,param):
        value = self.cf.get("login_element",param)
        return value

    def get_user(self, param):
        value = self.cf.get("User", param)
        return value

    def get_manager(self, param):
        value = self.cf.get("IframeManager", param)
        return value

    def get_manager_num(self, param):
        value = self.cf.get("Manager_Num", param)
        return value


#
# if __name__ == '__main__':
#     read_ini = ReadIni()
#     print(read_ini.get_element("login_element","user_name"))