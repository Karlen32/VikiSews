from selenium.webdriver.common.by import By
    
class FavoritesLocators:
    """
    Локаторы для раздела "Избранное" и "Корзина"
    """

    # Кнопка "В избранное" в шапке
    HEADER_FAVORITES_BUTTON = (
        By.CSS_SELECTOR,
        "a.header__icon-button[href='/personal/favorites/']"
    )
    
    # Заголовок страницы "Избранное"
    FAVORITES_PAGE_TITLE = (
        By.XPATH,
        "//h1[contains(translate(normalize-space(), 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ', "
        "'абвгдеёжзийклмнопрстуфхцчшщъыьюя'), 'избранное')]"
    )

    FAVORITE_ADDED_MESSAGE = (
        By.XPATH,
        "//div[contains(@class,'graph-modal__content-body')]//div[contains(@class,'text-body-s') and contains(., 'Товар добавлен в избранное')]"
    )

    # Кнопка удаления товара из избранного
    FAVORITE_REMOVE_BUTTON = (
        By.CSS_SELECTOR,
        "button.favorite-card__close-button.js-remove-favorite"
    )