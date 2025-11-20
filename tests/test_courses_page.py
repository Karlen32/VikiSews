from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.base_locators import BaseLocators
from locators.courses_locators import CoursesLocators
from utils.test_helpers import DEFAULT_TIMEOUT
from data.work_example_text_bloc import WorkExampleTextBlock

import pytest
import allure
import time



class TestCoursesPageTexts:

    @pytest.mark.smoke
    @allure.title("Проверка текстов на странице курсов")
    @allure.description("Проверка текстов всех модальных окон на странице курса")
    def test_courses_page_texts(self, driver_logged):
        driver = driver_logged

        # 1. Открываем бургер и переходим в курсы
        WebDriverWait(driver, DEFAULT_TIMEOUT).until(
            EC.element_to_be_clickable(BaseLocators.BURGER_BUTTON)
        ).click()

        WebDriverWait(driver, DEFAULT_TIMEOUT).until(
            EC.element_to_be_clickable(BaseLocators.BURGER_ITEM_COURSES)
        ).click()

        WebDriverWait(driver, DEFAULT_TIMEOUT).until(
            EC.visibility_of_element_located(CoursesLocators.COURSES_TITLE)
        )

        # 2. Открываем первый курс
        courses = WebDriverWait(driver, DEFAULT_TIMEOUT).until(
            EC.presence_of_all_elements_located(CoursesLocators.COURSE_CARD)
        )
        assert courses, "❌ Курсы не найдены"

        courses[0].click()

        # --- Универсальная функция проверки модалки ---
        def check_modal(open_button_locator, title_locator, expected_text):
            # 1) Скроллим К КОНКРЕТНОЙ кнопке
            button_el = WebDriverWait(driver, DEFAULT_TIMEOUT).until(
                EC.presence_of_element_located(open_button_locator)
            )
            driver.execute_script(
                "arguments[0].scrollIntoView({block: 'center'});",
                button_el
            )
            time.sleep(0.3)

            # 2) Ждём, пока она станет кликабельной, и кликаем
            WebDriverWait(driver, DEFAULT_TIMEOUT).until(
                EC.element_to_be_clickable(open_button_locator)
            ).click()

            # 3) Ждём заголовок модалки и проверяем текст
            text = WebDriverWait(driver, DEFAULT_TIMEOUT).until(
                EC.visibility_of_element_located(title_locator)
            ).text

            assert text == expected_text, f"❌ Текст не совпал: '{text}'"

            # 4) Закрываем модалку
            WebDriverWait(driver, DEFAULT_TIMEOUT).until(
                EC.element_to_be_clickable(CoursesLocators.MODAL_CLOSE_BUTTON)
            ).click()

            # 5) Небольшая пауза, чтобы анимация закрытия успела отработать
            time.sleep(0.3)

        # --- Проверки всех модалок ---
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



    @pytest.mark.smoke
    @allure.title("Проверка вида страницы курса")
    @allure.description("Проверка вида страницы курса и перехода на GetCourse")
    def test_course_page_view(self, driver_logged):
        driver = driver_logged

        # 1. Переход в раздел Курсы
        WebDriverWait(driver, DEFAULT_TIMEOUT).until(
            EC.element_to_be_clickable(BaseLocators.COURSES)
        ).click()

        WebDriverWait(driver, DEFAULT_TIMEOUT).until(
            EC.visibility_of_element_located(CoursesLocators.COURSES_TITLE)
        )

        # 2. Получаем список курсов
        courses = WebDriverWait(driver, DEFAULT_TIMEOUT).until(
            EC.presence_of_all_elements_located(CoursesLocators.COURSE_CARD)
        )

        assert len(courses) > 0, "❌ Курсы не найдены"

        # 3. Открываем первый курс
        courses[0].click()

        # Запоминаем текущее окно
        main_window = driver.current_window_handle

        # 4. Кликаем по кнопке перехода на GetCourse
        WebDriverWait(driver, DEFAULT_TIMEOUT).until(
            EC.element_to_be_clickable(CoursesLocators.GO_TO_GETCOURSE_BUTTON)
        ).click()

        # 5. Ждём появления нового окна
        WebDriverWait(driver, DEFAULT_TIMEOUT).until(
            lambda d: len(d.window_handles) > 1
        )

        # 6. Переключаемся в новое окно
        new_window = [w for w in driver.window_handles if w != main_window][0]
        driver.switch_to.window(new_window)

        # 7. Проверяем URL страницы GetCourse
        WebDriverWait(driver, DEFAULT_TIMEOUT).until(
            EC.url_contains("https://vikisews.online/mini-kurs-po")
        )

        assert "https://vikisews.online/mini-kurs-po" in driver.current_url.lower(), \
            f"❌ Редирект не произошёл! Сейчас: {driver.current_url}"


        

        