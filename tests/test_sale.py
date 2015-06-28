import pytest
from pages.sale import SalePage


class TestSalePage:

    @pytest.mark.nondestructive
    def test_dropdowns(self, mozwebqa):
        sale_page = SalePage(mozwebqa)
        sale_page.go_to_page()
