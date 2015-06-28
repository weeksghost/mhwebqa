import pytest
from pages.home import HomePage
from base_test import BaseTest


class TestGoogleSearch(BaseTest):

    @pytest.mark.nondestructive
    def test_search_selenium_from_google(self, mozwebqa):
        home_page = HomePage(mozwebqa)
        input_text = 'selenium'
        home_page.go_to_page()
        home_page.is_the_current_page
        home_page.search_text(input_text)
        home_page.search_box_submit()
        home_page.force_wait(1)
        assert home_page.is_result_output_present(), 'Locator not working.'
