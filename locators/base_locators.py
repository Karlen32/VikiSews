from selenium.webdriver.common.by import By

class BaseLocators:
    """
    Локаторы для базовых элементов сайта:
    - Бургер-меню
    - Переход в каталог "Выкройки"
    """

    # Кнопка бургер-меню
    BURGER_BUTTON = (By.CSS_SELECTOR, "button.burger[data-burger]")

    # Пункт меню "Выкройки" (регистронезависимо)
    PATTERNS_SUBMENU_LINK = (
        By.XPATH,
        "//a[.//span[translate(normalize-space(text()), 'ВЫКРОЙКИ', 'выкройки')='выкройки']]"
    )
    # Пункт меню "Курсы" (регистронезависимо)
    COURSES = (
        By.XPATH,
        "//a[@href='/course/']//span[contains(normalize-space(), 'Курсы')]"
    )
    # Ссылка "все выкройки" после нажатие выкройки в меню
    ALL_PATTERNS_LINK = (
        By.XPATH,
        "//a[contains(normalize-space(.), 'все выкройки')]"
    )

    # Бургер-меню
    # Выкройки
    BURGER_ITEM_PATTERNS = (
        By.XPATH,
        "//li[@data-burger-btn='patterns']"
    )

    BURGER_ITEM_COURSES = (
        By.XPATH,
        "//a[contains(@class, 'burger-menu__item-button') and @href='/course/']"
    )

    # Сертификаты
    BURGER_ITEM_CERTIFICATES = (
        By.XPATH,
        "//a[@href='/sertifikaty/']/span[contains(translate(normalize-space(), 'СЕРТИФИКАТЫ', 'сертификаты'), 'сертификаты')]"
    )

    # Блог
    BURGER_ITEM_BLOG = (
        By.XPATH,
        "//a[@href='/blog']/span[contains(normalize-space(), 'блог')]"
    )

    # Примеры работ
    BURGER_ITEM_WORK_EXAMPLES = (
        By.XPATH,
        "//a[@href='/work-examples/']/span[contains(normalize-space(), 'примеры')]"
    )

    # Образы
    BURGER_ITEM_LOOKS = (
        By.XPATH,
        "//a[@href='/obrazy/']/span[contains(normalize-space(), 'образы')]"
    )

