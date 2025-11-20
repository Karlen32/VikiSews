from selenium.webdriver.common.by import By

class VykrojkiLocators:
    """
    Локаторы для раздела 'Выкройки':
    - Страница всех выкроек
    - Карточка товара
    - Рост, размер, цена
    - Добавление в корзину, избранное
    """
    @staticmethod
    def pattern_card_by_name(name: str):
        """Генерирует локатор карточки товара по названию"""
        return (
            By.XPATH,
            f"//div[contains(@class, 'card-pattern')][.//span[contains(normalize-space(), '{name}')]]"
        )

    @staticmethod
    def detail_add_to_cart_button(name: str = None):
        """
        Локатор кнопки 'В корзину' на детальной странице товара.
        """
        return (
            By.CSS_SELECTOR,
            "button[id$='_add_basket_link']"
        )

    @staticmethod
    def basket_button_by_name(name: str):
        """Генерирует локатор кнопки корзины на карточке по названию товара"""
        return (
            By.XPATH,
            f"//div[contains(@class, 'card-pattern')][.//span[contains(normalize-space(), '{name}')]]//button[contains(@class, 'block-btns__cart')]"
        )

    @staticmethod
    def image_by_name(name: str):
        """Генерирует локатор изображения карточки по названию товара"""
        return (
            By.XPATH,
            f"//div[contains(@class, 'card-pattern')][.//span[contains(normalize-space(), '{name}')]]//img"
        )

    @staticmethod
    def favorite_button_by_name(name: str):
        """Генерирует локатор кнопки избранного на карточке по названию товара"""
        return (
            By.XPATH,
            f"//div[contains(@class, 'card-pattern')][.//span[contains(normalize-space(), '{name}')]]//button[contains(@class, 'block-btns__favorites')]"
        )

    @staticmethod
    def height_option(height_value: str):
        """Генерирует локатор опции роста по тексту (например, '154-160', '170-176')"""
        return (
            By.XPATH,
            f"//span[@class='select-secondary__list-text js-select-text' and normalize-space(text())='{height_value}']"
        )

    @staticmethod
    def size_option(size_value: str):
        """Генерирует локатор опции размера по тексту (например, 'XS', 'M', 'XL', '36', '42')"""
        return (
            By.XPATH,
            f"//span[@class='select-secondary__list-text js-select-text' and normalize-space(text())='{size_value.lower()}']"
        )

    @staticmethod
    def height_option_modal(height_value: str):
        """Генерирует локатор опции роста в модальном окне"""
        return (
            By.XPATH,
            f"//div[@id='add-height']//span[@class='select-secondary__list-text js-select-text' and normalize-space(text())='{height_value}']"
        )

    @staticmethod
    def size_option_modal(size_value: str):
        """Генерирует локатор опции размера в модальном окне"""
        return (
            By.XPATH,
            f"//div[@id='add-size']//span[@class='select-secondary__list-text js-select-text' and normalize-space(text())='{size_value.lower()}']"
        )
    # =========================================================
    # СТРАНИЦА "ВСЕ ВЫКРОЙКИ"
    # =========================================================
    # Ссылка на карточку выкройки
    PATTERN_CARD = (By.CSS_SELECTOR, ".card-pattern")


    # =========================================================
    # КАРТОЧКА ТОВАРА — ВЫБОР ПАРАМЕТРОВ
    # =========================================================

    # --- Поле выбора роста ---
    HEIGHT_DROPDOWN_BUTTON = (By.XPATH,
        "//span[normalize-space(text())='Ваш рост*']/ancestor::div[contains(@class,'js-select-input')]//button[contains(@class, 'select__open-button')]"
    )
    HEIGHT_OPTION_BY_TEXT = (By.XPATH,"//ul[contains(@class,'product-item-scu-item-list-height')]"
        "//span[contains(@class,'select-secondary__list-text') and normalize-space(text())='{height_value}']"
    )
    HEIGHT_OPTION_154_160 = (By.XPATH, "//span[@class='select-secondary__list-text js-select-text' and normalize-space(text())='154-160']")
    HEIGHT_OPTION_162_168 = (By.XPATH, "//span[@class='select-secondary__list-text js-select-text' and normalize-space(text())='162-168']")
    HEIGHT_OPTION_170_176 = (By.XPATH, "//span[@class='select-secondary__list-text js-select-text' and normalize-space(text())='170-176']")
    HEIGHT_OPTION_178_184 = (By.XPATH, "//span[@class='select-secondary__list-text js-select-text' and normalize-space(text())='178-184']")
    HEIGHT_SELECTED_VALUE = (By.ID, "heightSMProdParam")

    # --- Поле выбора размера (цифровые) ---
    SIZE_DROPDOWN_BUTTON = (By.XPATH,"//span[normalize-space(text())='Ваш размер(европейский)*']""/ancestor::div[contains(@class,'js-select-input')]""//button[contains(@class,'select__open-button')]")
    SIZE_OPTION_BY_TEXT = (By.XPATH,"//ul[contains(@class,'product-item-scu-item-list')]""//span[contains(@class,'select-secondary__list-text') and normalize-space(text())='{size_value}']")
    SIZE_SELECTED_VALUE = (By.XPATH,"//span[contains(@class,'js-select-value') and contains(@class,'v3')]")

    SIZE_OPTION_34 = (By.XPATH, "//span[@class='select-secondary__list-text js-select-text' and normalize-space(text())='34']")
    SIZE_OPTION_36 = (By.XPATH, "//span[@class='select-secondary__list-text js-select-text' and normalize-space(text())='36']")
    SIZE_OPTION_38 = (By.XPATH, "//span[@class='select-secondary__list-text js-select-text' and normalize-space(text())='38']")
    SIZE_OPTION_40 = (By.XPATH, "//span[@class='select-secondary__list-text js-select-text' and normalize-space(text())='40']")
    SIZE_OPTION_42 = (By.XPATH, "//span[@class='select-secondary__list-text js-select-text' and normalize-space(text())='42']")
    SIZE_OPTION_44 = (By.XPATH, "//span[@class='select-secondary__list-text js-select-text' and normalize-space(text())='44']")
    SIZE_OPTION_46 = (By.XPATH, "//span[@class='select-secondary__list-text js-select-text' and normalize-space(text())='46']")
    SIZE_OPTION_48 = (By.XPATH, "//span[@class='select-secondary__list-text js-select-text' and normalize-space(text())='48']")
    SIZE_OPTION_50 = (By.XPATH, "//span[@class='select-secondary__list-text js-select-text' and normalize-space(text())='50']")
    SIZE_OPTION_52 = (By.XPATH, "//span[@class='select-secondary__list-text js-select-text' and normalize-space(text())='52']")

    # --- Поле выбора размера (буквенные) ---
    SIZE_OPTION_XS = (By.XPATH, "//span[@class='select-secondary__list-text js-select-text' and normalize-space(text())='xs']")
    SIZE_OPTION_S = (By.XPATH, "//span[@class='select-secondary__list-text js-select-text' and normalize-space(text())='s']")
    SIZE_OPTION_M = (By.XPATH, "//span[@class='select-secondary__list-text js-select-text' and normalize-space(text())='m']")
    SIZE_OPTION_L = (By.XPATH, "//span[@class='select-secondary__list-text js-select-text' and normalize-space(text())='l']")
    SIZE_OPTION_XL = (By.XPATH, "//span[@class='select-secondary__list-text js-select-text' and normalize-space(text())='xl']")

    # --- Окно оплаты(Экваринг) ---
    PAYMENT_PAGE_HEADER = (
    By.XPATH,
    "//div[contains(@class,'card-edit__header') and normalize-space(text())='Оплатить картой']"
    )

    # --- Кнопки ---
    ADD_TO_BASKET_BUTTON = (By.XPATH,"//button[contains(normalize-space(.), 'В корзину')]")
    BUY_ONE_CLICK_BUTTON = (By.XPATH,"//button[contains(@class, 'pattern-right-part__buy-link') and contains(@class, 'js-add-basket-click')]")
    FAVORITE_ICON = (By.XPATH, "//svg[path[starts-with(@d, 'M5.05371 1.44737C2.9029')]]")

    # --- Модалка добавления в корзину ---
    HEIGHT_DROPDOWN_BUTTON_MODAL = (By.XPATH, "//div[@id='add-height']//button[contains(@class, 'select__open-button')]")
    HEIGHT_OPTION_BY_TEXT_MODAL = (By.XPATH, "//div[@id='add-height']//span[@class='select-secondary__list-text js-select-text' and normalize-space(text())='{height_value}']")
    HEIGHT_SELECTED_VALUE_MODAL = (By.XPATH, "//div[@id='add-height']//span[contains(@class, 'js-select-value')]")
    SIZE_DROPDOWN_BUTTON_MODAL = (By.XPATH, "//div[@id='add-size']//button[contains(@class, 'select__open-button')]")
    SIZE_SELECTED_VALUE_MODAL = (By.XPATH, "//div[@id='add-size']//span[contains(@class, 'js-select-value')]")
    SIZE_OPTION_BY_TEXT_MODAL = (By.XPATH, "//div[@id='add-size']//span[@class='select-secondary__list-text js-select-text' and normalize-space(text())='{size_value}']")
    ADD_TO_CART_BUTTON_MODAL = (By.XPATH, "//button[contains(normalize-space(.), 'В корзину') and contains(@class, 'big-button-first')]")
    