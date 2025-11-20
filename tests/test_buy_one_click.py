import pytest
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.vykrojki_locators import VykrojkiLocators
from utils.product_config import ProductConfig
from utils.test_helpers import (
    confirm_checkout_conditions,
    go_to_payment,
    wait_for_payment_iframe,
    DEFAULT_TIMEOUT
)


class TestBuyProductInOneClick:
    """Тест: покупка товара в один клик"""

    @pytest.mark.smoke
    @allure.title("Покупка товара 'Джуанна платье' в один клик")
    @allure.description("Проверка покупки товара в один клик: выбор параметров, подтверждение условий, переход к оплате, (пока функция не доступна)")
    def test_buy_product_in_one_click(self, select_product):

        # ---------- 1. Открываем товар и выбираем параметры ----------
        driver = select_product(
            ProductConfig.NAME,
            ProductConfig.HEIGHT,
            ProductConfig.SIZE
        )

        # ---------- 2. Кликаем “Купить в один клик” ----------
        WebDriverWait(driver, DEFAULT_TIMEOUT).until(
            EC.element_to_be_clickable(VykrojkiLocators.BUY_ONE_CLICK_BUTTON)
        ).click()

        # ---------- 3. Подтверждение условий ----------
        confirm_checkout_conditions(driver)

        # ---------- 4. Переход к оплате ----------
        go_to_payment(driver)

        # ---------- 5. Проверяем, что iframe оплаты загрузился ----------
        wait_for_payment_iframe(driver)

         

