import pytest
import allure
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.base_locators import BaseLocators
from locators.favorits_locators import FavoritesLocators
from utils.test_helpers import DEFAULT_TIMEOUT
from utils.product_config import ProductConfig


class TestAddToFavoritesFromProductModal:

    @pytest.mark.smoke
    @allure.title("Добавление товара в избранное с карточки")
    @allure.description("Ховер на карточку, клик по избранному, проверка состояния")
    def test_add_to_favorites_from_product_modal(self, driver_logged):
        driver = driver_logged

        # ---------- 1. Переход в раздел ----------
        WebDriverWait(driver, DEFAULT_TIMEOUT).until(
            EC.element_to_be_clickable(BaseLocators.PATTERNS_SUBMENU_LINK)
        ).click()

        WebDriverWait(driver, DEFAULT_TIMEOUT).until(
            EC.element_to_be_clickable(BaseLocators.ALL_PATTERNS_LINK)
        ).click()

        WebDriverWait(driver, DEFAULT_TIMEOUT).until(
            EC.url_contains("/vykrojki/vse-vykrojki/")
        )

        # ---------- 2. Ждём карточку ----------
        card = WebDriverWait(driver, DEFAULT_TIMEOUT).until(
            EC.presence_of_element_located(ProductConfig.CARD)
        )

        # Скроллим к карточке
        driver.execute_script("arguments[0].scrollIntoView({block:'center'});", card)

        # ---------- 3. Ховер ----------
        time.sleep(2)
        ActionChains(driver).move_to_element(card).pause(0.4).perform()

        driver.execute_script("""
            arguments[0].dispatchEvent(new MouseEvent('mouseover', {bubbles:true}));
            arguments[0].dispatchEvent(new MouseEvent('mouseenter', {bubbles:true}));
        """, card)

        # ---------- 4. Кнопка избранного ----------
        favorite_button = WebDriverWait(driver, DEFAULT_TIMEOUT).until(
            EC.element_to_be_clickable(ProductConfig.FAVORITE)
        )

        # Кликаем
        favorite_button.click()

        msg = WebDriverWait(driver, DEFAULT_TIMEOUT).until(
            EC.visibility_of_element_located(FavoritesLocators.FAVORITE_ADDED_MESSAGE)
        )
        assert "Товар добавлен в избранное" in msg.text

    # ======================================================================
    #                       УДАЛЕНИЕ ИЗ ИЗБРАННОГО
    # ======================================================================
    @pytest.mark.smoke
    @allure.title("Удаление товара из избранного через шапку")
    @allure.description("Переход по иконке, удаление первого товара")
    def test_delete_favorites_from_header(self, driver_logged):
        driver = driver_logged

        # ---------- 1. Открываем избранное ----------
        WebDriverWait(driver, DEFAULT_TIMEOUT).until(
            EC.element_to_be_clickable(FavoritesLocators.HEADER_FAVORITES_BUTTON)
        ).click()

        # ---------- 2. Проверяем, что страница открылась ----------
        WebDriverWait(driver, DEFAULT_TIMEOUT).until(
            EC.visibility_of_element_located(FavoritesLocators.FAVORITES_PAGE_TITLE)
        )

        # ---------- 3. Удаляем первый товар ----------
        delete_btn = WebDriverWait(driver, DEFAULT_TIMEOUT).until(
            EC.element_to_be_clickable(FavoritesLocators.FAVORITE_REMOVE_BUTTON)
        )
        delete_btn.click()

        # ---------- 4. Ждём исчезновения ----------
        WebDriverWait(driver, DEFAULT_TIMEOUT).until_not(
            EC.presence_of_element_located(FavoritesLocators.FAVORITE_REMOVE_BUTTON)
        )


