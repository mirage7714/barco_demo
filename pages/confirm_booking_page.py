import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class ConfirmBookingPage(BasePage):
    def __init__(self, driver):

        self.calendar_add_button = '//button[@name="calendarModalAcceptButton"]'
        self.calendar_reject_button = 'button//[@name="calendarModalCloseButton"]'
        self.privacy_policy = '//label[@for="privacy-policy"]'
        self.cancel_reservation_button = '//button[@data-cy="rsv-cancel-button"]'

        super().__init__(driver)
    
    def click_calendar_reject_button(self):
        time.sleep(5)
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, self.calendar_reject_button))).click()

    def cancel_reservation(self):
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, self.cancel_reservation_button))).click()
        alert = self.driver.switch_to.alert
        alert.accept()
        time.sleep(10)
        url = self.driver.current_url
        assert ('cancelled' in url)