from locators.vykrojki_locators import VykrojkiLocators


class ProductConfig:
    """
    Централизованный конфиг — тут меняем название товара,
    а все тесты автоматически подхватывают новые локаторы.
    """

    NAME = "Джуанна платье"

     # Параметры по умолчанию
    HEIGHT = "162-168"
    SIZE = "38"

     # Параметры по умолчанию
    HEIGHT1 = "170-176"
    SIZE1 = "34"
    

    CARD = VykrojkiLocators.pattern_card_by_name(NAME)
    FAVORITE = VykrojkiLocators.favorite_button_by_name(NAME)
    BASKET_DETAIL = VykrojkiLocators.detail_add_to_cart_button(NAME)
    BASKET = VykrojkiLocators.basket_button_by_name(NAME)