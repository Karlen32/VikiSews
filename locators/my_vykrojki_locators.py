from selenium.webdriver.common.by import By  


class MyVykrojkiLocators:


    # Кнопка открытия выпадающего списка (стрелка вниз)
    PATTERN_SORT_OPEN_BUTTON = (
        By.CSS_SELECTOR, 'button.select-secondary__open-button'
    )
    # Радио-кнопка выбора категории "Новая коллекция"
    RADIO_NEW_COLLECTION = (
        By.XPATH, "//label[contains(@class, 'custom-radio-button__wrap')][.//span[contains(text(), 'Новая коллекция')]]"
    )
    # Радио-кнопка выбора категории "Платья и сарафаны"
    RADIO_DRESSES = (
        By.XPATH, "//label[contains(@class, 'custom-radio-button__wrap')][.//span[contains(text(), 'Платья и сарафаны')]]"
    )
    # Радио-кнопка выбора категории "Худи, футболки, лонгсливы"
    RADIO_HOODIES_TSHIRTS_LONGSLEEVES = (
        By.XPATH,
        "//label[contains(@class, 'custom-radio-button__wrap')][.//span[contains(text(), 'Худи, футболки, лонгсливы')]]"
    )
    # Радио-кнопка выбора категории "Топы и футболки"
    RADIO_TOPS_TSHIRTS = (
        By.XPATH,
        "//label[contains(@class, 'custom-radio-button__wrap')][.//span[contains(text(), 'Топы и футболки')]]"
    )
    # Радио-кнопка выбора категории "Брюки, джинсы, шорты"
    RADIO_PANTS_JEANS_SHORTS = (
        By.XPATH,
        "//label[contains(@class, 'custom-radio-button__wrap')][.//span[contains(text(), 'Брюки, джинсы, шорты')]]"
    )
    # Контейнер со списком карточек (верхний блок)
    CARDS_CONTAINER = (By.CSS_SELECTOR, 'div.cards-wrap-five-column')
    # Список карточек внутри контейнера
    CARDS_LIST = (By.CSS_SELECTOR, 'div.cards-wrap-five-column div.card-pattern-wrap')
    
    # ---------------------- Статусы ----------------------

    # Кнопка со статусом "Хочу сшить"
    BUTTON_WANT_TO_SEW = (
        By.XPATH,
        "//div[contains(@class, 'select-switcher__button')][.//span[contains(text(), 'Хочу сшить')]]"
    )

    # Кнопка выбора статуса "Сшито"
    BUTTON_SEWN = (
        By.XPATH,
        "//div[contains(@class, 'select-switcher__button')][.//span[contains(text(), 'сшито')]]"
    )

    # Кнопка выбора статуса "Архив"
    BUTTON_ARCHIVE = (
        By.XPATH,
        "//div[contains(@class, 'select-switcher__button')][.//span[contains(text(), 'архив')]]"
    )

    # Текущий статус карточки "Хочу сшить"
    CARD_STATUS_WANT_TO_SEW = (
        By.XPATH,
        "//span[contains(@class, 'status')][.//span[contains(text(), 'Хочу сшить')]]"
    )

    # Текущий статус карточки "Сшито"
    CARD_STATUS_SEWN = (
        By.XPATH,
        "//span[contains(@class, 'status')][.//span[contains(text(), 'Сшито')]]"
    )

    # Текущий статус карточки "Архив"
    CARD_STATUS_ARCHIVE = (
        By.XPATH,
        "//span[contains(@class, 'status')][.//span[contains(text(), 'Архив')]]"
    )

    # Универсальный локатор кнопки статуса по тексту
    def BUTTON_STATUS(text: str):
        return (
            By.XPATH,
            f"//div[contains(@class, 'select-switcher__button')]"
            f"//span[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), '{text.lower()}')]"
        )

    def CARD_STATUS_BY_TEXT(text: str):
        return (
            By.XPATH,
            f"//span[contains(@class, 'status')]"
            f"//span[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), '{text.lower()}')]"
        )


    # ---------------------- Поиск ----------------------

    # Контейнер поиска (включая выпадашку) — верхний блок
    SEARCH_CONTAINER = (By.CSS_SELECTOR, "div.page-search__wrap.page-search__parent.js-select")

    # Кнопка открытия поиска (лупа) внутри контейнера
    SEARCH_OPEN_BUTTON = (
        By.CSS_SELECTOR,
        "div.page-search__wrap.page-search__parent.js-select button.top-block__btn-icon"
    )

    # Поле ввода поиска внутри контейнера
    SEARCH_INPUT = (
        By.CSS_SELECTOR,
        "div.page-search__wrap.page-search__parent.js-select input.search-form__input"
    )

    # Кнопка отправки поиска (внутри дропдауна)
    SEARCH_SUBMIT_BUTTON = (
        By.CSS_SELECTOR,
        "div.page-search__wrap.page-search__parent.js-select button.base-inline-flex-center"
    )
    
    # Название карточки выкройки
    CARD_NAME = (By.CSS_SELECTOR, "span.card-pattern__name")

    # ---------------------- Карточка выкройки, смена статуса ----------------------


    
