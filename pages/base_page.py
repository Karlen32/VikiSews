from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, timeout: int = 15):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    # =====================
    #       БАЗОВЫЕ WAIT
    # =====================

    def wait_visible(self, locator):
        """Ждём, пока элемент станет видимым, и возвращаем его."""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_clickable(self, locator):
        """Ждём, пока элемент станет кликабельным, и возвращаем его."""
        return self.wait.until(EC.element_to_be_clickable(locator))

    def wait_not_visible(self, locator):
        """Ждём, пока элемент исчезнет (или станет невидимым)."""
        return self.wait.until_not(EC.visibility_of_element_located(locator))

    # =====================
    #       ДЕЙСТВИЯ
    # =====================

    def click(self, locator):
        """Клик по элементу с ожиданием кликабельности."""
        self.wait_clickable(locator).click()

    def js_click(self, locator):
        """JS-клик по элементу (на случай перекрытий/анимаций)."""
        element = self.wait_visible(locator)
        self.driver.execute_script("arguments[0].click();", element)

    def send_keys(self, locator, value: str, clear: bool = True):
        """Ввод текста в поле с ожиданием видимости."""
        el = self.wait_visible(locator)
        if clear:
            el.clear()
        el.send_keys(value)
        return el

    # =====================
    #      СКРОЛЛЫ / ХОВЕР
    # =====================

    def scroll_into_view(self, locator, block: str = "center"):
        """Скролл к элементу через scrollIntoView."""
        element = self.wait_visible(locator)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: arguments[1]});",
            element,
            block,
        )
        return element

    def hover(self, locator):
        """Наведение курсора на элемент."""
        from selenium.webdriver.common.action_chains import ActionChains

        element = self.wait_visible(locator)
        ActionChains(self.driver).move_to_element(element).perform()
        return element

    # =====================
    #       URL / ПРОЧЕЕ
    # =====================

    def wait_url_contains(self, fragment: str):
        """Ждём, пока URL будет содержать подстроку."""
        self.wait.until(EC.url_contains(fragment))

    def find_elements(self, locator):
        """Удобный помощник: список элементов без дополнительных ожиданий."""
        return self.driver.find_elements(*locator)
