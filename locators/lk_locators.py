from selenium.webdriver.common.by import By


class LKLocators:
    """Локаторы личного кабинета"""

    # Кнопка открытия меню ЛК (иконка человека в шапке)
    LK_ICON_BUTTON = (By.CSS_SELECTOR, "button.header__icon-button.base-inline-flex")
    # Сам выпадающий контейнер
    LK_DROPDOWN = (By.CSS_SELECTOR,"div.lk-dropdown")

    # Меню ЛК — общий список
    LK_MENU_LIST = (By.CSS_SELECTOR,"ul.lk-dropdown__menu")

    # Пункты меню
    LK_MENU_ITEM = (By.CSS_SELECTOR,"ul.lk-dropdown__menu li.lk-dropdown__item")

    # Конкретные пункты меню в хедере
    MENU_HOME = (
        By.XPATH,
        "//a[@href='/' and .//span[contains(text(),'Главная')]]"
    )

    MENU_PROFILE = (
        By.XPATH,
        "//a[@href='/personal' and .//span[contains(text(),'Мой профиль')]]"
    )

    MENU_BONUSES_CERTIFICATES = (
        By.XPATH,
        "//a[@href='/personal/bonus/' and .//span[contains(text(),'Бонусы')]]"
    )

    MENU_ORDERS = (
        By.XPATH,
        "//a[@href='/personal/orders/' and .//span[contains(text(),'Мои заказы')]]"
    )

    MENU_MY_PATTERNS = (
        By.XPATH,
        "//a[@href='/personal/my-patterns/' and .//span[contains(text(),'Мои выкройки')]]"
    )

    MENU_MY_VIDEOGUIDES = (
        By.XPATH,
        "//a[@href='/personal/my-videogaid/' and .//span[contains(text(),'Мои видеоинструкции')]"
    )

    MENU_EXAMPLES = (
        By.XPATH,
        "//a[@href='/personal/examples/' and .//span[contains(text(),'Примеры работ')]]"
    )

    MENU_SUBSCRIPTIONS = (
        By.XPATH,
        "//a[@href='/personal/subscribe/' and .//span[contains(text(),'Подписки')]]"
    )

    # Кнопка "Крутить колесо удачи"
    WHEEL_OF_FORTUNE_BUTTON = (
    By.CSS_SELECTOR,
    "button.personal-cabinet-top-block__wheel-button[data-graph-path='wheel-of-fortune']"
)

    # ---------- ФОТО ПРОФИЛЯ ----------
    PROFILE_PHOTO_BUTTON = (
        By.CSS_SELECTOR,
        "button.personal-cabinet__photo-wrap"
    )

    PROFILE_PHOTO_IMG = (
        By.CSS_SELECTOR,
        "button.personal-cabinet__photo-wrap img.js-img-profile-photo"
    )

    # Меню: изменить / удалить фото
    CHANGE_PHOTO_BUTTON = (
        By.XPATH,
        "//span[text()='Изменить фото']"
    )

    PHOTO_UPLOAD_INPUT = (
        By.CSS_SELECTOR,
        "input.photo-input.js-input-secondary"
    )

    DELETE_PHOTO_BUTTON = (
        By.XPATH,
        "//span[contains(@class,'js-remove-personal-photo') and text()='Удалить фото']"
    )

     # ---- Верхний блок: быстрые переходы ----
    LK_MY_VYKROJKI_BUTTON = (
        By.XPATH,
        "//a[@href='/personal/my-patterns/' and contains(text(), 'выкройки')]"
    )

    LK_MY_GUIDES_BUTTON = (
        By.XPATH,
        "//a[@href='/personal/my-videogaid/' and contains(text(), 'Гайды')]"
    )

    LK_MY_COURSES_BUTTON = (
        By.XPATH,
        "//a[@href='https://vikisews.online/teach/control' and contains(text(), 'курсы')]"
    )

    LK_LESSONS_LIBRARY_BUTTON = (
        By.XPATH,
        "//a[contains(@class, 'personal-cabinet-top-block__my-courses') and @href='/personal/lessons-library/']"
    )

    @staticmethod
    def get_message_locator(text: str):
        return (
            By.XPATH,
            f"//*[contains(@class,'message')]//*[contains(text(), '{text}')]"
        )