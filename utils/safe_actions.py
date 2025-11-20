from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait


def safe_click(driver, locator, timeout=15):
    wait = WebDriverWait(driver, timeout, ignored_exceptions=(StaleElementReferenceException,))

    def _try(_driver):
        try:
            el = _driver.find_element(*locator)
            if el.is_displayed() and el.is_enabled():
                _driver.execute_script("arguments[0].scrollIntoView({block:'center'});", el)
                _driver.execute_script("arguments[0].click();", el)
                return True
        except StaleElementReferenceException:
            return False
        return False

    wait.until(_try)
