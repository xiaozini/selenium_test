from business.iframe_business import IframeBusiness
from selenium import webdriver
import unittest

class IframeManagerTest(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://h5-qa.admin.yuedaowang.com/#/")
        self.iframe_busi = IframeBusiness(self.driver)

    # def test_span_value(self):
    #     spans_value = self.iframe_busi.manager_value()
    #     if spans_value == True:
    #         print("span数据正确")

    def test_span_num(self):
        span_num = self.iframe_busi.manager_num()
        if span_num == True:
            print("span个数正确")


if __name__ == "__main__":
   unittest.main()
