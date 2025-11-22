import pytest
import allure
from pages.courses_page import CoursesPage
from pages.course_detail_page import CourseDetailPage


class TestCoursesBasket:

    @pytest.mark.smoke
    @allure.title("Проверка добавления курса в корзину")
    @allure.description("Проверка редиректа при добавлении курса в корзину")
    def test_add_course_to_basket(self, driver_logged):

        courses = CoursesPage(driver_logged)
        detail = CourseDetailPage(driver_logged)

        with allure.step("Открываем раздел 'Курсы'"):
            courses.open_from_burger()

        with allure.step("Находим и ховерим первую карточку"):
            card = courses.get_first_course()
            courses.hover_course(card)

        with allure.step("Нажимаем кнопку 'В корзину'"):
            courses.click_add_to_basket()

        with allure.step("Проверяем, что произошёл редирект на GetCourse"):
            detail.assert_redirect("https://vikisews.online/mini-kurs-po")




        