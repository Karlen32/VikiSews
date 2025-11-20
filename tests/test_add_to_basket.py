import pytest
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.product_config import ProductConfig
# Импорты всех нужных локаторов
from locators.basket_locators import BasketLocators
from utils.test_helpers import navigate_to_patterns, select_product_params, DEFAULT_TIMEOUT


class TestAddToBasket:
    """Тест: добавление товара 'Сувира манишка' в корзину"""

    @pytest.mark.smoke
    @allure.title("Добавление товара 'Сувира манишка' в корзину")
    @allure.description("Проверка добавления товара в корзину: выбор параметров, добавление, переход в корзину, удаление")
    def test_add_product_to_basket(self, driver_logged):
        driver = driver_logged

        # 1️⃣ Переход в "Выкройки"
        navigate_to_patterns(driver)

        # 2️⃣ Кликаем по карточке "Сувира манишка"
        WebDriverWait(driver, DEFAULT_TIMEOUT).until(
            EC.element_to_be_clickable(ProductConfig.CARD)
        ).click()

        # 3️⃣ Выбираем параметры товара
        select_product_params(driver, ProductConfig.HEIGHT, ProductConfig.SIZE)

        # 4️⃣ Добавляем в корзину
        WebDriverWait(driver, DEFAULT_TIMEOUT).until(
            EC.element_to_be_clickable(ProductConfig.BASKET_DETAIL)
        ).click()

        # 5️⃣ Переходим в корзину
        WebDriverWait(driver, DEFAULT_TIMEOUT).until(
            EC.element_to_be_clickable(BasketLocators.BASKET_BUTTON_MODAL_SECOND)
        ).click()

        # 6️⃣ Проверяем, что открылась страница корзины
        WebDriverWait(driver, DEFAULT_TIMEOUT).until(
            EC.visibility_of_element_located(BasketLocators.CART_PAGE_TITLE)
        )

        WebDriverWait(driver, DEFAULT_TIMEOUT).until(
            EC.element_to_be_clickable(BasketLocators.DELETE_PRODUCT_BUTTON)
        ).click()

        # 7️⃣ Проверяем, что товар удалён из корзины
        WebDriverWait(driver, DEFAULT_TIMEOUT).until_not(
            EC.presence_of_element_located(BasketLocators.DELETE_PRODUCT_BUTTON)
        )

        
   