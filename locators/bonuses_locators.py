from selenium.webdriver.common.by import By

class BonusesLocators:
    """
    Локаторы для блока оплаты бонусами
    """

    BONUS_CHECKBOX = (By.XPATH, "(//span[contains(@class, 'check__box--bonus')])[2]")
    BONUS_INPUT = (By.ID, "WANT_SPEND")
    BONUS_APPLY_BUTTON = (
        By.XPATH,
        "//div[@id='bonus']//button[contains(@class, 'input__send-button')]"
    )
