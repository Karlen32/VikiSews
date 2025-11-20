from selenium.webdriver.common.by import By



class BurgerMenuLocators:
    """Локаторы меню бургера"""

    # Кнопка бургер-меню
    BURGER_BUTTON = (By.CSS_SELECTOR, "button.burger[data-burger]")

    # Сам список в бургер-меню
    BURGER_MENU_LIST = (
        By.CSS_SELECTOR,
        "ul.burger-menu__list"
    )

    # Пункт "Выкройки"
    BURGER_ITEM_PATTERNS = (
        By.XPATH,
        "//li[@data-burger-btn='patterns']//span[contains(text(),'Выкройки')]"
    )

    # Пункт "Курсы"
    BURGER_ITEM_COURSES = (
        By.XPATH,
        "//li/a[contains(@href,'/course/')]/span[contains(text(),'Курсы')]"
    )

    # Пункт "Сертификаты"
    BURGER_ITEM_CERTIFICATES = (
        By.XPATH,
        "//li/a[contains(@href,'/sertifikaty/')]/span[contains(text(),'сертификаты')]"
    )

    # Пункт "Блог"
    BURGER_ITEM_BLOG = (
        By.XPATH,
        "//li/a[contains(@href,'/blog/')]/span[contains(text(),'блог')]"
    )

    # Пункт "Примеры работ"
    BURGER_ITEM_WORK_EXAMPLES = (
        By.XPATH,
        "//li/a[contains(@href,'/work-examples/')]/span[contains(text(),'примеры работ')]"
    )

    # Пункт "Образы"
    BURGER_ITEM_OUTFITS = (
        By.XPATH,
        "//li/a[contains(@href,'/obrazy/')]/span[contains(text(),'образы')]"
    )

    
