from selenium.webdriver.common.by import By
from pages.base import Base


class SalePage(Base):

    def go_to_page(self):
        self.open('/default/sale-discount')
