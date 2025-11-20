import pytest
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.lk_locators import LKLocators
from locators.lk_personal_locators import LKPersonalLocators
from selenium.webdriver.common.action_chains import ActionChains
from data.credentials import Credentials


class TestLKChangePassword:
    @pytest.mark.smoke
    @allure.title("Изменение пароля в личном кабинете")
    @allure.description("Проверка изменения пароля: ввод нового пароля и подтверждение, сохранение изменений")
    def test_lk_change_password(self, driver_logged):
        driver = driver_logged

        # ---------- 🔐 Открываем меню ЛК ----------
        lk_icon = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(LKLocators.LK_ICON_BUTTON)
        )
        ActionChains(driver).move_to_element(lk_icon).perform()

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(LKLocators.MENU_PROFILE)
        ).click()

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(LKPersonalLocators.CHANGE_PASSWORD_BUTTON)
        ).click()

        new_password_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(LKPersonalLocators.INPUT_NEW_PASSWORD)
        )
        new_password_input.send_keys(Credentials.NEW_PASSWORD["new_password"])


        repeat_password_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(LKPersonalLocators.INPUT_REPEAT_PASSWORD)
        )
        repeat_password_input.send_keys(Credentials.NEW_PASSWORD["repeat_password"])


        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(LKPersonalLocators.SAVE_PASSWORD_BUTTON)
        ).click()


        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(LKPersonalLocators.INPUT_NEW_PASSWORD)
        )





