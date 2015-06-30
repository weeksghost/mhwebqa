from bs4 import BeautifulSoup
import requests
import pytest


#@pytest.mark.skip_selenium
class TestSaleLinks(object):


    @pytest.mark.nondestructuve
    def test_left_dropdown_links(self, mozwebqa):
        response = requests.get(self.base_url + '/default/sale-discount')
        soup = BeautifulSoup(response.text)
        sale_nav_items = soup.find('ul', class_='sale-category-nav')
        for link in sale_nav_items.select('li a[href]'):
            resp = requests.get(self.base_url + link['href'])
            self.selenium.get(self.base_url + link['href'])
