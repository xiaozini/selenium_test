#coding:utf-8
import unittest
import os

case_path = os.path.join(os.getcwd(),'case')
class RunCase(unittest.TestCase):
    def test_case1(self):
        suite = unittest.defaultTestLoader.discover(case_path,"unittest_*.py")
        unittest.TextTestRunner().run(suite)

if __name__ == '__main__':
    unittest.main()