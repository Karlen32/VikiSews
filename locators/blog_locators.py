from selenium.webdriver.common.by import By


class BlogDetailLocators:
    # ==========================
    #      КАРТОЧКИ БЛОГА
    # ==========================

    BLOG_CARD = (
        By.CSS_SELECTOR,
        "a.article-card"
    )

    @staticmethod
    def card_by_title(title: str):
        return (
            By.XPATH,
            f"//a[contains(@class,'article-card')]"
            f"//p[contains(@class,'article-card__title')][normalize-space()='{title}']"
            f"/ancestor::a"
        )

    BLOG_DETAIL_TITLE = (
        By.XPATH,
        "//h1[contains(@class,'h1--bold')]"
    )

    BLOG_DESCRIPTION = (
        By.CSS_SELECTOR,
        ".article-card__description"
    )

    BLOG_TAGS = (
        By.CSS_SELECTOR,
        ".article-card__tegs-wrap .article-card__teg"
    )

    BLOG_DATE = (
        By.CSS_SELECTOR,
        ".information-activities__date"
    )

    # ==========================
    #         ИЗБРАННОЕ
    # ==========================

    FAVORITE_BUTTON = (By.CSS_SELECTOR, ".button_fav .in_favorite_text")

    FAVORITE_COUNT = (By.CSS_SELECTOR, ".button_fav .in_favorite")

    # ==========================
    #            ЛАЙК
    # ==========================

    LIKE_BUTTON = (By.XPATH, '//*[@id="likeButton"]')

    LIKE_COUNT = (
        By.XPATH,
        "//div[contains(@class,'review__like-block')]//span[@id='spanLikeCount']"
    )

    # ==========================
    #        ПОДЕЛИТЬСЯ
    # ==========================

    SHARE_BUTTON = (
        By.XPATH,
        "//button[contains(@class,'js-select-input')]"
    )

    COPY_LINK_BUTTON = (
        By.CSS_SELECTOR,
        "button.js-copy-link"
    )

    COPIED_MODAL_TEXT = (
        By.XPATH,
        "//*[contains(text(),'Скопировано')]"
    )

    # ==========================
    #        КОММЕНТАРИИ
    # ==========================

    COMMENT_TEXTAREA = (
        By.CSS_SELECTOR,
        "textarea.comments__textarea"
    )

    COMMENT_UPLOAD_INPUT = (
        By.CSS_SELECTOR,
        "input[type='file'][name='image']"
    )

    COMMENT_SEND_BUTTON = (
        By.CSS_SELECTOR,
        "button.js-set-enable-button"
    )

    COMMENT_SENT_MODAL = (
        By.XPATH,
        "//*[@id='subscribeTitle' and contains(normalize-space(),'Комментарий отправлен')]"
    )

    COMMENT_SENT_CLOSE = (
        By.CSS_SELECTOR,
        "button.js-message-close"
    )


    
