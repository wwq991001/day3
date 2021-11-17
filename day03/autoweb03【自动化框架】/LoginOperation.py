from selenium import webdriver
import time
from selenium.webdriver.common.by import By

class LoginOpera:
    # 保证driver使用全局同一个
    def __init__(self,driver):

        self.driver = driver

    # 登陆
    def login(self,username,password):
            # self.driver.find_element_by_xpath("//*[@id='loginname']").send_keys(username)
            self.driver.find_element(By.XPATH, "//*[@id='loginname']").send_keys(username)
            # self.driver.find_element_by_xpath("//*[@id='password']").send_keys(password)
            self.driver.find_element(By.XPATH, "//*[@id='password']").send_keys(password)
            # self.driver.find_element_by_xpath("//*[@id='submit']").click()
            self.driver.find_element(By.XPATH, "//*[@id='submit']").click()

    # 获取登陆成功的实际结果
    def   getLoginSuccessResult(self):
        return self.driver.title

    # 获取失败的结果数据
    def getLoginErrorResult(self):
        # return self.driver.find_element_by_xpath("//*[@id='msg_uname']").text
        return self.driver.find_element(By.XPATH, "//*[@id='msg_uname']").text






















