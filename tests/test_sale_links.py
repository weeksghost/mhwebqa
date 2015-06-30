import pytest
import requests
from bs4 import BeautifulSoup
from pages.sale import SalePage

@pytest.mark.skip_selenium
class TestSaleLinks:

    @pytest.mark.nondestructive
    def test_left_dropdown_links(self, mozwebqa):
        sale_page = SalePage(mozwebqa)
        response = requests.get(mozwebqa.base_url + '/default/sale-discount')
        soup = BeautifulSoup(response.content)
        sale_nav_items = soup.find('ul', class_='sale-category-nav')
        for link in sale_nav_items.select('li a[href]'):
            assert sale_page.get_response_code(
                mozwebqa.base_url + link['href']) == 200
