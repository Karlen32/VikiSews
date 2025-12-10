from locators.vykrojki_locators import VykrojkiLocators


class ProductConfig:
    """
    Централизованный конфиг — тут меняем название товара,
    а все тесты автоматически подхватывают новые локаторы.
    """

    NAME = "Сувира манишка"

    HEIGHT = "162-168"
    SIZE = "XL"

    HEIGHT1 = "170-176"
    SIZE1 = "S"

    HEIGHT2 = "162-168"
    SIZE2 = "XS"

    HEIGHT3 = "178-184"
    SIZE3 = "L"


    

    CARD = VykrojkiLocators.pattern_card_by_name(NAME)
    FAVORITE = VykrojkiLocators.favorite_button_by_name(NAME)
    BASKET_DETAIL = VykrojkiLocators.detail_add_to_cart_button(NAME)
    BASKET = VykrojkiLocators.basket_button_by_name(NAME)