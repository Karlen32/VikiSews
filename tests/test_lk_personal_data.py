import pytest
import allure
from pages.lk_page import LKPage
from data.personal_info_data import PERSONAL_INFO_DATA



class TestLKPersonalData:

    @pytest.mark.smoke
    @allure.title("Изменение персональных данных в личном кабинете")
    @allure.description("Проверка изменения персональных данных: имя, фамилия, параметры тела, рост и сохранение")
    def test_lk_personal_data(self, driver_logged):

        page = LKPage(driver_logged)

        with allure.step("Открываем личный кабинет"):
            page.open_menu()
            page.go_to_profile()

        with allure.step("Вводим персональные данные"):
            page.set_first_name(PERSONAL_INFO_DATA["first_name"])
            page.set_last_name(PERSONAL_INFO_DATA["last_name"])
            page.set_chest(PERSONAL_INFO_DATA["boobs"])
            page.set_waist(PERSONAL_INFO_DATA["waist"])

        
            page.set_hips(PERSONAL_INFO_DATA["hips"])
            page.set_height(PERSONAL_INFO_DATA["height"])

        with allure.step("Сохраняем изменения"):
            page.save_personal_data()

        with allure.step("Проверяем успешное сохранение"):
            message = page.wait_success_message("Данные успешно сохранены")
            assert message is not None

    