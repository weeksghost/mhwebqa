import pytest
from pages.sale import SalePage


class TestSalePage:

    @pytest.mark.nondestructive
    def test_dropdowns(self, mozwebqa):
        sale_page = SalePage(mozwebqa)
        sale_page.go_to_page()
        sale_page.drop_down_one()
        assert sale_page.is_element_present(*sale_page._active_dropdown)
        sale_page.drop_down_two()
        assert sale_page.is_element_present(*sale_page._active_dropdown)
