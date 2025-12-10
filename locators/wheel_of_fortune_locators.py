from selenium.webdriver.common.by import By


class WheelLocators:
    OPEN_WHEEL_BUTTON = (
        By.CSS_SELECTOR,
        "button.personal-cabinet-top-block__wheel-button[data-graph-path='wheel-of-fortune']"
    )

    SPIN_BUTTON = (
        By.CSS_SELECTOR,
        "button.wheel-modal__big-button.js-wheel-button"
    )

    SPIN_COUNTER = (
        By.CSS_SELECTOR,
        ".wheel-modal__big-button-counter"
    )

    GIFT_CLOSE_BUTTON = (
        By.CSS_SELECTOR,
        "button.wheel-modal__big-button.js-gift-close"
    )

    GIFT_CLOSE_ICON_BUTTON = (
        By.CSS_SELECTOR,
        "button.wheel-modal__close-gift"
    )

    GO_TO_PURCHASES_LINK = (
        By.CSS_SELECTOR,
        "a.wheel-modal__big-button"
    )

