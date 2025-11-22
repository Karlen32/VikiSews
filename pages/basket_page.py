import allure
from pages.base_page import BasePage
from locators.basket_locators import BasketLocators


class BasketPage(BasePage):

    @allure.step("Переходим в корзину из шапки")
    def open_cart(self):
        self.click(BasketLocators.HEADER_BASKET_BUTTON)
        self.wait_visible(BasketLocators.CART_PAGE_TITLE)

    @allure.step("Удаляем первый товар из корзины")
    def delete_first_product(self):
        products = self.driver.find_elements(*BasketLocators.DELETE_PRODUCT_BUTTON)
        assert len(products) > 0, "В корзине нет товаров — удалять нечего"

        products[0].click()

        self.wait.until_not(
            lambda d: d.find_elements(*BasketLocators.DELETE_PRODUCT_BUTTON)
        )

    @allure.step("Подтверждаем товар в модалке")
    def click_modal_add_buttons(self):
        self.wait_clickable(BasketLocators.BASKET_BUTTON_MODAL_FIRST).click()
        self.wait_clickable(BasketLocators.BASKET_BUTTON_MODAL_SECOND).click()
