import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class BaseTest(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.add_argument('disable-infobars')
        options.add_argument("--disable-extensions")
        options.add_argument("--start-fullscreen")
        options.add_argument('--disable-gpu')

        self.driver = webdriver.Chrome(executable_path='chromedriver.exe')
        self.driver.get("https://www.barco.com/en/clickshare/support/warranty-info")

    def tearDown(self):
        self.driver.close()

