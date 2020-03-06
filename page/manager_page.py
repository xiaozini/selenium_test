#coding:utf-8
from base.find_element import FindElement


#读取元素的信息，然后用handle层读取该层
class ManagerPage(object):

    def __init__(self,driver):
        self.find_element = FindElement(driver)

    def get_ul_manager(self):
        return self.find_element.get_element("ul_manager")

    def get_li_span(self):
        return self.find_element.get_element("li_span")

    def get_num_li(self):
        return self.find_element.get_element("span_num")
