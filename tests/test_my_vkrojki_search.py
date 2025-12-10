import pytest
import allure
from pages.my_vykrojki_page import MyVykrojkiPage


class TestMyVykrojkiSearch:

    @pytest.mark.smoke
    @allure.title("Поиск выкроек 'Руми брюки'")
    def test_search_rumi(self, driver_logged):
        my = MyVykrojkiPage(driver_logged)

        with allure.step("Открываем раздел Мои выкройки"):
            my.open_my_vykrojki_section()

        with allure.step("Ищем выкройки 'Руми брюки'"):
            my.search("Руми брюки")

        with allure.step("Проверяем, что найдены 'Руми брюки'"):
            my.assert_found_pattern_exact("Руми брюки")

    @pytest.mark.smoke
    @allure.title("Поиск выкроек 'Кимико рукавицы'")
    def test_search_kimiko(self, driver_logged):
        my = MyVykrojkiPage(driver_logged)

        with allure.step("Открываем раздел Мои выкройки"):
            my.open_my_vykrojki_section()

        with allure.step("Ищем выкройки 'Кимико рукавицы'"):
            my.search("Кимико рукавицы")

        with allure.step("Проверяем, что найдены 'Кимико рукавицы'"):
            my.assert_found_pattern_exact("Кимико рукавицы")

    