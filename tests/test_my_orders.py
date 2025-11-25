import allure
from pages.my_orders_page import MyOrdersPage
from pages.lk_page import LKPage
from locators.lk_orders_locators import LKOrdersLocators



class TestMyOrders:

    @allure.feature("Мои заказы")
    @allure.story("Вкладки")
    def test_orders_tabs(self, driver_logged):
        page = MyOrdersPage(driver_logged)
        lk = LKPage(driver_logged)

        lk.open_menu()
        page.open_my_orders()

        page.switch_to_unpaid_orders()
        page.switch_to_completed_orders()
        page.switch_to_canceled_orders()
        page.switch_to_all_orders()

    @allure.feature("Мои заказы")
    @allure.story("Список заказов")
    def test_orders_list_not_empty(self, driver_logged):
        page = MyOrdersPage(driver_logged)
        lk = LKPage(driver_logged)

        lk.open_menu()
        page.open_my_orders()

        orders = page.get_orders()
        assert len(orders) > 0

    @allure.feature("Мои заказы")
    @allure.story("Раскрытие заказа")
    def test_order_accordion_expand(self, driver_logged):
        page = MyOrdersPage(driver_logged)
        lk = LKPage(driver_logged)

        lk.open_menu()
        page.open_my_orders()

        order = page.expand_order(0)
        assert order is not None


    @allure.feature("Мои заказы")
    @allure.story("Содержимое заказа")
    def test_order_content_exists(self, driver_logged):
        page = MyOrdersPage(driver_logged)
        lk = LKPage(driver_logged)

        lk.open_menu()
        page.open_my_orders()

        order = page.expand_order(0)

        order.find_element(*LKOrdersLocators.ORDER_PURCHASE_DATE)
        order.find_element(*LKOrdersLocators.ORDER_CUSTOMER_NAME)
        order.find_element(*LKOrdersLocators.ORDER_CUSTOMER_EMAIL)
        order.find_element(*LKOrdersLocators.ORDER_PAYMENT_METHOD)
        order.find_element(*LKOrdersLocators.ORDER_TOTAL_PRICE)

    @allure.feature("Мои заказы")
    @allure.story("Товары внутри заказа")
    def test_order_products(self, driver_logged):
        page = MyOrdersPage(driver_logged)
        lk = LKPage(driver_logged)

        lk.open_menu()
        page.open_my_orders()

        order = page.expand_order(0)

        products = page.get_order_products(order)
        assert len(products) > 0

        first = products[0]
        first.find_element(*LKOrdersLocators.PRODUCT_TITLE)
        first.find_element(*LKOrdersLocators.PRODUCT_PRICE)
        first.find_element(*LKOrdersLocators.PRODUCT_IMAGE)
