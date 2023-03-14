import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.confirm_booking_page import ConfirmBookingPage

class ContactPage(BasePage):
    def __init__(self, driver): 
        
        self.phone_number = '0900123456'
        self.contact_name = 'test1test'

        self.submit_button = '//button[@type="submit"]'
        self.back_button = 'button//[@id="contact-form"]'
        self.privacy_policy = '//label[@for="privacy-policy"]'
        self.footer = '//span[@class="sc-iqcoie"]'
        super().__init__(driver)
    
    def enter_contact_name(self):
        self.driver.find_element(By.ID, 'name').send_keys(self.contact_name)
        
    def enter_phone_number(self):
        self.driver.find_element(By.ID, 'phone').send_keys(self.phone_number)

    def click_policy_checkbox(self):
        f = self.driver.find_element_by_xpath(self.footer)
        f.location_once_scrolled_into_view
        time.sleep(5)
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, self.footer)))
        element = self.driver.find_element_by_xpath(self.privacy_policy)
        #element.location_once_scrolled_into_view
        element.click()
    
    def click_submit_button(self):
        self.driver.find_element_by_xpath(self.submit_button).click()
        return ConfirmBookingPage(self.driver)

    def fill_in_contact_and_submit(self):
        self.enter_contact_name()
        self.enter_phone_number()
        self.click_policy_checkbox()
        self.click_submit_button()
        return ConfirmBookingPage(self.driver)