from selenium.webdriver.common.by import By


class LKExamplesLocators:
    """Локаторы примеров работ"""

    #Вкладка "Примеры работ" 
    TAB_EXAMPLES = (
        By.XPATH,
        "//div[contains(@class,'personal-cabinet-links__links')]"
        "//span[contains(@class,'link-with-underline__text') and contains(normalize-space(text()), 'Примеры работ')]"
    )

    # Кнопка "Добавить работу"
    ADD_WORK_BUTTON = (
        By.XPATH,
        "//a[@href='/personal/add-work-examples/']"
    )
    
    # Кнопка "Назад к примерам работ"
    BACK_TO_EXAMPLES_BUTTON = (
        By.XPATH,
        "//a[contains(@class, 'button-back') and contains(normalize-space(text()), 'назад к примерам работ')]"
    )
    
    # Поле "Название работы"
    WORK_NAME_INPUT = (By.XPATH,"//div[contains(@class,'js-input-wrap')]//input[@name='work']")

    # Поле "Описание" — textarea
    WORK_DESCRIPTION_INPUT = (By.CSS_SELECTOR,"textarea[name='description']")

    # Кнопка "Загрузить изображение" (иконка с плюсом)
    COVER_UPLOAD_IMAGE_INPUT = (
        By.CSS_SELECTOR,
        "input#image"
    )

    # Поле загрузки нескольких изображений (до 6 фото)
    WORK_IMAGES_UPLOAD_INPUT = (
        By.CSS_SELECTOR,
        "input#images[name='images[]'][multiple]"
    )

    # Кнопка-стрелка для открытия списка связ продуктов
    PRODUCT_SELECT_DROPDOWN_BUTTON = (
        By.XPATH,
        "//span[contains(@class, 'select__open-button')]"
    )

    # Все элементы списка в выпадающем меню
    PRODUCT_SELECT_OPTIONS = (
        By.CSS_SELECTOR,
        "ul.select-secondary__dropdown-list li.js-select-item"
    )
    @staticmethod
    def product_option_by_text(text: str):
        return (
            By.XPATH,
            f"//label[contains(@class,'custom-radio-button__wrap')]"
            f"[.//span[contains(@class,'select-secondary__list-text') and normalize-space(text())='{text}']]"
        )

        # Поле "Фамилия"
    WORK_AUTHOR_LASTNAME_INPUT = (By.CSS_SELECTOR,"input[name='lastname']")

    # Поле "Имя"
    WORK_AUTHOR_NAME_INPUT = (By.CSS_SELECTOR,"input[name='name']")
    
    # Кнопка "Отменить" на странице добавления примера работы
    WORK_CANCEL_BUTTON = (By.CSS_SELECTOR,"button[data-graph-path='cancel-add-work']")

    # Кнопка "Опубликовать" (submit)
    WORK_PUBLISH_BUTTON = (By.CSS_SELECTOR,"button[type='submit'].big-button-first")

    # Модалка "Успешно отправлено"
    SUCCESS_MODAL = (
        By.CSS_SELECTOR,
        "div.graph-modal__container[data-graph-target='success-submitted']"
    )

    # Текст внутри модалки
    SUCCESS_MODAL_TEXT = (
        By.XPATH,
        "//p[contains(text(), 'Работа успешно отправлена на модерацию')]"
    )

    # Кнопка закрытия (нижняя кнопка)
    SUCCESS_MODAL_CLOSE_BUTTON = (
        By.XPATH,
        "//div[contains(@class,'graph-modal__container') and contains(@class,'graph-modal-open')]"
        "//button[contains(@class,'big-button-first') and normalize-space(text())='закрыть']"
    )

    
        