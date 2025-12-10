from selenium.webdriver.common.by import By

class CheckoutLocators:
    """
    Локаторы для страницы оформления и оплаты заказа
    """

    RULES_CHECKBOX = (By.XPATH, "(//span[contains(@class, 'check__box')])[1]")
    SUBSCRIPTION_CHECKBOX = (By.XPATH, "(//span[contains(@class, 'check__box')])[2]")
    GO_TO_PAYMENT_BUTTON = (
    By.XPATH,"//button[contains(@class,'order__fix-button')][contains(translate(.,""'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ',"
    "'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'),"
    "'перейти к оплате')]"
    )
    CHECKOUT_REDIRECT_BUTTON = (
        By.XPATH,
        "//span[contains(translate(normalize-space(.), 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ', 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'), 'перейти к оформлению')]"
    )
    SUCCESS_TITLE = (
        By.XPATH,
        "//h1[contains(@class, 'h1') and contains(translate(normalize-space(text()), 'БЛАГОДАРИМ ВАС ЗА ПОКУПКУ', 'благодарим вас за покупку')]"
    )
