from selenium import webdriver
from selenium.webdriver.common.by import By

def Chrome():
    option = webdriver.ChromeOptions
    option.binary_location = r'D:\Google\Chrome\Application\chrome.exe'