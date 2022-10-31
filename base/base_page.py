from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
class BasePage:

    def __init__(self):
        global driver

        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver = self.driver

        driver.implicitly_wait(15)

        driver.get(url)


    #定位元素
    def locator_element(self,loc):
        return self.driver.find_element(*loc)

    def send_keys(self, loc, value):
        return self.locator_element(loc).send_keys(value)

    def click(self, loc):
        self.locator_element(loc).click()