from selenium.webdriver.common.by import By


class LKOrdersLocators:
    """Локаторы заказов"""

    """ Вкладка "Мои заказы" """
    TAB_ORDERS = (
        By.XPATH,
        "//a[@href='/personal/orders/']//span[contains(text(), 'Мои заказы')]"
    )

    # Таб: Все заказы
    ORDERS_TAB_ALL = (By.ID,"js-my-orders-tabs1")

    # Таб: Завершённые
    ORDERS_TAB_COMPLETED = (By.ID,"js-my-orders-tabs2")

    # Таб: Неоплаченные
    ORDERS_TAB_UNPAID = (By.ID,"js-my-orders-tabs3")

    # Таб: Отменённые
    ORDERS_TAB_CANCELED = (By.ID,"js-my-orders-tabs4")

    # Все кнопки раскрытия заказа в списке по ID
    ORDER_ACCORDION_BUTTONS = (
        By.CSS_SELECTOR,
        "button.orders-item__header-btn.js-accordion-button")

    # Кнопка "Повторить заказ"
    REPEAT_ORDER_BUTTON = (
            By.XPATH,
            "//a[contains(@class,'orders-item__btn') and contains(normalize-space(text()), 'Повторить заказ')]"
    )

    # Кнопка "Оплатить заказ"
    PAY_ORDER_BUTTON = (
        By.XPATH,
        "//a[contains(@class,'orders-item__btn') and contains(normalize-space(text()), 'Оплатить заказ')]"
    )

    # Кнопка "Изменить размер"
    CHANGE_SIZE_BUTTON = (
        By.XPATH,
        "//button[contains(@class,'js-reload-size-product')]"
        "[.//span[contains(normalize-space(text()), 'изменить размер')]]"
    )