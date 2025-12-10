import pytest
import allure
from pages.examples_page import LKExamplesPage
from data.work_example_data import WORK_EXAMPLE_DATA


class TestLKCreateWorkExample:

    @pytest.mark.smoke
    @allure.title("Создание примера работы в личном кабинете")
    @allure.description("Проверка создания примера работы: заполнение названия, описания, загрузка изображений, выбор продукта, публикация")
    def test_lk_create_work_example(self, driver_logged):

        page = LKExamplesPage(driver_logged)

        with allure.step("Переходим в раздел 'Примеры работ'"):
            page.open_examples_section()

        with allure.step("Открываем форму создания работы"):
            page.add_work()

        with allure.step("Заполняем данные новой работы"):
            page.set_work_name(WORK_EXAMPLE_DATA["work_name"])
            page.set_work_description(WORK_EXAMPLE_DATA["description"])

        with allure.step("Загружаем изображения"):
            page.upload_cover(WORK_EXAMPLE_DATA["images"])
            page.upload_gallery_images(
                WORK_EXAMPLE_DATA["images_2"],
                WORK_EXAMPLE_DATA["images_3"],
                WORK_EXAMPLE_DATA["images_4"],
            )

        with allure.step("Выбираем продукт"):
            page.select_product(WORK_EXAMPLE_DATA["product_name"])

        with allure.step("Заполняем информацию об авторе"):
            page.set_author_lastname(WORK_EXAMPLE_DATA["lastname"])
            page.set_author_name(WORK_EXAMPLE_DATA["name"])

        with allure.step("Публикуем работу"):
            page.publish_work()

        with allure.step("Закрываем окно успешного создания"):
            page.close_success_modal()


        

