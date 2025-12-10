import pytest
import allure

from pages.product_catalog_page import ProductCatalogPage
from pages.product_detail_page import ProductDetailPage
from pages.checkout_page import CheckoutPage
from utils.product_config import ProductConfig


class TestBuyProductInOneClick:

    @pytest.mark.skip(reason="Тест пока не нужен, покупка товара в один клик откючена")
    @allure.title("Покупка товара в один клик")
    def test_buy_product_in_one_click(self, driver_logged):
        driver = driver_logged

        catalog = ProductCatalogPage(driver)
        product = ProductDetailPage(driver)
        checkout = CheckoutPage(driver)

        with allure.step("Открываем каталог выкроек и карточку товара"):
            catalog.open_patterns_catalog()
            catalog.wait_url_contains("/vykrojki/vse-vykrojki/")
            product.open_product_from_card()

        with allure.step("Выбираем параметры товара"):
            product.choose_params(ProductConfig.HEIGHT, ProductConfig.SIZE)

        with allure.step("Открываем форму покупки в один клик"):
            product.open_buy_one_click()

        with allure.step("Подтверждаем условия заказа"):
            checkout.confirm_conditions_step()

        with allure.step("Переходим к оплате"):
            checkout.go_to_payment_step()
            checkout.wait_payment_iframe()


         

