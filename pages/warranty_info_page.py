
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

from selenium.webdriver.common.by import By

class WarrantyInfoPage(BasePage):
    def __init__(self, driver):
        self.valid_sn = '1863552437'
        self.invalid_sn = '186355243'
        self.invalid_short_sn = '1'
        self.invalid_long_sn = '1111111111111111111111111111'
        self.sn_input = '//input[@id="SerialNumber"]'
        self.query_btn_css = '.btn-block'
        self.error_msg = '//span[@class="field-validation-error"]'
        self.accept_cookie_btn = '//button[@id="onetrust-accept-btn-handler"]'

        self.error_short_sn = 'Minimum 6 characters required'
        self.error_blank_sn = 'Please specify a serial number'
        self.error_long_sn = 'Please enter a valid serial number'
        self.error_no_result = "We couldn't find a product with this serial number. Please double-check the serial number and try again."

        self.result_no_match_css = '.c-bb-tile'
        self.result_query_sn_css = '.c-result-tile__highlight'
        self.result_dl_css = '.c-result-tile__dl'
        self.result_image_css = '.o-aspect-ratio__element'
        self.correct_product_info = [
            'CLICKSHARE CX-50 SET NA',
            'R9861522NA',
            '09/28/2020 00:00:00',
            '09/27/2021 00:00:00',
            '01/01/0001 00:00:00'
        ]
        self.correct_product_img_url = "https://az877327.vo.msecnd.net/~/media/clickshare2020/images/product%20shots%20-%20transparent/cx-50_buttons_top%20png.png?v=1"

        super().__init__(driver)

    def dismiss_cookie_popup(self):
        WebDriverWait(self.driver, self.timeout).until(EC.element_to_be_clickable((By.XPATH, self.accept_cookie_btn))).click()
        WebDriverWait(self.driver, self.timeout).until(EC.invisibility_of_element_located((By.XPATH, self.accept_cookie_btn)))

    def type_sn(self, sn):
        element = self.driver.find_element(By.XPATH, self.sn_input)
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

    def search_invalid_sn(self):
        self.type_sn(self.invalid_sn)
        self.click_get_info_btn()

    def click_get_info_btn(self):
        element = self.driver.find_element(By.CSS_SELECTOR, self.query_btn_css)
        element.click()

    def check_error_toast(self, msg):
        element = ''
        elements = self.driver.find_elements(By.XPATH, self.error_msg)
        for ele in elements:
            if ele.get_attribute('style') != 'display: none;':
                element = ele
        assert element.text == msg

    def verify_product_info(self):
        WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.result_query_sn_css)))
        WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.result_dl_css)))
        WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.result_image_css)))
        sn = self.driver.find_element(By.CSS_SELECTOR, self.result_query_sn_css)
        assert sn.text == self.valid_sn
        element = self.driver.find_element(By.CSS_SELECTOR, self.result_dl_css)
        dd = element.find_elements(By.XPATH, './/dd')
        for m in range(len(dd)):
            assert dd[m].text == self.correct_product_info[m]
        img = self.driver.find_element(By.CSS_SELECTOR, self.result_image_css)
        assert img.get_attribute('src') == self.correct_product_img_url

    def verify_no_result_info(self):
        WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.result_query_sn_css)))
        sn = self.driver.find_element(By.CSS_SELECTOR, self.result_query_sn_css)
        assert sn.text == self.invalid_sn
        element = self.driver.find_element(By.CSS_SELECTOR, self.result_no_match_css)
        assert element.find_element(By.XPATH, './/div').find_element(By.XPATH, './/p').text == self.error_no_result

    def verify_blank_sn_error(self):
        self.check_error_toast(self.error_blank_sn)

    def verify_short_sn_error(self):
        self.check_error_toast(self.error_short_sn)

    def verify_long_sn_error(self):
        self.check_error_toast(self.error_long_sn)