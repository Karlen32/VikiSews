import pytest
import allure
from pages.product_catalog_page import ProductCatalogPage
from pages.product_detail_page import ProductDetailPage
from pages.basket_page import BasketPage
from utils.product_config import ProductConfig


class TestAddToBasket:

    @pytest.mark.smoke
    @allure.title("Добавление товара 'Сувира манишка' в корзину")
    @allure.description("Проверка добавления товара в корзину: выбор параметров, добавление, переход в корзину, удаление")
    def test_add_product_to_basket(self, driver_logged):

        catalog = ProductCatalogPage(driver_logged)
        detail = ProductDetailPage(driver_logged)
        basket = BasketPage(driver_logged)

        with allure.step("Переходим в каталог выкроек"):
            catalog.open_patterns_catalog()

        with allure.step("Открываем товар 'Сувира манишка'"):
            detail.open_product_from_card()

        with allure.step("Выбираем параметры товара"):
            detail.choose_params(ProductConfig.HEIGHT, ProductConfig.SIZE)

        with allure.step("Добавляем товар в корзину"):
            detail.add_to_cart()

        with allure.step("Переходим в корзину через модалку"):
            detail.go_to_cart_from_modal()

        with allure.step("Удаляем товар из корзины"):
            basket.delete_first_product()

        
   