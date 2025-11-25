from selenium.webdriver.common.by import By


class BlogLocators:

    """Генерирует локатор карточки статьи по названию"""
    @staticmethod
    def card_by_title(title: str):
        return (By.XPATH, f"//p[@class='article-card__title' and normalize-space(text())='{title}']/ancestor::a")

    # Вся карточка статьи (кликабельная ссылка)
    BLOG_CARD = (By.CSS_SELECTOR, "div.js-blog-item a.article-card")

    # Заголовок статьи
    BLOG_TITLE = (By.CSS_SELECTOR, ".article-card__title")  # Название статьи в карточке

    # Короткое описание
    BLOG_DESCRIPTION = (By.CSS_SELECTOR, ".article-card__description")  # Превью текста статьи

    # Теги статьи
    BLOG_TAGS = (By.CSS_SELECTOR, ".article-card__tegs-wrap .article-card__teg")  # Список тегов карточки

    # Дата публикации
    BLOG_DATE = (By.CSS_SELECTOR, ".information-activities__date")  # Дата создания статьи

    # Кнопка "Избранное"
    FAVORITE_BUTTON = (
        By.XPATH, 
        "//button[.//span[contains(@class,'in_favorite_text') and contains(text(),'в избранное')]]"
    )

    # Счётчик "В избранном"
    FAVORITE_COUNT = (By.CSS_SELECTOR, "button.button_fav span.in_favorite")

    # Кнопка "Комментарии"
    COMMENTS_BUTTON = (By.CSS_SELECTOR, "a.button-secondary[href='#comments']")

    # Кнопка "Нравится"
    LIKE_BUTTON = (By.CSS_SELECTOR, "button.js-review-btn-like")


class CommentLocators:
    # Поле ввода комментария
    COMMENT_TEXTAREA = (By.CSS_SELECTOR, "textarea[name='comment']")

    # Кнопка "Добавить фото"
    UPLOAD_IMAGE_BUTTON = (By.CSS_SELECTOR, ".comments__upload-img-icon")

    # Кнопка "Отправить комментарий"
    SUBMIT_COMMENT_BUTTON = (By.CSS_SELECTOR, "button.js-set-enable-button")

    # Модальное окно "Комментарий отправлен"
    COMMENT_SENT_MODAL = (By.CSS_SELECTOR, ".graph-modal__content")

    # Текст внутри модалки
    COMMENT_SENT_MODAL_TEXT = (By.ID, "subscribeTitle")


class ShareModalLocators:
    # Модальное окно "Поделиться"
    SHARE_MODAL = (By.CSS_SELECTOR, ".graph-modal__content")

    # Заголовок модалки
    SHARE_MODAL_TITLE = (By.CSS_SELECTOR, ".graph-modal__title")

    # Основная кнопка "поделиться"
    # Основная кнопка "поделиться"
    SHARE_BUTTON = (By.CSS_SELECTOR, "button.js-select-input")

    # Выпадающий список
    SHARE_DROPDOWN = (By.CSS_SELECTOR, ".select-secondary__dropdown")

    # Ссылки соцсетей
    SHARE_VK = (By.XPATH, "//span[text()='vkontakte']/ancestor::a")
    SHARE_TELEGRAM = (By.XPATH, "//span[text()='telegram']/ancestor::a")
    SHARE_PINTEREST = (By.XPATH, "//span[text()='pinterest']/ancestor::a")
    SHARE_TWITTER = (By.XPATH, "//span[text()='twitter']/ancestor::a")
    SHARE_FACEBOOK = (By.XPATH, "//span[text()='facebook']/ancestor::a")

    # Кнопка "Скопировать ссылку"
    COPY_LINK_BUTTON = (By.CSS_SELECTOR, "button.js-copy-link")

    SHARE_MODAL_CLOSE_BUTTON = (
        By.XPATH,
        "//div[@data-graph-target='share']//button[contains(@class,'js-modal-close')]"
    )
