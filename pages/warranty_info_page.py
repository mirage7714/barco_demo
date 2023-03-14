
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from pages.contact_page import ContactPage
from selenium.webdriver.common.by import By
import time

class WarrantyInfoPage(BasePage):
    def __init__(self, driver):
        self.valid_sn = '1863552437'
        self.invalid_short_sn = '1'
        self.invalid_long_sn = '111111111111111'
        self.sn_input = '//input[@id="SerialNumber"]'
        self.query_btn_css = '.btn-block'
        self.error_hint = '//span[@class="field-validation-error"]'
        self.accept_cookie_btn = '//button[@id="onetrust-accept-btn-handler"]'

        self.error_short_sn = 'Minimum 6 characters required'

        super().__init__(driver)

    def dismiss_cookie_popup(self):
        WebDriverWait(self.driver, self.timeout).until(EC.element_to_be_clickable((By.XPATH, self.accept_cookie_btn))).click()
        WebDriverWait(self.driver, self.timeout).until(EC.invisibility_of_element_located((By.XPATH, self.accept_cookie_btn)))

    def type_sn(self, sn):
        element = self.driver.find_element_by_xpath(self.sn_input)
        element.click()
        element.clear()
        element.send_keys(sn)

    def search_valid_sn(self):
        self.type_sn(self.valid_sn)
        self.click_get_info_btn()

    def search_blank_sn(self):
        self.type_sn('')
        self.click_get_info_btn()

    def search_short_sn(self):
        self.type_sn(self.invalid_short_sn)
        self.click_get_info_btn()

    def search_long_sn(self):
        self.type_sn(self.invalid_long_sn)
        self.click_get_info_btn()

    def click_get_info_btn(self):
        element = self.driver.find_element(By.CSS_SELECTOR, self.query_btn_css)
        element.click()

    def check_error_toast(self, msg):
        #WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located((By.XPATH, self.error_hint)))
        element = self.driver.find_element_by_xpath(self.error_hint)
        print(element.text)
        assert element.text == msg


    def verify_short_sn_error(self):
        self.check_error_toast(self.error_short_sn)