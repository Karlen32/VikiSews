from pages.my_orders_page import MyOrdersPage
from pages.lk_page import LKPage
from pages.product_detail_page import ProductDetailPage
from utils.product_config import ProductConfig
import allure
import time


class TestChangeOrderSize:

    @allure.feature("Мои заказы")
    @allure.story("Изменение размера заказа")
    def test_change_order_size(self, driver_logged):
        page = MyOrdersPage(driver_logged)
        lk = LKPage(driver_logged)
        detail = ProductDetailPage(driver_logged)

        lk.open_menu()
        page.open_my_orders()

        order = page.expand_order(0)

        page.click_change_size(order)

        detail.choose_params(ProductConfig.HEIGHT, ProductConfig.SIZE)
        time.sleep(2)

        page.click_change()