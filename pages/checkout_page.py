import allure
from pages.base_page import BasePage
from locators.basket_locators import BasketLocators
from utils.test_helpers import (
    confirm_checkout_conditions,
    go_to_payment,
    wait_for_payment_iframe
)


class CheckoutPage(BasePage):

    @allure.step("Переходим к оформлению заказа из popup")
    def go_to_checkout_from_popup(self):
        self.click(BasketLocators.CHECKOUT_BUTTON)

    @allure.step("Подтверждаем чекбоксы условий покупки")
    def confirm_conditions(self):
        confirm_checkout_conditions(self.driver)

    @allure.step("Переходим на страницу оплаты")
    def go_to_payment_step(self):
        go_to_payment(self.driver)

    @allure.step("Ожидаем загрузку iframe оплаты")
    def wait_payment_iframe(self):
        return wait_for_payment_iframe(self.driver)

    

