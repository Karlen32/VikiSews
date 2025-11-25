import allure
import time
from pages.base_page import BasePage
from locators.blog_locators import BlogLocators, CommentLocators, ShareModalLocators


class BlogDetailsPage(BasePage):

    # ===============================
    #        ИЗБРАННОЕ
    # ===============================

    @allure.step("Добавляем статью в избранное")
    def add_to_favorites(self):
        fav_btn = self.wait_visible(BlogLocators.FAVORITE_BUTTON)
        fav_count_el = self.wait_visible(BlogLocators.FAVORITE_COUNT)

        before = int(fav_count_el.text.strip() or 0)

        self.driver.execute_script("arguments[0].click();", fav_btn)

        self.wait.until(
            lambda d: int(
                d.find_element(*BlogLocators.FAVORITE_COUNT).text.strip() or 0
            ) == before + 1
        )

    # ===============================
    #          ЛАЙК
    # ===============================

    @allure.step("Ставим лайк статье")
    def like_work(self):
        like_btn = self.wait_visible(BlogLocators.LIKE_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", like_btn)
        time.sleep(0.2)

        # SVG может перекрывать → жёсткий JS-клик
        self.driver.execute_script("arguments[0].click();", like_btn)
        time.sleep(0.5)

    # ===============================
    #        КОММЕНТАРИИ
    # ===============================

    @allure.step("Переходим в раздел комментариев")
    def go_to_comments(self):
        self.click(BlogLocators.COMMENTS_BUTTON)

    @allure.step("Оставляем комментарий к статье")
    def send_comment(self, text: str, image_path: str):
        textarea = self.wait_visible(CommentLocators.COMMENT_TEXTAREA)
        textarea.send_keys(text)

        img_input = self.wait_visible(CommentLocators.UPLOAD_IMAGE_BUTTON)
        img_input.send_keys(image_path)

        self.click(CommentLocators.SUBMIT_COMMENT_BUTTON)

    @allure.step("Проверяем сообщение после отправки комментария")
    def wait_comment_sent(self):
        return self.wait_visible(CommentLocators.COMMENT_SENT_MODAL_TEXT)

    # ===============================
    #           ШАРИНГ
    # ===============================

    @allure.step("Открываем модальное окно шаринга")
    def open_share_modal(self):
        btn = self.wait_visible(ShareModalLocators.SHARE_BUTTON)
        self.scroll_into_view(ShareModalLocators.SHARE_BUTTON)
        time.sleep(0.1)

        self.driver.execute_script("arguments[0].click();", btn)
        self.wait_visible(ShareModalLocators.SHARE_MODAL)

    @allure.step("Закрываем модальное окно шаринга")
    def close_share_modal(self):
        close_btn = self.wait_visible(ShareModalLocators.SHARE_MODAL_CLOSE_BUTTON)
        self.driver.execute_script("arguments[0].click();", close_btn)

