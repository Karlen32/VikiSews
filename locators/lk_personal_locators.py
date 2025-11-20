from selenium.webdriver.common.by import By

class LKPersonalLocators:
    """Локаторы личного кабинета"""

    
      # Контейнер вкладок
    TABS_CONTAINER = (
        By.CSS_SELECTOR,
        "div.personal-cabinet-links__links"
    )

    # 1. Вкладка «Мой профиль»
    TAB_MY_PROFILE = (
        By.XPATH,
        "//div[contains(@class,'personal-cabinet-links__links')]"
        "//a[@href='/personal/']"
    )

    # 2. Вкладка «Бонусы / Сертификаты»
    TAB_BONUSES = (
        By.XPATH,
        "//div[contains(@class,'personal-cabinet-links__links')]"
        "//a[@href='/personal/bonus/']"
    )

    # 3. Вкладка «Мои заказы»
    TAB_ORDERS = (
        By.XPATH,
        "//div[contains(@class,'personal-cabinet-links__links')]"
        "//a[@href='/personal/orders/']"
    )

    # 4. Вкладка «Примеры работ»
    TAB_EXAMPLES = (
        By.XPATH,
        "//div[contains(@class,'personal-cabinet-links__links')]"
        "//a[@href='/personal/examples/']"
    )

    # 5. Вкладка «Подписки»
    TAB_SUBSCRIPTIONS = (
        By.XPATH,
        "//div[contains(@class,'personal-cabinet-links__links')]"
        "//a[@href='/personal/subscribe/']"
    )

    # Активная вкладка
    ACTIVE_TAB = (
        By.CSS_SELECTOR,
        "a.link-with-underline.active.js-active-tab"
    )
    
     
    """ Локаторы окна смены пароля """
    
    # Кнопка изменения пароля
    CHANGE_PASSWORD_BUTTON = (
    By.XPATH,
    "//button[contains(@class,'credentials__change-password') and contains(normalize-space(text()), 'изменить пароль')]"
    )

     # Поле ввода нового пароля
    INPUT_NEW_PASSWORD = (
        By.ID,
        "passwordNew"
    )
    # Новый пароль – закрыть глаз
    NEW_PASSWORD_CLOSE = (
        By.XPATH,
        "//span[text()='Новый пароль']/following-sibling::button[contains(@class,'password-close')]"
    )

    # Новый пароль – открыть глаз
    NEW_PASSWORD_OPEN = (
        By.XPATH,
        "//span[text()='Новый пароль']/following-sibling::button[contains(@class,'password-open')]"
    )

    # Поле «Повторить пароль»
    INPUT_REPEAT_PASSWORD = (
        By.ID,
        "passwordRepeat"
    )

    # Повторите пароль – закрыть глаз
    REPEAT_PASSWORD_CLOSE = (
        By.XPATH,
        "//span[text()='Повторить пароль']/following-sibling::button[contains(@class,'password-close')]"
    )

    # Повторите пароль – открыть глаз
    REPEAT_PASSWORD_OPEN = (
        By.XPATH,
        "//span[text()='Повторить пароль']/following-sibling::button[contains(@class,'password-open')]"
    )
    # Кнопка «Сохранить» 
    SAVE_PASSWORD_BUTTON = (
        By.XPATH,
        "//button[@type='submit' and normalize-space()='сохранить']"
    )