from base_test import *
from pages.warranty_info_page import *
import time

class TestWarranty(BaseTest):
    def test_successful_query_info(self):
        warranty_info_page = WarrantyInfoPage(self.driver)
        warranty_info_page.dismiss_cookie_popup()
        warranty_info_page.search_valid_sn()

    def test_query_invalid_sn(self):
        warranty_info_page = WarrantyInfoPage(self.driver)
        warranty_info_page.dismiss_cookie_popup()
        warranty_info_page.search_blank_sn()
        warranty_info_page.search_short_sn()
        warranty_info_page.search_long_sn()
