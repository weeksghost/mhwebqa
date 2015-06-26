from selenium.webdriver.common.by import By
from page import Page


class Base(Page):

    @property
    def footer(self):
        return self.Footer(self.testsetup)

    class Footer(Page):

        footer_links_list = [
            {
                'locator': (By.CSS_SELECTOR, '#fsl > a:nth-child(1)'),
                'url_suffix': '//www.google.com/intl/en/ads/?fg=1',
            },
        ]



