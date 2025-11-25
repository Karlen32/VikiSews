import pytest
import allure
import time
from pages.product_detail_page import ProductDetailPage
from pages.basket_page import BasketPage
from pages.bonuses_page import BonusesPage
from pages.checkout_page import CheckoutPage
from utils.product_config import ProductConfig


class TestPaymentWithBonuses:

    @pytest.mark.smoke
    @allure.title("Оплата заказа бонусами из корзины")
    @allure.description("Проверка оплаты заказа бонусами: добавление товара, применение бонусов, оформление и оплата")
    def test_pay_from_cart_with_bonuses(self, select_product):

        driver = select_product(
            ProductConfig.NAME,
            ProductConfig.HEIGHT1,
            ProductConfig.SIZE1
        )

        detail = ProductDetailPage(driver)
        basket = BasketPage(driver)
        bonuses = BonusesPage(driver)
        checkout = CheckoutPage(driver)

        with allure.step("Добавляем товар в корзину"):
            detail.add_to_cart()

        with allure.step("Переходим в корзину"):
            basket.open_from_modal()

        with allure.step("Применяем бонусы"):
            bonuses.apply_bonuses("220")

        with allure.step("Переходим к оформлению"):
            basket.open_checkout()

        with allure.step("Подтверждаем условия"):
            checkout.confirm_conditions()

        # ---- Здесь добавляем скролл ----
        checkout.driver.execute_script("window.scrollBy(0, 300);")
        time.sleep(0.2)

        with allure.step("Переходим к оплате"):
            checkout.go_to_payment()

        with allure.step("Проверяем успешную оплату"):
            checkout.wait_success()

