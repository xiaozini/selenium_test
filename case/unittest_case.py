#coding:utf-8
import unittest,os
class FirstCase(unittest.TestCase):
    def setUp(self):
        print('aaa')

    def test_first01111(self):
        print("这是第一个case")
        self.assertEqual("aaa",'aa','该条数据错误')

    def test_first01112(self):
        print("这是第二条case")

    def tearDown(self):
        print("sss")
        #错误截图
        for method_name,error in self._outcome.errors:
            if error:
                case_name = self._testMethodName#case名称
                file_path = os.path.join(os.getcwd()+"/report/"+case_name+".png")
                self.driver.save_screenshot(file_path)
        self.driver.close()


if __name__ == '__main__':
    unittest.main()