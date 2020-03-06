from selenium import webdriver
import unittest

class BaseTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get("https://h5-qa.admin.yuedaowang.com/#/driverSettle")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
