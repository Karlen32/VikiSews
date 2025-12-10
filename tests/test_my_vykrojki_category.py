import pytest
import allure
from pages.my_vykrojki_page import MyVykrojkiPage


class TestMyVykrojkiCategory:
    
    @pytest.mark.smoke
    @allure.title("Фильтрация по категории 'Новая коллекция'")
    def test_filter_collection(self, driver_logged):
        my = MyVykrojkiPage(driver_logged)

        with allure.step("Открываем раздел 'Мои выкройки'"):
            my.open_my_vykrojki_section()

        with allure.step("Открываем список категорий"):
            my.open_sort_dropdown()

        with allure.step("Выбираем категорию 'Новая коллекция'"):
            my.select_category_new_collection()

        with allure.step("Ожидаем обновления списка карточек"):
            my.wait_cards_updated()

        with allure.step("Проверяем список карточек"):
            cards = my.get_cards()
            assert len(cards) > 0, "Список карточек пуст после фильтрации"


    @pytest.mark.smoke
    @allure.title("Фильтрация по категории 'Платья и сарафаны'")
    def test_filter_dresses(self, driver_logged):
        my = MyVykrojkiPage(driver_logged)

        with allure.step("Открываем раздел 'Мои выкройки'"):
            my.open_my_vykrojki_section()

        with allure.step("Открываем список категорий"):
            my.open_sort_dropdown()

        with allure.step("Выбираем категорию 'Платья и сарафаны'"):
            my.select_category_dresses()

        with allure.step("Ожидаем обновления списка карточек"):
            my.wait_cards_updated()

        with allure.step("Проверяем список карточек"):
            cards = my.get_cards()
            assert len(cards) > 0, "Список карточек пуст после фильтрации"


    @pytest.mark.smoke
    @allure.title("Фильтрация по категории 'Худи, футболки, лонгсливы'")
    def test_filter_hoodies_tshirts_longsleeves(self, driver_logged):
        my = MyVykrojkiPage(driver_logged)

        with allure.step("Открываем раздел 'Мои выкройки'"):
            my.open_my_vykrojki_section()

        with allure.step("Открываем список категорий"):
            my.open_sort_dropdown()

        with allure.step("Выбираем категорию 'Худи, футболки, лонгсливы'"):
            my.select_category_hoodies_tshirts_longsleeves()

        with allure.step("Ожидаем обновления списка карточек"):
            my.wait_cards_updated()

        with allure.step("Проверяем список карточек"):
            cards = my.get_cards()
            assert len(cards) > 0, "Список карточек пуст после фильтрации"
    




