"""
Helper-методы для тестов - уменьшение дублирования кода
"""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators.base_locators import BaseLocators
from locators.vykrojki_locators import VykrojkiLocators
from locators.checkout_locators import CheckoutLocators
import time

# Константы для таймаутов
DEFAULT_TIMEOUT = 15
SHORT_TIMEOUT = 10
LONG_TIMEOUT = 30


def navigate_to_patterns(driver, timeout=DEFAULT_TIMEOUT):
   
    WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable(BaseLocators.PATTERNS_SUBMENU_LINK)
    ).click()
    
    WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable(BaseLocators.ALL_PATTERNS_LINK)
    ).click()
    
    WebDriverWait(driver, timeout).until(
        EC.url_contains("/vykrojki/vse-vykrojki/")
    )


def select_product_params(driver, height_option, size_option, timeout=DEFAULT_TIMEOUT, use_modal=False):
    """
    Выбор параметров товара (рост и размер)
    
    Args:
        driver: WebDriver instance
        height_option: локатор опции роста (готовый локатор, например VykrojkiLocators.HEIGHT_OPTION_162_168)
                      ИЛИ строка для генерации (например, "162-168")
        size_option: локатор опции размера (готовый локатор, например VykrojkiLocators.SIZE_OPTION_XL)
                     ИЛИ строка для генерации (например, "XL", "M", "36")
        timeout: время ожидания
        use_modal: использовать локаторы для модального окна (True) или для страницы товара (False)
    """
    if use_modal:
        height_dropdown = VykrojkiLocators.HEIGHT_DROPDOWN_BUTTON_MODAL
        height_selected = VykrojkiLocators.HEIGHT_SELECTED_VALUE_MODAL
        size_dropdown = VykrojkiLocators.SIZE_DROPDOWN_BUTTON_MODAL
        size_selected = VykrojkiLocators.SIZE_SELECTED_VALUE_MODAL
    else:
        height_dropdown = VykrojkiLocators.HEIGHT_DROPDOWN_BUTTON
        height_selected = VykrojkiLocators.HEIGHT_SELECTED_VALUE
        size_dropdown = VykrojkiLocators.SIZE_DROPDOWN_BUTTON
        size_selected = VykrojkiLocators.SIZE_SELECTED_VALUE

    # Если передан готовый локатор (tuple), используем его
    # Если передана строка, генерируем локатор
    if isinstance(height_option, str):
        if use_modal:
            height_option_locator = VykrojkiLocators.height_option_modal(height_option)
        else:
            height_option_locator = VykrojkiLocators.height_option(height_option)
    else:
        height_option_locator = height_option

    if isinstance(size_option, str):
        if use_modal:
            size_option_locator = VykrojkiLocators.size_option_modal(size_option)
        else:
            size_option_locator = VykrojkiLocators.size_option(size_option)
    else:
        size_option_locator = size_option

    # --------------------------
    # 1. Выбор роста
    # --------------------------
    WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable(height_dropdown)
    ).click()

    WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable(height_option_locator)
    ).click()

    WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located(height_selected)
    )

    # Небольшая задержка для перерисовки размеров
    WebDriverWait(driver, SHORT_TIMEOUT).until(
        lambda d: d.find_element(*size_dropdown).is_enabled()
    )

    # --------------------------
    # 2. Выбор размера
    # --------------------------
    time.sleep(3)
    WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable(size_dropdown)
    ).click()

    # Ждём, пока список размеров откроется (появляется в DOM)
    WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable(size_option_locator)
    ).click()

    WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located(size_selected)
    )


def confirm_checkout_conditions(driver, timeout=DEFAULT_TIMEOUT):
    
    WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable(CheckoutLocators.RULES_CHECKBOX)
    ).click()
    
    WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable(CheckoutLocators.SUBSCRIPTION_CHECKBOX)
    ).click()


def go_to_payment(driver, timeout=DEFAULT_TIMEOUT):
    
    button = WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable(CheckoutLocators.GO_TO_PAYMENT_BUTTON)
    )
    
    driver.execute_script(
        "arguments[0].scrollIntoView({block: 'center', inline: 'center'});",
        button
    )
    
    button.click()


def wait_for_payment_iframe(driver, timeout=20):
    
    iframe = WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((By.TAG_NAME, "iframe"))
    )
    
    driver.switch_to.frame(iframe)
    
    WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located(VykrojkiLocators.PAYMENT_PAGE_HEADER)
    )
    
    return iframe

