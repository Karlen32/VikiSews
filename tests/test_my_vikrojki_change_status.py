import pytest
import allure
from pages.my_vykrojki_page import MyVykrojkiPage


class TestMyVykrojkiChangeStatus:
    @pytest.mark.skip(reason="Не готова")
    @allure.title("Изменение статуса карточки 'Руми брюки' на 'Архив'")
    def test_change_status_for_rumi(self, driver_logged):
        my = MyVykrojkiPage(driver_logged)
        with allure.step("Открываем раздел 'Мои выкройки'"):
            my.open_my_vykrojki_section()

        with allure.step("Меняем статус карточки 'Руми брюки' на 'Архив'"):
            my.change_card_status_to_archive("Руми брюки")

        with allure.step("Переключаем фильтр на 'Архив'"):
            my.change_status("Архив")

        with allure.step("Проверяем, что найдена 'Руми брюки'"):
            my.assert_found_pattern_exact("Руми брюки")



        
