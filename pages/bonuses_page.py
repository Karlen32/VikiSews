import allure
import time
from pages.base_page import BasePage
from locators.bonuses_locators import BonusesLocators


class BonusesPage(BasePage):

    @allure.step("Применяем бонусы")
    def apply_bonuses(self, amount: str):
        self.click(BonusesLocators.BONUS_CHECKBOX)
        field = self.wait_visible(BonusesLocators.BONUS_INPUT)
        field.clear()
        field.send_keys(amount)
        self.click(BonusesLocators.BONUS_APPLY_BUTTON)
        self.driver.execute_script("window.scrollBy(0, 300);")
        time.sleep(0.2)
