import pytest
import allure
from pages.my_vykrojki_page import MyVykrojkiPage



class TestMyVykrojkiFilterStatus:

    @pytest.mark.smoke
    @allure.title("Изменение статуса карточек на 'Сшито'")
    def test_change_status_to_sewn(self, driver_logged):
        my = MyVykrojkiPage(driver_logged)

        with allure.step("Открываем раздел 'Мои выкройки'"):
            my.open_my_vykrojki_section()

        with allure.step("Меняем статус карточек на 'Сшито'"):
            my.change_status("Сшито")

        with allure.step("Проверяем, что все карточки имеют статус 'Сшито'"):
            my.assert_all_cards_have_status("Сшито")


    @pytest.mark.smoke
    @allure.title("Изменение статуса карточек на 'Архив'")
    def test_change_status_to_archive(self, driver_logged):
        my = MyVykrojkiPage(driver_logged)

        with allure.step("Открываем раздел 'Мои выкройки'"):
            my.open_my_vykrojki_section()

        with allure.step("Меняем статус карточек на 'Архив'"):
            my.change_status("Архив")

        with allure.step("Проверяем, что все карточки имеют статус 'Архив'"):
            my.assert_all_cards_have_status("Архив")

    @pytest.mark.smoke
    @allure.title("Изменение статуса карточек на 'Хочу сшить'")
    def test_change_status_to_want_to_sew(self, driver_logged):
        my = MyVykrojkiPage(driver_logged)

        with allure.step("Открываем раздел 'Мои выкройки'"):
            my.open_my_vykrojki_section()

        with allure.step("Переключаемся на статус 'Хочу сшить'"):
            my.change_status("Хочу сшить")

        with allure.step("Проверяем, что все карточки имеют статус 'Хочу сшить'"):
            my.assert_all_cards_have_status("Хочу сшить")
