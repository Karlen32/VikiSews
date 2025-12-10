from selenium.webdriver.common.by import By


class LKBonusCertificatesBuyLocators:
    """Локаторы покупки бонусных сертификатов"""
    
    # Вкладка "Бонусы/сертификаты"
    TAB_BONUSES = (
        By.XPATH,
        "//div[contains(@class,'personal-cabinet-links__links')]"
        "//a[@href='/personal/bonus/']"
    )

    # Кнопка "Условия программы"
    PROGRAM_CONDITIONS_BUTTON = (
        By.XPATH,
        "//button[contains(@class,'button-secondary') and contains(normalize-space(text()), 'условия программы')]"
    )

    # Кнопка "Приобрести сертификат"
    BUY_CERTIFICATE_BUTTON = (
    By.XPATH,
    "//a[contains(@class, 'button-secondary') and contains(normalize-space(text()), 'приобрести сертификат')]"
    )
    # Кнопка "У меня уже есть код"
    ENTER_CERTIFICATE_CODE_BUTTON = (
    By.XPATH,
    "//button[contains(@class, 'button-secondary') and contains(@class, 'button-secondary--full') "
    "and contains(normalize-space(text()), 'у меня уже есть код')]"
    )


    """ Модальное окно "Условия программы" """
    PROGRAM_CONDITIONS_MODAL = (
        By.XPATH,
        "//div[contains(@class,'graph-modal__container') and @data-graph-target='program-conditions']"
    )

    # Заголовок модального окна "Условия программы"
    PROGRAM_CONDITIONS_TITLE = (
        By.XPATH,
        "//div[@data-graph-target='program-conditions']//p[contains(@class,'graph-modal__title') "
        "and normalize-space(text())='Условия программы']"
    )

    # Основной текст внутри модалки
    PROGRAM_CONDITIONS_TEXT = (
        By.XPATH,
        "//div[@data-graph-target='program-conditions']//div[contains(@class,'graph-modal__content-body')]//p"
    )

    # Верхняя кнопка-крестик (закрыть)
    PROGRAM_CONDITIONS_CLOSE_ICON = (
        By.XPATH,
        "//div[@data-graph-target='program-conditions']//button[contains(@class,'js-modal-close') "
        "and contains(@class,'graph-modal__close')]"
    )

    # Нижняя кнопка "закрыть"
    PROGRAM_CONDITIONS_CLOSE_BUTTON = (
        By.XPATH,
        "//div[@data-graph-target='program-conditions']//button[contains(@class,'big-button-first') "
        "and contains(normalize-space(text()), 'закрыть')]"
    )

    """ Цвета сертификатов """
    # Первый цвет сертификата (салатовый)
    CERTIFICATE_COLOR_1_GREEN = (
        By.XPATH,
        "//div[contains(@class,'certificate__card') and contains(@style, 'rgb(195, 235, 16)')]"
    )

        # Второй цвет сертификата (тоже салатовый, второй в списке)
    CERTIFICATE_COLOR_2_GREEN = (
        By.XPATH,
        "(//div[contains(@class,'certificate__card') and contains(@style, 'rgb(195, 235, 16)')])[2]"
    )
    # Третий цвет сертификата (голубой)
    CERTIFICATE_COLOR_3_BLUE = (
    By.XPATH,
    "//div[contains(@class,'certificate__card') and contains(@style, 'rgb(113, 204, 255)')]"
    )

    """ Поле ввода цены сертификата """
    # Поле ввода цены сертификата
    CERTIFICATE_PRICE_INPUT = (
        By.CSS_SELECTOR,
        "input.js-range-slider-price"
    )

    # Блок noUiSlider
    CERTIFICATE_PRICE_SLIDER = (By.ID,"m-slider")

    # Ползунок слева
    CERTIFICATE_SLIDER_HANDLE_LEFT = (
        By.CSS_SELECTOR,
         "#m-slider .noUi-handle-lower"
    )

    # Отображение минимальной цены
    CERTIFICATE_PRICE_MIN_TEXT = (
        By.XPATH,
        "//div[@class='filters-detailed__prices base-flex-justify-content text-body-xs text-body-xs--gray']/span[1]"
    )

    # Отображение максимальной цены
    CERTIFICATE_PRICE_MAX_TEXT = (
        By.XPATH,
        "//div[@class='filters-detailed__prices base-flex-justify-content text-body-xs text-body-xs--gray']/span[2]"
    )
    
    # Блок диапазона цен
    CERTIFICATE_RANGE_BLOCK = (
        By.CSS_SELECTOR,
        ".certificate__range.js-slider-one-price"
    )

        # Табы выбора: "Себе"
    CERTIFICATE_TAB_FOR_MYSELF = (By.ID,"js-tabs1")

    # Табы выбора: "Другу"
    CERTIFICATE_TAB_FOR_FRIEND = (By.ID,"js-tabs2")


    """Локаторы формы подарка сертификата другу."""

    # Поле "Кому*"
    FIELD_TO_WHOM = (By.NAME,"whom")

    # Поле "От кого"
    FIELD_FROM_WHO = (By.NAME,"from")

    # Поле "Текст поздравления"
    FIELD_CONGRATS_TEXTAREA = (By.NAME,"description")

    # Текущий счетчик символов "0"
    TEXT_CURRENT_COUNT = (By.CSS_SELECTOR,"span.js-characters-current")

    # Максимум символов "/ 200"
    TEXT_MAX_COUNT = (By.CSS_SELECTOR,"span.js-characters-max")

    # --- Переключатели способа доставки ---
        # Кнопка "По email"
    TAB_SEND_EMAIL = (
        By.XPATH,
        "//button[.//span[contains(text(), 'по email')]]"
    )

    # Кнопка "По телефону"
    TAB_SEND_PHONE = (
        By.XPATH,
        "//button[.//span[contains(text(), 'по телефону')]]"
    )


    # --- Поля email / телефон ---
    # Поле "Email*"
    FIELD_EMAIL = (By.NAME,"email")

    # Поле "Телефон*"
    FIELD_PHONE = (By.CSS_SELECTOR, "input[data-name='certificatePhone']")

    # --- Кнопка продолжения ---
    # Кнопка "Дальше"
    NEXT_BUTTON = (
        By.CSS_SELECTOR,
        ".pattern-right-part__buttons-wrap--fixed button.certNext"
    )

    # Кнопка «Перейти к оплате»
    PAY_BUTTON = (By.CSS_SELECTOR,"button.pay-button")

