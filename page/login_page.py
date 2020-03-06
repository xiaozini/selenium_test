#coding:utf-8
from base.find_element import FindElement


#读取元素的信息，然后用handle层读取该层
class LoginPage(object):

    def __init__(self,driver):
        self.find_element = FindElement(driver)

    def get_user_element(self):
        return self.find_element.get_element("user_name")

    def get_pwd_element(self):
        return self.find_element.get_element("user_pwd")

    def get_btn_element(self):
        return self.find_element.get_element("btn")

    def get_text_element(self):
        return self.find_element.get_element("msg")

    def get_logout_btn(self):
        return self.find_element.get_element("logout")

# if __name__ == '__main__':
#     file_path = os.path.join(os.getcwd()+'/report/'+"html_case.html")
#     with open(file_path,'wb') as f1:
#         suite = unittest.TestSuite()
#         suite.addTest(LoginPage(""))
