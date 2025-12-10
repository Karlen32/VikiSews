from selenium.webdriver.common.by import By

class CoursesLocators:

    # Заголовок страницы "Курсы"
    COURSES_TITLE = (
        By.CSS_SELECTOR,
        "div.top-block__title h1.h1--bold"
    )

    # Карточка курса (контейнер)
    COURSE_CARD = (
        By.CSS_SELECTOR,
        ".card-course"
    )

    # Кнопка "В корзину" внутри карточки курса
    COURSE_CARD_BASKET_BUTTON = (
        By.CSS_SELECTOR,
        ".card-course .block-btns__cart"
    )

    # Кнопка "В избранное" внутри карточки курса
    COURSE_CARD_FAVORITE_BUTTON = (
        By.CSS_SELECTOR,
        ".card-course .block-btns__favorites"
    )

    # Кнопка "Перейти в GetCourse" в правой колонке
    GO_TO_GETCOURSE_BUTTON = (
        By.CSS_SELECTOR,
        ".pattern-right-part__cart-button"
    )

    # Кнопка "В избранное" в правой колонке
    COURSE_FAVORITE_BUTTON = (
        By.CSS_SELECTOR,
        ".pattern-right-part__buttons .js-favorite-course"
    )

    # Кнопка "Закрыть модалку" (универсальная)
    MODAL_CLOSE_BUTTON = (
        By.XPATH,
        "//div[contains(@class,'graph-modal-open')]//button[contains(@class,'js-modal-close')]"
    )

    # Кнопка "Таблица размеров"
    SIZE_TABLE_BUTTON = (
        By.CSS_SELECTOR,
        "button[data-graph-path='size-table']"
    )
    # Заголовок таблицы размеров
    SIZE_TABLE_TITLE = (
        By.XPATH,
        "//p[contains(@class, 'graph-modal__title')][normalize-space()='таблица размеров']"
    )

    # Кнопка "Расход"
    PRODUCT_EXPENSE_BUTTON = (
        By.CSS_SELECTOR,
        "button[data-graph-path='product-expense']"
    )
    # Заголовок таблицы расхода
    EXPENSE_TITLE = (
        By.XPATH,
        "//p[contains(@class, 'graph-modal__title')][normalize-space()='расход']"
    )

    # Кнопка аккордеона "Рекомендуемые материалы"
    RECOMMENDED_MATERIALS_BUTTON = (
        By.CSS_SELECTOR,
        "button.accordion__title[data-graph-path='recomend']"
    )
    # Заголовок аккордеона "Рекомендуемые материалы"
    RECOMMENDED_MATERIALS_TITLE = (
        By.XPATH,
        "//p[contains(@class, 'graph-modal__title')][normalize-space()='Рекомендуемые материалы']"
    )

    # Кнопка аккордеона "Оборудование и приспособления"
    EQUIPMENT_BUTTON = (
        By.CSS_SELECTOR,
        "button.accordion__title[data-graph-path='equipment']"
    )
    # Заголовок аккордеона "Оборудование и приспособления"
    EQUIPMENT_TITLE = (
        By.XPATH,
        "//p[contains(@class,'graph-modal__title')][normalize-space()='Оборудование и приспособления']"
    )

    # Кнопка аккордеона "Что будет отправлено"
    WHAT_GO_TO_YOU_BUTTON = (
        By.CSS_SELECTOR,
        "button.accordion__title[data-graph-path='what-go-to-you']"
    )
    # Заголовок аккордеона "Что будет отправлено"
    WHAT_WILL_BE_SENT_TITLE = (
        By.XPATH,
        "//p[contains(@class, 'graph-modal__title')][normalize-space()='Что будет отправлено']"
    )

    # Кнопка "Длина изделия и рукава"
    PRODUCT_LENGTH_BUTTON = (
        By.CSS_SELECTOR,
        "a.button-secondary[data-graph-path='dlina-izdelia']"
    )
    # Заголовок аккордеона "Длина изделия и рукава"
    PRODUCT_LENGTH_TITLE = (
        By.XPATH,
        "//p[contains(@class,'graph-modal__title')][normalize-space()='Длина изделия и рукава']"
    )

    # Кнопка "Прибавки на свободу облегания"
    FREEDOM_EASE_BUTTON = (
        By.CSS_SELECTOR,
        "a.button-secondary[data-graph-path='svobodOblegania']"
    )

    # Заголовок аккордеона "Прибавки на свободу облегания"
    FREEDOM_EASE_TITLE = (
        By.XPATH,
        "//p[contains(@class,'graph-modal__title')][normalize-space()='Прибавки на свободу облегания']"
    )

    # Кнопка "Примеры работ"
    WORK_EXAMPLES_BUTTON = (
        By.CSS_SELECTOR,
        "button.button-teg[data-graph-path='work-examples']"
    )

