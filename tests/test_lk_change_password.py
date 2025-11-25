import pytest
import allure
from pages.lk_page import LKPage
from utils.credentials import Credentials


class TestLKChangePassword:

    @pytest.mark.smoke
    @allure.title("Изменение пароля в личном кабинете")
    @allure.description("Проверка изменения пароля: ввод нового пароля, повтор пароля и сохранение изменений")
    def test_lk_change_password(self, driver_logged):

        lk = LKPage(driver_logged)

        # ---------- Меню ЛК ----------
        lk.open_menu()
        lk.go_to_profile()

        # ---------- Изменение пароля ----------
        lk.open_change_password_modal()
        lk.set_new_password(Credentials.NEW_PASSWORD["new_password"])
        lk.set_repeat_password(Credentials.NEW_PASSWORD["repeat_password"])
        lk.save_new_password()

        # ---------- Проверка ----------
        assert lk.wait_invisible
            







