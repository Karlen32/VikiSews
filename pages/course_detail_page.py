import time
import allure
from pages.base_page import BasePage
from locators.courses_locators import CoursesLocators


class CourseDetailPage(BasePage):

    @allure.step("Открываем модалку по кнопке")
    def open_modal(self, button_locator):
        btn = self.wait_visible(button_locator)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            btn
        )
        time.sleep(0.3)
        self.wait_clickable(button_locator).click()

    @allure.step("Получаем заголовок модалки")
    def get_modal_title(self, title_locator):
        return self.wait_visible(title_locator).text

    @allure.step("Закрываем модалку")
    def close_modal(self):
        self.click(CoursesLocators.MODAL_CLOSE_BUTTON)
        time.sleep(0.3)

    @allure.step("Переходим на GetCourse страницу")
    def go_to_getcourse(self):
        self.click(CoursesLocators.GO_TO_GETCOURSE_BUTTON)
        self.wait.until(lambda d: len(d.window_handles) > 1)

        main = self.driver.current_window_handle
        new_window = [w for w in self.driver.window_handles if w != main][0]

        self.driver.switch_to.window(new_window)

    @allure.step("Проверяем редирект на GetCourse")
    def assert_redirect_getcourse(self, expected_part):
        self.wait.until(lambda d: expected_part in d.current_url.lower())
        assert expected_part in self.driver.current_url.lower(), \
            f"Ожидали переход на {expected_part}, а попали на {self.driver.current_url}"


    @allure.step("Проверяем редирект страницы")
    def assert_redirect(self, expected_part):
        self.wait.until(lambda d: expected_part in d.current_url.lower())
        assert expected_part in self.driver.current_url.lower(), \
            f"Ожидали переход на {expected_part}, а получили {self.driver.current_url}"
