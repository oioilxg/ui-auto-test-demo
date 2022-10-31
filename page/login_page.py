from selenium.webdriver.common.by import By
from base.base_page import BasePage

class LoginPage(BasePage):
    #页面元素
    user_loc = (By.ID, "username")
    pass_loc = (By.ID, "username")
    login_button = (By.ID, "login_button")

    def login(self, username='', password=''):
        self.send_keys(LoginPage.user_loc, username)
        self.send_keys(LoginPage.pass_loc, password)
        self.click(LoginPage.login_button)