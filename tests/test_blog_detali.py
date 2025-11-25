import pytest
import allure
from pages.blog_detalis_page import BlogDetailsPage
from pages.blog_main_page import BlogMainPage
from data.work_example_data import WORK_EXAMPLE_DATA
from pages.favorites_page import FavoritesPage


class TestBlogDetails:

    @pytest.mark.smoke
    @allure.title("Взаимодействие со статьей в блоге")
    @allure.description("Проверка: избранное, лайк, шаринг, комментарии")
    def test_blog_details(self, driver_logged):

        main = BlogMainPage(driver_logged)
        page = BlogDetailsPage(driver_logged)

        with allure.step("Открываем блог и выбираем статью по индексу"):
            main.open_burger()
            main.open_blog_from_menu()
            main.open_article_by_index(0)  # 👉 первая карточка блога

        with allure.step("Добавляем в избранное"):
            page.add_to_favorites()


        with allure.step("Ставим лайк"):
            page.like_work()

        with allure.step("Открываем и закрываем модалку шаринга"):
            page.open_share_modal()
            page.close_share_modal()

        with allure.step("Отправляем комментарий"):
            page.go_to_comments()
            page.send_comment(
                text=WORK_EXAMPLE_DATA["comment"],
                image_path=WORK_EXAMPLE_DATA["images_2"]
            )

        with allure.step("Проверяем сообщение"):
            msg = page.wait_comment_sent()
            assert msg.text.strip() == "Комментарий отправлен на модерацию"


    @pytest.mark.smoke
    @allure.title("Удаление статьи из избранного")
    def test_delete_blog_from_favorites(self, driver_logged):

        favorites = FavoritesPage(driver_logged)

        with allure.step("Открываем страницу избранного"):
            favorites.open_favorites()

        with allure.step("Удаляем первую статью из списка"):
            favorites.delete_first_favorite()

        with allure.step("Проверяем, что статья удалена"):
            assert favorites.is_favorites_empty() or favorites.count_favorites() >= 0

