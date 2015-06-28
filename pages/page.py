from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from unittestzero import Assert
import time


class Page(object):
    """
    Base class for all pages
    """

    def __init__(self, testsetup):
        self.testsetup = testsetup
        self.base_url = testsetup.base_url
        self.selenium = testsetup.selenium
        self.timeout = testsetup.timeout
        self._selenium_root = hasattr(
            self, '_root_element') and self._root_element or \
            self.selenium

    def refresh(self):
        self.selenium.refresh()

    def open(self):
        self.selenium.get(self.base_url)
        self.selenium.maximize_window()

    @property
    def page_title(self):
        WebDriverWait(self.selenium, self.timeout).until(lambda s: self.selenium.title)
        return self.selenium.title

    @property
    def is_the_current_page(self):
        if self._page_title:
            Assert.equal(self.page_title, self._page_title,
                         "Expected page title: %s. Actual page title: %s" % (self._page_title, self.page_title))
        return True

    def is_element_visible(self, *locator):
        try:
            return self.selenium.find_element(*locator).is_displayed()
        except (ElementNotVisibleException, NoSuchElementException):
            # this will return a snapshot, which takes time.
            return False

    def is_element_present(self, *locator):
        """
        Return true if the element at the specified locator is present in the DOM.
        Note: It returns false immediately if the element is not found.
        """
        self.selenium.implicitly_wait(0)
        try:
            self._selenium_root.find_element(*locator)
            return True
        except NoSuchElementException:
            return False
        finally:
            # set the implicit wait back
            self.selenium.implicitly_wait(self.testsetup.default_implicit_wait)

    def wait_until_element_visible(self, element):
        # overriding timeout here to higher value of 360
        timeout = 30
        self.selenium.execute_script("window.scrollTo(0, 0)")
        WebDriverWait(self.selenium, timeout).until(EC.visibility_of(element))

    def wait_for_element_present(self, *locator):
        """Wait for the element at the specified locator to be present in the DOM."""
        count = 0
        while not self.is_element_present(*locator):
            time.sleep(1)
            count += 1
            if count == self.timeout:
                raise Exception("{} is not visible".format(*locator))

    def wait_for_element_visible(self, *locator):
        """Wait for the element at the specified locator to be visible in the browser."""
        count = 0
        while not self.is_element_visible(*locator):
            time.sleep(1)
            count += 1
            if count == self.timeout:
                raise Exception("{} is not visible".format(*locator))

    def wait_for_element_not_present(self, *locator):
        """Wait for the element at the specified locator to be not present in the DOM."""
        self.selenium.implicitly_wait(0)
        try:
            WebDriverWait(self.selenium, self.timeout).until(lambda s: len(self.find_elements(*locator)) < 1)
            return True
        except TimeoutException:
            Assert.fail(TimeoutException)
        finally:
            self.selenium.implicitly_wait(self.testsetup.default_implicit_wait)

    def select_option(self, value, locator):
        dropdown = self.selenium.find_element(*locator)
        option_found = False
        all_options = dropdown.find_elements_by_tag_name("option")
        for option in all_options:
            if option.get_attribute("value") == value:
                option_found = True
                option.click()
                break
        if option_found is False:
            raise Exception("Option '" + value + "' was not found, thus not selectable.")

    def get_url_current_page(self):
        return(self.selenium.current_url)

    def find_element(self, *locator):
        """Return the element at the specified locator."""
        return self._selenium_root.find_element(*locator)

    def find_elements(self, *locator):
        """Return a list of elements at the specified locator."""
        return self._selenium_root.find_elements(*locator)

    def force_wait(self, wait_time):
        try:
            time.sleep(int(wait_time))
        except TimeoutException:
            Assert.fail(TimeoutException)
        finally:
            self.selenium.implicitly_wait(self.testsetup.default_implicit_wait)

class PageRegion(Page):
    """Base class for a page region (generally an element in a list of elements)."""

    def __init__(self, testsetup, element):
        self._root_element = element
        Page.__init__(self, testsetup)
