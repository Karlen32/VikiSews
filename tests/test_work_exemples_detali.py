import pytest
import allure
from pages.work_examples_detail_page import WorkExamplesDetailPage
from data.work_example_data import WORK_EXAMPLE_DATA


@allure.feature("Примеры работ")
class TestWorkExamplesDetail:

    @pytest.mark.smoke
    @allure.title("Добавление примера работ в избранное")
    def test_add_to_favorites(self, driver_logged):
        page = WorkExamplesDetailPage(driver_logged)

        page.open_burger()
        page.open_work_examples_from_menu()
        page.open_card_by_index(3)

        page.add_to_favorites()


    @pytest.mark.smoke
    @allure.title("Ставим лайк примеру работ")
    def test_like_work_example(self, driver_logged):
        page = WorkExamplesDetailPage(driver_logged)

        page.open_burger()
        page.open_work_examples_from_menu()
        page.open_card_by_index(3)

        page.go_to_comments()
        page.like_work()


    @pytest.mark.smoke
    @allure.title("Открываем и закрываем окно шаринга")
    def test_share_work_example(self, driver_logged):
        page = WorkExamplesDetailPage(driver_logged)

        page.open_burger()
        page.open_work_examples_from_menu()
        page.open_card_by_index(3)

        page.open_share()
        page.close_share()


    @pytest.mark.smoke
    @allure.title("Отправляем комментарий к примеру работ")
    def test_send_comment(self, driver_logged):
        page = WorkExamplesDetailPage(driver_logged)

        page.open_burger()
        page.open_work_examples_from_menu()
        page.open_card_by_index(3)

        page.send_comment(
            WORK_EXAMPLE_DATA["comment"],
            WORK_EXAMPLE_DATA["images_2"]
        )

        msg = page.wait_comment_sent()
        assert msg.text.strip() == "Комментарий отправлен на модерацию"


    @pytest.mark.smoke
    @allure.title("Удаление примера работ из избранного")
    def test_delete_from_favorites(self, driver_logged):
        page = WorkExamplesDetailPage(driver_logged)

        page.open_burger()
        page.open_work_examples_from_menu()
        page.open_card_by_index(3)

        # Второй клик снимает избранное (toggle)
        page.add_to_favorites()




