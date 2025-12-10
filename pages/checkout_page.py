import allure
from pages.base_page import BasePage
from locators.basket_locators import BasketLocators
from locators.vykrojki_locators import VykrojkiLocators
from utils.test_helpers import (
    confirm_checkout_conditions,
    go_to_payment,
    wait_for_payment_iframe
)


class CheckoutPage(BasePage):

    @allure.step("Переходим к оформлению заказа из popup")
    def go_to_checkout_from_popup(self):
        self.click(BasketLocators.CHECKOUT_MODAL_BUTTON)

    @allure.step("Подтверждаем чекбоксы условий покупки")
    def confirm_conditions(self):
        confirm_checkout_conditions(self.driver)

    @allure.step("Переходим на страницу оплаты")
    def go_to_payment_step(self):
        go_to_payment(self.driver)

    @allure.step("Ожидаем загрузку iframe оплаты")
    def wait_payment_iframe(self):
        return wait_for_payment_iframe(self.driver)


    
    @allure.step("Подтверждаем условия оформления заказа")
    def confirm_checkout_conditions(self):
        from utils.test_helpers import confirm_checkout_conditions
        confirm_checkout_conditions(self.driver)

    @allure.step("Переходим к оплате")
    def go_to_payment(self):
        from utils.test_helpers import go_to_payment
        go_to_payment(self.driver)

    @allure.step("Ожидаем успешную оплату")
    def wait_success(self):
        self.wait_visible(VykrojkiLocators.THANK_YOU_TITLE)

    

