from selenium.webdriver.common.by import By

class BasketLocators:
    """
    Локаторы для корзины:
    - Кнопки перехода в корзину
    - Элементы страницы корзины
    - Управление товарами в корзине
    """

    # Кнопка "В корзину" в шапке
    HEADER_BASKET_BUTTON = (
        By.CSS_SELECTOR,
        "a.header__icon-button[href='/personal/basket/']"
    )

    # 🔹 Кнопка “в корзину” во втором модальном окне (ссылка <a>)
    BASKET_BUTTON_MODAL_SECOND = (
        By.XPATH,
        "//a[contains(normalize-space(text()), 'в корзину')]"
    )

    # 🔹 Ссылка на карточку выкройки “ОсАнна”
    OSANNA_PATTERN_LINK_CARD = (
        By.CSS_SELECTOR,
        "a[href='/vykrojki/platja-i-sarafany/osanna-plate/']"
    )

    # 🔹 Заголовок страницы корзины <h1>КОРЗИНА</h1>
    CART_PAGE_TITLE = (
        By.XPATH,
        "//h1[contains(@class, 'h1--bold') and normalize-space(text())='КОРЗИНА']"
    )

    # 🔹 Кнопка “К оформлению” на странице корзины
    CHECKOUT_BUTTON = (
        By.XPATH,
        "//a[contains(@class, 'js-service-button-second') "
        "and contains(translate(normalize-space(text()), 'К ОФОРМЛЕНИЮ', 'к оформлению'), 'к оформлению')]"
    )

    # 🔹 Кнопка “В корзину” в первом модальном окне (button)
    BASKET_BUTTON_MODAL_FIRST = (
        By.XPATH,
        "//button[contains(translate(normalize-space(.), 'ВКОРЗИНУ', 'вкорзину'), 'в корзину')]"
    )

    # 🔹 Кнопка удаления товара (крестик) в корзине
    DELETE_PRODUCT_BUTTON = (
        By.XPATH,
        "//button[contains(@class,'js-remove-product')]"
    )

    # 🔹 Кнопка удаления конкретного товара по product_id
    DELETE_PRODUCT_BUTTON_BY_ID = (
        By.XPATH,
        "//button[@data-product='{product_id}']"
    )
