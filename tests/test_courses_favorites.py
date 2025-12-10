import pytest
import allure
from pages.courses_page import CoursesPage
from pages.favorites_page import FavoritesPage


class TestCoursesFavorites:

    @pytest.mark.smoke
    @allure.title("Проверка добавления курса в избранное")
    def test_add_course_to_favorites(self, driver_logged):

        courses = CoursesPage(driver_logged)

        with allure.step("Открываем раздел 'Курсы'"):
            courses.open_from_burger()

        with allure.step("Ховерим по первой карточке"):
            card = courses.get_first_course()
            courses.hover_course(card)

        with allure.step("Добавляем в избранное"):
            fav_btn = courses.click_favorite()

        with allure.step("Проверяем, что курс добавлен в избранное"):
            classes = fav_btn.get_attribute("class")
            assert any(c in classes for c in ["active", "added"]), "❌ Курс не добавлен в избранное"
    
    
    @pytest.mark.skip(reason="не возможно зайти в избранное если добавлен курс")
    @allure.title("Проверка удаления курса из избранного")
    def test_delete_course_from_favorites(self, driver_logged):

        favorites = FavoritesPage(driver_logged)

        with allure.step("Открываем избранное"):
            favorites.open_favorites()

        with allure.step("Удаляем первый курс"):
            favorites.delete_first_favorite()