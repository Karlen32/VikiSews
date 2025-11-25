import pytest
import allure
from pages.login_page import LoginPage
from pages.lk_page import LKPage
from utils.credentials import Credentials


class TestLogin:

    @pytest.mark.smoke
    @allure.title("Успешная авторизация пользователя с валидными данными")
    def test_login_valid(self, driver_prelogin):

        login = LoginPage(driver_prelogin)
        lk = LKPage(driver_prelogin)

        lk.click_login_icon()
        login.enter_email(Credentials.USER["email"])
        login.enter_password(Credentials.USER["password"])
        login.submit()

        lk.open_menu()

        assert lk.user_email_visible(), "Email пользователя не отображается — вход не выполнен"

    @pytest.mark.smoke
    @allure.title("Выход пользователя")
    def test_logout(self, driver_login_ui):

        lk = LKPage(driver_login_ui)
        login = LoginPage(driver_login_ui)

        # ---------- Логаут ----------
        lk.open_menu()
        lk.go_to_profile()
        login.logout_button()
        login.logout_confirm_button()

        # ---------- Проверка ----------
        assert login.email_input_visible(), "Пользователь не вышел из аккаунта"

