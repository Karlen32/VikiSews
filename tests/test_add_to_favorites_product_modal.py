import pytest
import allure
from pages.product_catalog_page import ProductCatalogPage
from pages.favorites_page import FavoritesPage
import time

class TestAddToFavoritesFromProductModal:


    @pytest.mark.smoke
    @allure.title("Добавление товара в избранное с карточки")
    @allure.description("Ховер на карточку, клик по избранному, проверка состояния")
    def test_add_to_favorites_from_product_modal(self, driver_logged):

        page = ProductCatalogPage(driver_logged)

        with allure.step("Переходим в каталог"):
            page.open_patterns_catalog()

        with allure.step("Находим и ховерим карточку"):
            card = page.get_first_card()
            time.sleep(1)
            page.hover_card(card)

        with allure.step("Добавляем товар в избранное"):
            page.click_favorite()

        with allure.step("Проверяем всплывающее сообщение"):
            msg = page.wait_favorite_added_message()
            assert "Товар добавлен в избранное" in msg.text


    @allure.title("Удаление товара из избранного через шапку")
    @allure.description("Переход по иконке, удаление первого товара")
    def test_delete_favorites_from_header(self, driver_logged):

        page = FavoritesPage(driver_logged)

        with allure.step("Открываем избранное"):
            page.open_favorites()

        with allure.step("Удаляем первый товар"):
            page.delete_first_favorite()


