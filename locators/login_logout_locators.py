from selenium.webdriver.common.by import By


class LoginLogoutLocators:
    # Иконка профиля / входа
    PROFILE_ICON = (By.XPATH, "//button[@data-graph-path='login-with-email']")
    LOGIN_ICON = (By.XPATH, "//svg[path[contains(@d, 'M9.9923 2.70573')]]")

    # Имя пользователя
    USER_NAME = (By.CSS_SELECTOR,".comments__author-right-part p.text-body-xs")

    # Email пользователя
    USER_EMAIL = (By.CSS_SELECTOR,".comments__author-right-part a[href^='mailto']")

    # Кнопка выхода
    LOGOUT_BUTTON = (By.CSS_SELECTOR,"button[data-graph-path='logout']")

    # Кнопка выхода в модальном окне
    LOGOUT_CONFIRM_BUTTON = (By.CSS_SELECTOR,".graph-modal__footer a[href='/personal/logout.php']")

    # Заголовок модального окна входа/регистрации
    LOGIN_MODAL_TITLE = (By.XPATH, "//p[contains(@class, 'graph-modal__title') and normalize-space()='вход или регистрация']")

    # Поля ввода
    EMAIL_INPUT = (By.CSS_SELECTOR, "input.js-email")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input.js-password")

    # Кнопки показа / скрытия пароля
    SHOW_PASSWORD_BUTTON = (By.XPATH, "//button[contains(@class, 'password-open')]")
    HIDE_PASSWORD_BUTTON = (By.XPATH, "//button[contains(@class, 'password-close')]")

    # Кнопка входа
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit' and normalize-space()='войти']")




