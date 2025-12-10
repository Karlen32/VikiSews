from pages.my_orders_page import MyOrdersPage
from pages.checkout_page import CheckoutPage
import allure
import time
import pytest


class TestPaymentForAnUnpaidOrder:

    @pytest.mark.smoke
    @allure.feature("Мои заказы")
    @allure.story("Оплата неоплаченного заказа")
    def test_payment_for_an_unpaid_order(self, driver_logged):
        page = MyOrdersPage(driver_logged)
        checkout = CheckoutPage(driver_logged)

        with allure.step("Открываем раздел 'Мои заказы'"):
            page.open_my_orders()

        with allure.step("Переключаемся на вкладку 'Неоплаченные'"):
            page.switch_to_unpaid_orders()
            time.sleep(3)

        with allure.step("Раскрываем первый заказ"):
            order = page.expand_order(0)

        with allure.step("Кликаем 'Оплатить заказ'"):
            page.click_pay_order(order)

        with allure.step("Проверяем, что iframe оплаты появился"):
            assert checkout.wait_payment_iframe(), \
                "Iframe оплаты не появился"


    @allure.feature("Мои заказы")
    @allure.story("Переходим к выкройке из заказа")
    def test_go_to_vykrojki_from_order(self, driver_logged):
        page = MyOrdersPage(driver_logged)

        with allure.step("Открываем раздел 'Мои заказы'"):
            page.open_my_orders()

        with allure.step("Переключаемся на вкладку 'Завершенные'"):
            page.switch_to_completed_orders()
            time.sleep(3)

        with allure.step("Раскрываем первый заказ"):
            order = page.expand_order(0)

        with allure.step("Кликаем 'Перейти к выкройке'"):
            page.click_go_to_vykrojki(order)
