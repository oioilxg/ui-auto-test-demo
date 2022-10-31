import unittest

from page.login_page import LoginPage

class TestCase(unittest.TestCase):
    def test_login(self):
        lp = LoginPage()
        lp.login()