from selenium.webdriver.common.by import By
from base import Base


class HomePage(Base):

    _base_locator = (By.NAME, 'q')
    _page_title = u'Google'
    _search_locator = (By.ID, 'lst-ib')
    _results_locator = (By.CSS_SELECTOR, '#navcnt')

    def __init__(self, testsetup):
        super(HomePage, self).__init__(testsetup)

    def go_to_page(self):
        self.open('')

    def search_text(self, custom_search):
        self.selenium.find_element(*self._base_locator).send_keys(custom_search)

    def search_box_submit(self):
        search_box = self.find_element(*self._search_locator)
        search_box.submit()

    def is_result_output_present(self):
        return self.is_element_visible(*self._results_locator)
