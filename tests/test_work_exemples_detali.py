import pytest
import allure
from pages.work_examples_detail_page import WorkExamplesDetailPage
from data.work_example_data import WORK_EXAMPLE_DATA
from pages.favorites_page import FavoritesPage


class TestWorkExamplesDetail:

    @pytest.mark.smoke
    @allure.title("Взаимодействие с примером работы")
    @allure.description("Проверка: избранное, лайк, шаринг, комментарии")
    def test_work_examples_detail(self, driver_logged):

        page = WorkExamplesDetailPage(driver_logged)

        with allure.step("Открываем и выбираем карточку"):
            page.open_burger()
            page.open_work_examples_from_menu()
            page.open_card_by_index(3)

        with allure.step("Добавляем в избранное"):
            page.add_to_favorites()

        with allure.step("Комментарии и лайки"):
            page.go_to_comments()
            page.like_work()

        with allure.step("Шарим"):
            page.open_share()
            page.close_share()

        with allure.step("Пишем комментарий"):
            page.send_comment(
                WORK_EXAMPLE_DATA["comment"],
                WORK_EXAMPLE_DATA["images_2"]
            )

        with allure.step("Проверяем сообщение"):
            msg = page.wait_comment_sent()
            assert msg.text.strip() == "Комментарий отправлен на модерацию"


    @pytest.mark.skip
    @allure.title("Удаление примера работ из избранного")
    def test_delete_work_example_from_favorites(self, driver_logged):
        favorites = FavoritesPage(driver_logged)

        favorites.open_favorites()
        favorites.delete_first_favorite()





