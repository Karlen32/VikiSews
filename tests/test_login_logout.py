import pytest
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from locators.login_logout_locators import LoginLogoutLocators
from data.credentials import Credentials
from locators.lk_locators import LKLocators



class TestLogin:
    """Тест: вход пользователя с валидными данными"""

    @pytest.mark.smoke
    @allure.title("Успешная авторизация пользователя с валидными данными")
    @allure.description("Проверка входа в систему: ввод email и пароля, проверка успешной авторизации")
    def test_login_valid(self, driver_prelogin):
        driver = driver_prelogin

        # ---------- 🔐 Открываем окно авторизации ----------
        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable(LoginLogoutLocators.PROFILE_ICON)
        ).click()

        # ---------- 📧 Вводим email ----------
        email_input = WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located(LoginLogoutLocators.EMAIL_INPUT)
        )
        email_input.send_keys(Credentials.USER["email"])

        # ---------- 🔑 Вводим пароль ----------
        password_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(LoginLogoutLocators.PASSWORD_INPUT)
        )
        password_input.send_keys(Credentials.USER["password"])

        # ---------- 🚀 Отправляем форму ----------
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(LoginLogoutLocators.LOGIN_BUTTON)
        ).click()

        # ---------- 🖱 Наводим курсор на иконку ЛК ----------
        lk_icon = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(LKLocators.LK_ICON_BUTTON)
        )

        ActionChains(driver).move_to_element(lk_icon).perform()

        # ---------- ✉️ Проверяем, что email появился в выпадающем меню ----------
        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(LoginLogoutLocators.USER_EMAIL)
        )

    @pytest.mark.smoke
    @allure.title("Выход пользователя")
    @allure.description("Проверка выхода из системы")
    def test_logout(self, driver_logged):
        driver = driver_logged

        wait = WebDriverWait(driver, 15)

        # ---------- 🔐 Открываем меню ЛК ----------
        lk_icon = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(LKLocators.LK_ICON_BUTTON)
        )
        ActionChains(driver).move_to_element(lk_icon).perform()

        user_email = wait.until(
            EC.visibility_of_element_located(LKLocators.MENU_PROFILE)
        )
        user_email.click()

        wait.until(
            EC.element_to_be_clickable(LoginLogoutLocators.LOGOUT_BUTTON)
        ).click()

        wait.until(
            EC.element_to_be_clickable(LoginLogoutLocators.LOGOUT_CONFIRM_BUTTON)
        ).click()

        assert WebDriverWait(driver, 15).until_not(
            EC.visibility_of_element_located(LKLocators.LK_ICON_BUTTON)
        )