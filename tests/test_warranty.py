from base_test import *
from pages.warranty_info_page import *

class TestWarranty(BaseTest):
    def test_successful_query_info(self):
        warranty_info_page = WarrantyInfoPage(self.driver)
        warranty_info_page.dismiss_cookie_popup()
        warranty_info_page.search_valid_sn()
        warranty_info_page.verify_product_info()

    def test_query_invalid_sn(self):
        warranty_info_page = WarrantyInfoPage(self.driver)
        warranty_info_page.dismiss_cookie_popup()
        warranty_info_page.search_blank_sn()
        warranty_info_page.verify_blank_sn_error()
        warranty_info_page.search_short_sn()
        warranty_info_page.verify_short_sn_error()
        warranty_info_page.search_long_sn()
        warranty_info_page.verify_long_sn_error()

    def test_query_with_no_result(self):
        warranty_info_page = WarrantyInfoPage(self.driver)
        warranty_info_page.dismiss_cookie_popup()
        warranty_info_page.search_invalid_sn()
        warranty_info_page.verify_no_result_info()