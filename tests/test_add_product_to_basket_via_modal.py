import pytest
import allure
import time
from pages.basket_page import BasketPage
from pages.product_catalog_page import ProductCatalogPage


class TestAddProductToBasketViaModal:



    @pytest.mark.smoke
    @allure.title("Добавление товара в корзину через модальное окно")
    def test_add_product_to_basket_via_modal(self, driver_logged):

        catalog = ProductCatalogPage(driver_logged)
        basket = BasketPage(driver_logged)

        with allure.step("Открываем каталог"):
            catalog.open_patterns_catalog()

        with allure.step("Находим карточку товара и ховерим"):
            card = catalog.get_first_card()
            time.sleep(1)
            catalog.hover_card(card)

        with allure.step("Открываем модалку добавления в корзину"):
            catalog.click_add_to_cart_button()

        with allure.step("Выбираем параметры товара"):
            catalog.select_product_params("178-184", "m")

        with allure.step("Подтверждаем добавление товара в корзину"):
            basket.click_modal_add_buttons()

    @pytest.mark.smoke
    @allure.title("Удаление товара из корзины")
    def test_delete_product_from_basket(self, driver_logged):

        basket = BasketPage(driver_logged)

        with allure.step("Открываем корзину"):
            basket.open_cart()

        with allure.step("Удаляем первый товар"):
            basket.delete_first_product()

