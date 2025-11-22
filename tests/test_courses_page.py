import pytest
import allure
from pages.courses_page import CoursesPage
from pages.course_detail_page import CourseDetailPage
from data.work_example_text_bloc import WorkExampleTextBlock
from locators.courses_locators import CoursesLocators


class TestCoursesPageTexts:

    @pytest.mark.smoke
    @allure.title("Проверка текстов на странице курсов")
    def test_courses_page_texts(self, driver_logged):

        courses = CoursesPage(driver_logged)
        detail = CourseDetailPage(driver_logged)

        with allure.step("Открываем страницу курсов"):
            courses.open_from_burger()

        with allure.step("Открываем первый курс"):
            courses.open_course_by_index(0)

        def check_modal(open_btn, title_loc, expected_text):
            detail.open_modal(open_btn)
            text = detail.get_modal_title(title_loc)
            assert text == expected_text, f"Ожидали '{expected_text}', а получили '{text}'"
            detail.close_modal()

        check_modal(
            CoursesLocators.SIZE_TABLE_BUTTON,
            CoursesLocators.SIZE_TABLE_TITLE,
            WorkExampleTextBlock.SIZE_TITLE_TEXT
        )

        check_modal(
            CoursesLocators.PRODUCT_EXPENSE_BUTTON,
            CoursesLocators.EXPENSE_TITLE,
            WorkExampleTextBlock.EXPENSE_TITLE_TEXT
        )

        check_modal(
            CoursesLocators.RECOMMENDED_MATERIALS_BUTTON,
            CoursesLocators.RECOMMENDED_MATERIALS_TITLE,
            WorkExampleTextBlock.RECOMMENDED_MATERIALS_TITLE_TEXT
        )

        check_modal(
            CoursesLocators.EQUIPMENT_BUTTON,
            CoursesLocators.EQUIPMENT_TITLE,
            WorkExampleTextBlock.EQUIPMENT_TITLE_TEXT
        )

        check_modal(
            CoursesLocators.WHAT_GO_TO_YOU_BUTTON,
            CoursesLocators.WHAT_WILL_BE_SENT_TITLE,
            WorkExampleTextBlock.WHAT_WILL_BE_SENT_TITLE_TEXT
        )

        check_modal(
            CoursesLocators.PRODUCT_LENGTH_BUTTON,
            CoursesLocators.PRODUCT_LENGTH_TITLE,
            WorkExampleTextBlock.PRODUCT_LENGTH_TITLE_TEXT
        )

        check_modal(
            CoursesLocators.FREEDOM_EASE_BUTTON,
            CoursesLocators.FREEDOM_EASE_TITLE,
            WorkExampleTextBlock.FREEDOM_EASE_TITLE_TEXT
        )
    
    @allure.title("Проверка вида страницы курса и перехода на GetCourse")
    def test_course_page_view(self, driver_logged):

        courses = CoursesPage(driver_logged)
        detail = CourseDetailPage(driver_logged)

        with allure.step("Открываем страницу курсов"):
            courses.open_from_header()

        with allure.step("Открываем первый курс"):
            courses.open_course_by_index(0)

        with allure.step("Переходим на GetCourse"):
            detail.go_to_getcourse()

        with allure.step("Проверяем URL GetCourse"):
            detail.assert_redirect_getcourse("https://vikisews.online/mini-kurs-po")


        

        