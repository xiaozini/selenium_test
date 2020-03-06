#coding:utf-8
from config.read_ini import ReadIni

class FindElement(object):
    def __init__(self,driver):
        self.driver = driver

    def get_element(self,key):
        readini = ReadIni()
        data = readini.get_element(key)
        key = data.split(">")[0]
        value = data.split(">")[1]
        try:
            if key == 'id':
                return self.driver.find_element_by_id(value)
            elif key == 'name':
                return self.driver.find_element_by_name(value)
            elif key == 'class_name':
                return self.driver.find_element_by_class_name(value)
            elif key == 'link_text':
                return self.driver.find_element_by_link_text(value)
            elif key == 'xpath':
                return self.driver.find_element_by_xpath(value)
            elif key == 'css_selector':
                return self.driver.find_elements_by_css_selector(value)
            elif key == 'css_selectors':
                return self.driver.find_element_by_css_selector(value)
        except:
            return None


    def get_user(self,key):
        readini = ReadIni()
        data = readini.get_element(key)
        print(data)



