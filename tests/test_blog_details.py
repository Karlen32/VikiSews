import pytest
import allure
from pages.blog_main_page import BlogMainPage
from pages.blog_detalis_page import BlogDetailPage
from data.work_example_data import WORK_EXAMPLE_DATA



@allure.feature("Блог")
class TestBlogDetails:

    @pytest.mark.smoke
    @allure.title("Добавление статьи в избранное")
    def test_blog_add_to_favorites(self, driver_logged):
        main = BlogMainPage(driver_logged)
        page = BlogDetailPage(driver_logged)

        main.open_burger()
        main.open_blog_from_menu()
        main.open_article_by_index(0)

        page.add_to_favorites()

    @pytest.mark.smoke
    @allure.title("Удаление статьи из избранного")
    def test_blog_remove_from_favorites(self, driver_logged):
        main = BlogMainPage(driver_logged)
        page = BlogDetailPage(driver_logged)

        main.open_burger()
        main.open_blog_from_menu()
        main.open_article_by_index(0)

        page.add_to_favorites()
        page.remove_from_favorites()

    @pytest.mark.skip(reason="Кнопка не кликабельна")
    @allure.title("Ставим лайк статье")
    def test_blog_like(self, driver_logged):
        main = BlogMainPage(driver_logged)
        page = BlogDetailPage(driver_logged)

        main.open_burger()
        main.open_blog_from_menu()
        main.open_article_by_index(0)

        page.like_article()


    @pytest.mark.smoke
    @allure.title("Шаринг — копируем ссылку")
    def test_blog_share(self, driver_logged):
        main = BlogMainPage(driver_logged)
        page = BlogDetailPage(driver_logged)

        main.open_burger()
        main.open_blog_from_menu()
        main.open_article_by_index(0)

        page.copy_link()

    @pytest.mark.smoke
    @allure.title("Отправляем комментарий к статье")
    def test_blog_send_comment(self, driver_logged):
        main = BlogMainPage(driver_logged)
        page = BlogDetailPage(driver_logged)

        main.open_burger()
        main.open_blog_from_menu()
        main.open_article_by_index(0)

        page.send_comment(
            WORK_EXAMPLE_DATA["comment"],
            WORK_EXAMPLE_DATA["images_2"]
        )

        msg = page.wait_and_close_comment_sent()
        assert msg.text.strip() == "Комментарий отправлен на модерацию"


