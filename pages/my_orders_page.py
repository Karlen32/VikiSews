from pages.base_page import BasePage
from locators.lk_locators import LKLocators
from locators.lk_orders_locators import LKOrdersLocators
import allure
import time


class MyOrdersPage(BasePage):

    # -----------------------------
    # Открытие раздела
    # -----------------------------
    @allure.step("Открываем раздел 'Мои заказы' в ЛК")
    def open_my_orders(self):
        self.hover(LKLocators.LK_ICON_BUTTON)  # обязательно!
        self.click(LKLocators.MENU_ORDERS)
        self.wait_visible(LKOrdersLocators.ORDERS_TAB_ALL)

    # -----------------------------
    # Вкладки
    # -----------------------------
    @allure.step("Переключаемся на вкладку 'Все'")
    def switch_to_all_orders(self):
        self.click(LKOrdersLocators.ORDERS_TAB_ALL)

    @allure.step("Переключаемся на вкладку 'Неоплаченные'")
    def switch_to_unpaid_orders(self):
        self.click(LKOrdersLocators.ORDERS_TAB_UNPAID)

    @allure.step("Переключаемся на вкладку 'Завершённые'")
    def switch_to_completed_orders(self):
        self.click(LKOrdersLocators.ORDERS_TAB_COMPLETED)

    @allure.step("Переключаемся на вкладку 'Отменённые'")
    def switch_to_canceled_orders(self):
        self.click(LKOrdersLocators.ORDERS_TAB_CANCELED)

    # -----------------------------
    # Получение списка заказов
    # -----------------------------
    @allure.step("Получаем список заказов")
    def get_orders(self):
        active_tab = self.wait_visible(LKOrdersLocators.ACTIVE_TAB)
        return active_tab.find_elements(*LKOrdersLocators.ORDER_CARD)


    @allure.step("Получаем заказ по индексу {index}")
    def get_order(self, index):
        orders = self.get_orders()
        if len(orders) <= index:
            raise AssertionError(f"Нет заказа с индексом {index}, найдено: {len(orders)}")
        return orders[index]

    # -----------------------------
    # Раскрытие заказа
    # -----------------------------
    @allure.step("Раскрываем заказ по индексу {index}")
    def expand_order(self, index):
        orders = self.get_orders()
        order = orders[index]

        accordion = order.find_element(*LKOrdersLocators.ORDER_ACCORDION_BUTTON)

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            accordion
        )

        accordion.click()
        return order

    # -----------------------------
    # Действия внутри заказа
    # -----------------------------
    @allure.step("Кликаем кнопку 'Изменить размер' в заказе")
    def click_change_size(self, order):
        # Найдём кнопку
        btns = order.find_elements(*LKOrdersLocators.CHANGE_SIZE_BUTTON)
        if not btns:
            raise AssertionError("Кнопка 'Изменить размер' отсутствует в заказе")
        btn = btns[0]
        self.wait.until(lambda d: btn.is_displayed())
        self.driver.execute_script(
            "window.scrollTo({top: arguments[0].getBoundingClientRect().top + window.scrollY - 200, behavior: 'smooth'});",
            btn
        )
        # Дадаём небольшую паузу, пока анимация скролла завершится
        self.wait.until(lambda d: btn.is_displayed())
        # Пробуем обычный клик
        try:
            btn.click()
        except:
            # Если перекрыто — делаем JS-клик
            self.driver.execute_script("arguments[0].click();", btn)

    @allure.step("Кликаем кнопку 'Изменить'")
    def click_change(self):
        btn = self.wait_visible(LKOrdersLocators.CHANGE_BUTTON)

        # Скролл именно к нулевой позиции Y внутри модалки
        self.driver.execute_script("""
            arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});
        """, btn)

        # Дать закончиться анимации (всегда есть transition 300-600ms)
        self.wait.until(lambda d: btn.is_enabled())

        # Жёсткий JS-клик, который игнорирует перекрытия
        self.driver.execute_script("arguments[0].click();", btn)

    # -----------------------------
    # Товары в заказе
    # -----------------------------
    @allure.step("Получаем товары внутри заказа")
    def get_order_products(self, order):
        return order.find_elements(*LKOrdersLocators.ORDER_PRODUCT_CARD)


    @allure.step("Нажимаем кнопку 'Оплатить заказ'")
    def click_pay_order(self, order):
        btn = order.find_element(*LKOrdersLocators.PAY_ORDER_BUTTON)

        self.driver.execute_script(
            "arguments[0].scrollIntoView({behavior: 'instant', block: 'center'});",
            btn
        )
        time.sleep(0.3)
        try:
            btn.click()
        except:
            self.driver.execute_script("arguments[0].click();", btn)

        self.switch_to_new_window()


    @allure.step("Кликаем на кнопку 'Перейти к выкройке'")
    def click_go_to_vykrojki(self, order):
        btn = order.find_element(*LKOrdersLocators.GO_TO_PATTERN_BUTTON)
        btn.click()


    
        
    