from selenium.webdriver.common.by import By
from page import Page

"""Empty base page object

"""


class Base(Page):

    @property
    def base_method(self):
        pass

    class PageObjectClass(Page):
        pass
