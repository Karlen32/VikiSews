import pytest
import allure
from pages.login_page import LoginPage
from pages.lk_page import LKPage
from data.credentials import Credentials
from locators.lk_locators import LKLocators


class TestLogin:

    @pytest.mark.smoke
    @allure.title("Успешная авторизация пользователя с валидными данными")
    def test_login_valid(self, driver_prelogin):

        login = LoginPage(driver_prelogin)
        lk = LKPage(driver_prelogin)

        login.open_login()
        login.enter_email(Credentials.USER["email"])
        login.enter_password(Credentials.USER["password"])
        login.submit()

        lk.open_menu()

        assert lk.email_visible()

    @pytest.mark.smoke
    @allure.title("Выход пользователя")
    def test_logout(self, driver_logged):

        lk = LKPage(driver_logged)

        lk.open_menu()
        lk.select_profile()
        lk.logout()

        assert lk.wait_not_visible(LKLocators.LK_ICON_BUTTON)
