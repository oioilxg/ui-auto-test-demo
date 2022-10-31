import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

#  新建一个类继承uniittest
class TestCase(unittest.TestCase):
    def test_login(self):
        #selenium4.0 用service 启动驱动
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        # 驱动加载等待时间
        driver.implicitly_wait(15)
        #加载页面
        driver.get('https://www.baidu.com')
        #定位元素
        driver.find_element(By.ID, 'kw').send_keys('上海天气预报')

        time.sleep(5)
        driver.quit()