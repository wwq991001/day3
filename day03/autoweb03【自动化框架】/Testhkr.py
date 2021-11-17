from selenium import webdriver
from unittest import TestCase
from ddt import ddt
from ddt import data
from InitPage import InitPage
from LoginOperation import LoginOpera
import time
import GoogleChrome
from xlutils.copy import copy

GoogleChrome.Chrome()

newwb = copy(InitPage.wb)
ws = newwb.get_sheet(0)
@ddt
class TestHkr(TestCase):

    global newwb, ws
    # 在所有用例执行前执行
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:8080/HKR")
        self.driver.maximize_window()

    # 在所有用例执行后执行
    def tearDown(self) -> None:
        self.driver.quit()




    @data(*InitPage.loginSuccessData)
    def testLoginSuccess(self,testdata):

        username = testdata["姓名"]
        password = testdata["密码"]
        expect = testdata["期望数据"]
        via = testdata["是否通过"]
        time1 = time.strftime('%Y-%m-%d', time.localtime(time.time()))

        login = LoginOpera(self.driver)

        # 执行登陆的三项惭怍
        login.login(username, password)


        # 获取实际结果
        result = login.getLoginSuccessResult()

        time.sleep(3)

        if expect == result:
            ws.write(via, 3, "通过")
            ws.write(via, 5, time1)
            newwb.save("HKR.xls")
        else:
            ws.write(via, 3, "不通过")
            ws.write(via, 5, time1)
            newwb.save("HKR.xls")

        # 断言
        self.assertEqual(str(expect),str(result))



    @data(*InitPage.loginErrorData)
    def testLoginError(self,testdata):

        username = testdata["姓名"]
        password = testdata["密码"]
        expect = testdata["期望数据"]
        via = testdata["是否通过"]
        time1 = time.strftime('%Y-%m-%d', time.localtime(time.time()))

        login = LoginOpera(self.driver)

        # 执行登陆的三项惭怍
        login.login(username,password)


        # 获取实际结果
        result = login.getLoginErrorResult()

        time.sleep(3)

        if expect == result:
            ws.write(via, 3, "通过")
            ws.write(via, 5, time1)
            newwb.save("HKR.xls")
        else:
            ws.write(via, 3, "不通过")
            ws.write(via, 5, time1)
            newwb.save("HKR.xls")

        # 断言
        self.assertEqual(expect, result)





















