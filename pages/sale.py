from selenium.webdriver.common.by import By
import requests
from urlparse import urlparse
from bs4 import BeautifulSoup
from pages.base import Base


class SalePage(Base):

    def go_to_page(self):
        self.open('/default/sale-discount')

    def window_max(self):
        self.selenium.maximize_window()

    def resize_window(self, width, height):
        self.selenium.set_window_size(width, height)

    _left_dropdown_list = (By.CLASS_NAME, 'sale-subcategory-nav')

    _left_dropdown_elements = (By.CSS_SELECTOR, 'body > div.wrapper > div > div > div.row.row-sale-content.row-two-column > div.row-content-secondary')

    _drop_down_one = (By.CSS_SELECTOR, 'body > div.wrapper > div > div > div.row.row-sale-content.row-two-column > div.row-content-secondary > ul > li:nth-child(1) > h3')

    _drop_down_two = (By.CSS_SELECTOR, 'body > div.wrapper > div > div > div.row.row-sale-content.row-two-column > div.row-content-secondary > ul > li:nth-child(2) > h3')

    _active_dropdown = (By.CLASS_NAME, 'active')

    def drop_down_one(self):
        self.selenium.find_element(*self._drop_down_one).click()

    def drop_down_two(self):
        self.selenium.find_element(*self._drop_down_two).click()
