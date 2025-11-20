from selenium.webdriver.common.by import By


class LKPersonalDataLocators:
    """Локаторы данных пользователя"""
    
    # Вкладка "Мой профиль"
    TAB_MY_PROFILE = (
        By.XPATH,
        "//a[@href='/personal/']//span[contains(text(), 'Мой профиль')]"
    )
      # Поле «Имя»
    INPUT_FIRST_NAME = (By.NAME,"NAME")

    # Поле «Фамилия»
    INPUT_LAST_NAME = (By.NAME,"LAST_NAME")

    # Поле «Обхват груди»
    INPUT_CHEST_GIRTH = (By.NAME,"UF_BOOBS")

    # Поле «Обхват талии»
    INPUT_WAIST_GIRTH = (By.NAME,"UF_CHEST")

    # Поле «Обхват бёдер»
    INPUT_HIPS_GIRTH = (By.NAME,"UF_BUTS")

    # Поле «Рост»
    INPUT_HEIGHT = (By.NAME,"UF_HEIGHT")

    # Сообщение об ошибке под полями
    ERROR_MESSAGE = (By.CSS_SELECTOR,"span.input__error-message")

    # Кнопка «Сохранить изменения»
    SAVE_CHANGES_BUTTON = (By.CSS_SELECTOR,"input[type='submit'][name='save']")