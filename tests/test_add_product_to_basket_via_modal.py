import pytest
import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.basket_locators import BasketLocators
from utils.test_helpers import navigate_to_patterns, select_product_params, DEFAULT_TIMEOUT
from utils.product_config import ProductConfig
import time


class TestAddToCartViaModal:
    

    @pytest.mark.smoke
    @allure.title("Добавление товара в корзину через модальное окно")
    @allure.description("Проверка добавления товара в корзину через модальное окно")
    def test_add_product_to_cart_via_modal(self, driver_logged):
        driver = driver_logged

        # 1. Переход в “Выкройки”
        navigate_to_patterns(driver)

        # 2. Ждём появления карточки
        card = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located(ProductConfig.CARD)
        )

        # 3. Скроллим к карточке
        driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", card
        )

        # 4. Наводим курсор
        time.sleep(2)
        ActionChains(driver).move_to_element(card).pause(0.5).perform()

        # 5. Дублируем hover через JS
        driver.execute_script("""
            arguments[0].dispatchEvent(new MouseEvent('mouseover', {bubbles: true}));
            arguments[0].dispatchEvent(new MouseEvent('mouseenter', {bubbles: true}));
        """, card)

        # 6. Кликаем по кнопке "В корзину"
        basket_button = WebDriverWait(driver, DEFAULT_TIMEOUT).until(
            EC.element_to_be_clickable(ProductConfig.BASKET)
        )

        basket_button.click()

        # 7. Выбор параметров в модалке
        select_product_params(
            driver,
            "178-184",
            "34",
            use_modal=True
        )

        # 8. Клик “Добавить в корзину” в модалке
        WebDriverWait(driver, DEFAULT_TIMEOUT).until(
            EC.element_to_be_clickable(BasketLocators.BASKET_BUTTON_MODAL_FIRST)
        ).click()

        WebDriverWait(driver, DEFAULT_TIMEOUT).until(
            EC.element_to_be_clickable(BasketLocators.BASKET_BUTTON_MODAL_SECOND)
        ).click()



    @pytest.mark.smoke
    @allure.title("Удаление товара из корзины")
    @allure.description("Проверка удаления товара из корзины")
    def test_delete_product_from_basket(self, driver_logged):
        driver = driver_logged

        # 1. Переход в корзину из шапки
        WebDriverWait(driver, DEFAULT_TIMEOUT).until(
            EC.element_to_be_clickable(BasketLocators.HEADER_BASKET_BUTTON)
        ).click()

        # 2. Проверяем, что страница корзины открылась
        WebDriverWait(driver, DEFAULT_TIMEOUT).until(
            EC.visibility_of_element_located(BasketLocators.CART_PAGE_TITLE)
        )

        # 3. Проверяем, что есть хотя бы один товар
        products = driver.find_elements(*BasketLocators.DELETE_PRODUCT_BUTTON)
        assert len(products) > 0, "❌ В корзине нет товаров — удалять нечего"

        # 4. Удаляем первый товар
        products[0].click()

        # 5. Ждём исчезновения кнопки (этого конкретного товара)
        WebDriverWait(driver, DEFAULT_TIMEOUT).until_not(
            EC.presence_of_element_located(BasketLocators.DELETE_PRODUCT_BUTTON)
        )
            


       