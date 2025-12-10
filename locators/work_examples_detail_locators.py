from selenium.webdriver.common.by import By


class WorkExamplesDetailLocators:
    """Локаторы страницы примера работ"""


    # Примеры работ
    BURGER_ITEM_WORK_EXAMPLES = (
        By.XPATH,
        "//a[@href='/work-examples/']/span[contains(normalize-space(), 'примеры')]"
    )
    # Заголовок страницы "Примеры работ"
    WORK_EXAMPLES_TITLE = (
        By.XPATH,
        "//h1[contains(normalize-space(),'Примеры работ')]"
    )
    # =====Карточка примера работ на странице=====
    # Карточка примера работ
    WORK_EXAMPLES_CARD_LINK = (
        By.XPATH,
        "//a[contains(@class,'card-pattern__link')]"
    )
    
    # Название карточки примера работ
    WORK_EXAMPLES_CARD_TITLE = (
        By.XPATH,
        "//span[contains(@class,'card-pattern__name')]"
    )
    # Описание карточки примера работ
    WORK_EXAMPLES_CARD_DESCRIPTION = (
        By.XPATH,
        "//span[contains(@class,'card-pattern__descrs')]"
    )
    # Счетчик лайков
    WORK_EXAMPLES_CARD_COUNTER_LIKE = (
        By.XPATH,
        "(//div[contains(@class,'card-pattern-info__item')]//span[@class='text-body-xs'])[1]"
    )
    # Счетчик комментариев
    WORK_EXAMPLES_CARD_COUNTER_COMMENTS = (
        By.XPATH,
        "(//div[contains(@class,'card-pattern-info__item')]//span[@class='text-body-xs'])[2]"
    )

    # =====Подробная страница примера работ=====

    # Кнопка "Комментарии"
    USER_ACTIVITY_COMMENTS_BUTTON = (
        By.XPATH,
        '//a[.//span[@data-author-comments]]'
    )
    

    # Кнопка "В избранное"
    USER_ACTIVITY_FAVORITE_BUTTON = (
        By.XPATH,
        '//button[.//span[@data-author-saved]]'
    )

    # Счётчик "В избранном"
    USER_ACTIVITY_FAVORITE_COUNT = (
        By.XPATH,
        "//button[@data-work-example-favorite-button]//span[@data-author-saved]"
    )

    # Счетчик избранных
    USER_ACTIVITY_FAVORITE_COUNT = (
        By.XPATH,
        "//button[@data-work-example-favorite-button]//span[@data-author-saved]"
    )

    # Кнопка "Поделиться"
    SHARE_BUTTON = (
        By.CSS_SELECTOR,
        "button.js-select-input[data-graph-path='share']"
    )

    SHARE_DROPDOWN = (
        By.CSS_SELECTOR,
        ".select-secondary__dropdown-wrap--left"
    )

    SHARE_COPY_LINK = (
        By.CSS_SELECTOR,
        "button.js-copy-link"
    )
    # Модальное окно "Поделиться"
    SHARE_MODAL = (
        By.XPATH,
        "//div[@data-graph-target='share' and contains(@class,'graph-modal-open')]"
    )

    SHARE_MODAL_CLOSE_BUTTON = (
        By.XPATH,
        "//div[@data-graph-target='share']//button[contains(@class,'js-modal-close')]"
    )

    # Кнопка "Нравится"
    LIKE_BUTTON = (
        By.CSS_SELECTOR,
        ".review__like-btn.js-review-btn-like"
    )
    # Блок "Нравится"
    REVIEW_LIKE_BLOCK = (By.CSS_SELECTOR, ".review__like-block")

    # Счетчик лайков
    REVIEW_LIKE_COUNT = (
        By.XPATH,
        "//button[@data-work-example-action='like']//span[@data-liked-value]"
    )

    # Поле ввода комментария
    COMMENTS_TEXTAREA_INPUT = (
        By.XPATH,
        "//textarea[@name='comment' and contains(@class,'js-set-enable-input')]"
    )

    # Кнопка добавления фото (input)
    COMMENTS_UPLOAD_IMAGE_INPUT = (
        By.XPATH,
        "//input[@type='file' and @id='upload-img-1']"
    )

    # Кнопка добавления фото (кликабельная часть)
    COMMENTS_UPLOAD_IMAGE_BUTTON = (
        By.XPATH,
        "//label[@for='upload-img-1']"
    )

    # Кнопка отправить
    COMMENTS_SEND_BUTTON = (
        By.XPATH,
        "//button[contains(@class,'js-set-enable-button')]"
    )

    COMMENT_SENT_MODAL_TEXT = (
        By.CSS_SELECTOR,
        "#subscribeTitle"
    )

                    

    










