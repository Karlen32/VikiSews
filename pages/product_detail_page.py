import allure
from pages.base_page import BasePage
from locators.basket_locators import BasketLocators
from utils.product_config import ProductConfig
from utils.test_helpers import select_product_params
from locators.vykrojki_locators import VykrojkiLocators


class ProductDetailPage(BasePage):

    @allure.step("Открываем товар по клику на карточку")
    def open_product_from_card(self):
        self.click(ProductConfig.CARD)

    @allure.step("Выбираем параметры товара: рост {1}, размер {2}")
    def choose_params(self, height, size):
        select_product_params(self.driver, height, size)

    @allure.step("Добавляем товар в корзину на странице товара")
    def add_to_cart(self):
        self.click(ProductConfig.BASKET_DETAIL)

    @allure.step("Переходим в корзину через модалку")
    def go_to_cart_from_modal(self):
        self.click(BasketLocators.BASKET_BUTTON_MODAL_SECOND)

    @allure.step("Покупка в 1 клик — открываем форму")
    def open_buy_one_click(self):
        self.click(VykrojkiLocators.BUY_ONE_CLICK_BUTTON)