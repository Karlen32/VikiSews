import pytest
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.product_config import ProductConfig
from locators.basket_locators import BasketLocators
from utils.test_helpers import (
    confirm_checkout_conditions,
    go_to_payment,
    wait_for_payment_iframe,
    DEFAULT_TIMEOUT
)


class TestBuyProductViaPopup:
    """Тест: покупка товара 'Джуанна платье' через popup"""

    @pytest.mark.smoke
    @allure.title("Покупка товара через всплывающее окно")
    @allure.description("Полный сценарий: добавление, переход к оформлению, подтверждение условий, оплата")
    def test_buy_product_via_popup(self, select_product):

        # ---------- 1. Выбор товара ----------
        driver = select_product(
            ProductConfig.NAME,
            ProductConfig.HEIGHT,
            ProductConfig.SIZE
        )

        # ---------- 2. Добавление в корзину ----------
        WebDriverWait(driver, DEFAULT_TIMEOUT).until(
            EC.element_to_be_clickable(ProductConfig.BASKET_DETAIL)
        ).click()

        # ---------- 3. Переход к оформлению из popup ----------
        WebDriverWait(driver, DEFAULT_TIMEOUT).until(
            EC.element_to_be_clickable(BasketLocators.CHECKOUT_BUTTON)
        ).click()

        # ---------- 4. Подтверждение чекбоксов ----------
        confirm_checkout_conditions(driver)

        # ---------- 5. Переход на оплату ----------
        go_to_payment(driver)

        # ---------- 6. Проверка iframe оплаты ----------
        wait_for_payment_iframe(driver)


    
