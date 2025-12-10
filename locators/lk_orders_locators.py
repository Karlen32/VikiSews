from selenium.webdriver.common.by import By


class LKOrdersLocators:
    """Локаторы раздела 'Мои заказы'"""

    # =====================================================
    # 🔹 ОСНОВНОЙ ПУНКТ МЕНЮ ЛК
    # =====================================================
    # Пункт меню «Мои заказы» в боковой панели/меню ЛК
    TAB_ORDERS = (
        By.XPATH,
        "//a[@href='/personal/orders/']//span[contains(text(), 'Мои заказы')]"
    )

    # =====================================================
    # 🔹 ВКЛАДКИ НА СТРАНИЦЕ ЗАКАЗОВ
    # =====================================================
    ORDERS_TAB_ALL = (By.ID, "js-my-orders-tabs1")         # Все заказы
    ORDERS_TAB_COMPLETED = (By.ID, "js-my-orders-tabs2")   # Завершённые
    ORDERS_TAB_UNPAID = (By.ID, "js-my-orders-tabs3")      # Неоплаченные
    ORDERS_TAB_CANCELED = (By.ID, "js-my-orders-tabs4")    # Отменённые

    # =====================================================
    # 🔹 СПИСОК ЗАКАЗОВ
    # =====================================================
    # Карточка одного заказа
    ORDER_CARD = (
        By.CSS_SELECTOR,
        "div.orders-item.accordion__item.js-accordion-item"
    )

    # Кнопка открытия/закрытия заказа
    ORDER_ACCORDION_BUTTON = (
        By.CSS_SELECTOR,
        ".accordion__icon.accordion__icon--lg"
    )
    ACTIVE_TAB = (By.CSS_SELECTOR, ".tabs__panel--active")
    # Тело раскрытого заказа
    ORDER_BODY = (
        By.CSS_SELECTOR,
        ".orders-item__body"
    )

    ORDER_ITEM = (By.CSS_SELECTOR, "div.orders-item")

    # =====================================================
    # 🔹 ОСНОВНАЯ ИНФОРМАЦИЯ ВНУТРИ ЗАКАЗА
    # =====================================================
    ORDER_PURCHASE_DATE = (
        By.XPATH,
        ".//span[contains(text(),'Дата покупки')]/following-sibling::span"
    )

    ORDER_CUSTOMER_NAME = (
        By.XPATH,
        ".//span[contains(text(),'Имя')]/following-sibling::span"
    )

    ORDER_CUSTOMER_EMAIL = (
        By.XPATH,
        ".//span[contains(text(),'E–mail')]/following-sibling::span"
    )

    ORDER_PAYMENT_METHOD = (
        By.XPATH,
        ".//span[contains(text(),'Способы оплаты')]/following-sibling::span"
    )

    ORDER_BONUSES_USED = (
        By.XPATH,
        ".//span[contains(text(),'Использовано бонусов')]/following-sibling::span"
    )

    ORDER_TOTAL_PRICE = (
        By.XPATH,
        ".//span[contains(text(),'Всего к оплате')]/following-sibling::span"
    )

    # =====================================================
    # 🔹 ДЕЙСТВИЯ С ЗАКАЗОМ
    # =====================================================
    # Кнопка «Оплатить заказ»
    PAY_ORDER_BUTTON = (
        By.XPATH,
        "//a[contains(@class,'orders-item__btn') and contains(., 'Оплатить заказ')]"
    )

    # Кнопка «Изменить размер» в раскрытом заказе
    CHANGE_SIZE_BUTTON = (
        By.XPATH,
        "//button[contains(@class,'js-reload-size-product')]"
    )

    # Кнопка «Изменить» в модальном окне изменения товара
    CHANGE_BUTTON = (
        By.XPATH,
        "//div[contains(@class,'add-to-cart-modal__top-row')]//button[contains(., 'Изменить')]"
    )

    # =====================================================
    # 🔹 ТОВАРЫ ВНУТРИ ЗАКАЗА
    # =====================================================
    ORDER_PRODUCT_CARD = (
        By.CSS_SELECTOR,
        ".add-to-cart-card.favorite-card--order"
    )

    PRODUCT_TITLE = (
        By.CSS_SELECTOR,
        ".add-to-cart-card__text-part-top-row p"
    )

    PRODUCT_SIZE = (
        By.XPATH,
        ".//p[contains(text(),'Размер')]"
    )

    PRODUCT_HEIGHT = (
        By.XPATH,
        ".//p[contains(text(),'Ростовка')]"
    )

    PRODUCT_QUANTITY = (
        By.XPATH,
        ".//p[contains(text(),'кол-во')]"
    )

    PRODUCT_PRICE = (
        By.CSS_SELECTOR,
        ".block-descrs__prices span"
    )

    PRODUCT_IMAGE = (
        By.CSS_SELECTOR,
        ".add-to-cart-card__img-wrap img"
    )

    # =====================================================
    # 🔹 ССЫЛКИ НА СКАЧИВАНИЕ / ПЕРЕХОД К ВЫКРОЙКЕ
    # =====================================================
    GO_TO_PATTERN_BUTTON = (
        By.CSS_SELECTOR,
        "button.js-select-input"
    )

    ORDER_GO_TO_PATTERN_MOBILE = (
        By.CSS_SELECTOR,
        "button[data-select-download-modal]"
    )
    

    