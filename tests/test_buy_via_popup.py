import pytest
import allure
import time
from pages.product_detail_page import ProductDetailPage
from pages.checkout_page import CheckoutPage
from utils.product_config import ProductConfig


class TestBuyProductViaPopup:

    @pytest.mark.smoke
    @allure.title("Покупка товара через всплывающее окно")
    @allure.description("Полный сценарий: добавление, переход к оформлению, подтверждение условий, оплата")
    def test_buy_product_via_popup(self, select_product):

        # Фикстура возвращает driver уже на странице товара
        driver = select_product(
            ProductConfig.NAME,
            ProductConfig.HEIGHT,
            ProductConfig.SIZE
        )

        detail = ProductDetailPage(driver)
        checkout = CheckoutPage(driver)

        with allure.step("Добавляем товар в корзину"):
            detail.add_to_cart()

        with allure.step("Переходим к оформлению заказа через popup"):
            checkout.go_to_checkout_from_popup()

        with allure.step("Подтверждаем обязательные чекбоксы"):
            checkout.confirm_conditions()
            time.sleep(2)
        with allure.step("Переходим на оплату"):
            checkout.go_to_payment_step()

        with allure.step("Проверяем загрузку iframe оплаты"):
            checkout.wait_payment_iframe()



    
