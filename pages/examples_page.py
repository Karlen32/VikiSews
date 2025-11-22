import allure
from pages.base_page import BasePage
from locators.lk_locators import LKLocators
from locators.lk_examples_locators import LKExamplesLocators


class LKExamplesPage(BasePage):

    # ==========================
    #        НАВИГАЦИЯ
    # ==========================
    @allure.step("Открываем раздел 'Примеры работ'")
    def open_examples_section(self):
        self.hover(LKLocators.LK_ICON_BUTTON)
        self.click(LKLocators.MENU_EXAMPLES)

    # ==========================
    #      СОЗДАНИЕ РАБОТЫ
    # ==========================
    @allure.step("Нажимаем кнопку 'Добавить работу'")
    def add_work(self):
        self.click(LKExamplesLocators.ADD_WORK_BUTTON)

    @allure.step("Вводим название работы: {1}")
    def set_work_name(self, value):
        self.send_keys(LKExamplesLocators.WORK_NAME_INPUT, value)

    @allure.step("Вводим описание работы")
    def set_work_description(self, value):
        self.send_keys(LKExamplesLocators.WORK_DESCRIPTION_INPUT, value)

    @allure.step("Загружаем обложку работы")
    def upload_cover(self, file_path):
        el = self.wait_visible(LKExamplesLocators.COVER_UPLOAD_IMAGE_INPUT)
        el.send_keys(file_path)

    @allure.step("Загружаем изображения галереи")
    def upload_gallery_images(self, *image_paths):
        input_el = self.wait_visible(LKExamplesLocators.WORK_IMAGES_UPLOAD_INPUT)
        for img in image_paths:
            input_el.send_keys(img)

    @allure.step("Выбираем продукт: {1}")
    def select_product(self, product_name):
        dropdown = self.wait_visible(LKExamplesLocators.PRODUCT_SELECT_DROPDOWN_BUTTON)

        # скролл, как в исходном тесте
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center', behavior: 'instant'});",
            dropdown
        )
        self.driver.execute_script("window.scrollBy(0, -250);")

        dropdown.click()

        option = self.wait_visible(
            LKExamplesLocators.product_option_by_text(product_name)
        )
        option.click()

    @allure.step("Вводим фамилию автора: {1}")
    def set_author_lastname(self, value):
        self.send_keys(LKExamplesLocators.WORK_AUTHOR_LASTNAME_INPUT, value)

    @allure.step("Вводим имя автора: {1}")
    def set_author_name(self, value):
        self.send_keys(LKExamplesLocators.WORK_AUTHOR_NAME_INPUT, value)

    @allure.step("Публикуем работу")
    def publish_work(self):
        self.click(LKExamplesLocators.WORK_PUBLISH_BUTTON)

    @allure.step("Закрываем окно успешного создания работы")
    def close_success_modal(self):
        btn = self.wait_visible(LKExamplesLocators.SUCCESS_MODAL_CLOSE_BUTTON)
        btn.click()
