import pytest
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Импорты локаторов
from locators.vykrojki_locators import VykrojkiLocators
from locators.basket_locators import BasketLocators
from locators.checkout_locators import CheckoutLocators
from locators.bonuses_locators import BonusesLocators
from utils.test_helpers import confirm_checkout_conditions, go_to_payment, DEFAULT_TIMEOUT, LONG_TIMEOUT


class TestPaymentWithBonuses:
    """Тест: оплата из корзины бонусами"""

    @pytest.mark.smoke
    @allure.title("Оплата заказа бонусами из корзины")
    @allure.description("Проверка оплаты заказа бонусами: добавление товара, применение бонусов, оформление и оплата")
    def test_pay_from_cart_with_bonuses(self, select_product):
        driver = select_product

        # ---------- 🛒 Добавляем товар ----------
        WebDriverWait(driver, DEFAULT_TIMEOUT).until(
            EC.element_to_be_clickable(VykrojkiLocators.ADD_TO_BASKET_BUTTON)
        ).click()

        # ---------- 🧺 Переход в корзину ----------
        WebDriverWait(driver, DEFAULT_TIMEOUT).until(
            EC.element_to_be_clickable(BasketLocators.BASKET_BUTTON_MODAL_SECOND)
        ).click()

        # ---------- 💰 Применяем бонусы ----------
        WebDriverWait(driver, DEFAULT_TIMEOUT).until(
            EC.element_to_be_clickable(BonusesLocators.BONUS_CHECKBOX)
        ).click()

        WebDriverWait(driver, DEFAULT_TIMEOUT).until(
            EC.visibility_of_element_located(BonusesLocators.BONUS_INPUT)
        ).send_keys("220")

        WebDriverWait(driver, DEFAULT_TIMEOUT).until(
            EC.element_to_be_clickable(BonusesLocators.BONUS_APPLY_BUTTON)
        ).click()

        # ---------- 🧾 Переходим к оформлению ----------
        WebDriverWait(driver, DEFAULT_TIMEOUT).until(
            EC.element_to_be_clickable(BasketLocators.CHECKOUT_BUTTON)
        ).click()

        # ---------- ☑️ Подтверждение условий ----------
        confirm_checkout_conditions(driver)

        # ---------- 🚀 Переход к оплате ----------
        go_to_payment(driver)

        # ---------- ✅ Проверка успешной оплаты ----------
        WebDriverWait(driver, LONG_TIMEOUT).until(
            EC.visibility_of_element_located(CheckoutLocators.SUCCESS_TITLE)
        )

        print("✅ Покупка с оплатой бонусами прошла успешно!")
