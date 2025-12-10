import time
import allure
from pages.base_page import BasePage
from locators.blog_locators import BlogDetailLocators


class BlogDetailPage(BasePage):

    # ==========================
    #         ИЗБРАННОЕ
    # ==========================
    @allure.step("Добавляем статью в избранное")
    def add_to_favorites(self):
        fav_btn = self.wait_visible(BlogDetailLocators.FAVORITE_BUTTON)
        fav_count_el = self.wait_visible(BlogDetailLocators.FAVORITE_COUNT)

        before = int(fav_count_el.text.strip() or 0)

        self.driver.execute_script("arguments[0].click();", fav_btn)

        self.wait.until(
            lambda d: int(
                d.find_element(*BlogDetailLocators.FAVORITE_COUNT).text.strip() or 0
            ) == before + 1
        )

    @allure.step("Удаляем статью из избранного")
    def remove_from_favorites(self):
        fav_btn = self.wait_visible(BlogDetailLocators.FAVORITE_BUTTON)
        fav_count_el = self.wait_visible(BlogDetailLocators.FAVORITE_COUNT)

        before = int(fav_count_el.text.strip() or 0)

        self.driver.execute_script("arguments[0].click();", fav_btn)

        self.wait.until(
            lambda d: int(
                d.find_element(*BlogDetailLocators.FAVORITE_COUNT).text.strip() or 0
            ) == max(0, before - 1)
        )

    # ==========================
    #            ЛАЙК
    # ==========================

    @allure.step("Ставим лайк статье")
    def like_article(self):
        # Находим кнопку лайка и счётчик
        like_btn = self.wait_visible(BlogDetailLocators.LIKE_BUTTON)
        count_el = self.wait_visible(BlogDetailLocators.LIKE_COUNT)
        before = int(count_el.text.strip() or 0)
        btn = self.wait_visible(BlogDetailLocators.LIKE_BUTTON)

        self.driver.execute_script("""
            const el = arguments[0];
            el.scrollIntoView({block: 'center', inline: 'nearest'});
        """, btn)
        
        time.sleep(0.2)
        self.driver.execute_script("arguments[0].click();", like_btn)
        self.wait.until(
            lambda d: int(
                d.find_element(*BlogDetailLocators.LIKE_COUNT).text.strip() or 0
            ) == before + 1
        )


    # ==========================
    #           ШАРИНГ
    # ==========================
    @allure.step("Открываем dropdown 'Поделиться'")
    def open_share_dropdown(self):
        btn = self.wait_visible(BlogDetailLocators.SHARE_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", btn)
        self.driver.execute_script("arguments[0].click();", btn)

    @allure.step("Копируем ссылку")
    def copy_link(self):
        self.open_share_dropdown()

        btn = self.wait_visible(BlogDetailLocators.COPY_LINK_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", btn)
        self.driver.execute_script("arguments[0].click();", btn)

        self.wait_visible(BlogDetailLocators.COPIED_MODAL_TEXT)

    # ==========================
    #        КОММЕНТАРИИ
    # ==========================
    @allure.step("Оставляем комментарий")
    def send_comment(self, text, image_path):
        textarea = self.wait_visible(BlogDetailLocators.COMMENT_TEXTAREA)

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});", textarea
        )
        time.sleep(0.3)
        textarea.send_keys(text)

        img_input = self.wait_visible(BlogDetailLocators.COMMENT_UPLOAD_INPUT)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});", img_input
        )
        time.sleep(0.3)
        img_input.send_keys(image_path)

        send_btn = self.wait_visible(BlogDetailLocators.COMMENT_SEND_BUTTON)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});", send_btn
        )
        time.sleep(0.3)
        send_btn.click()

    @allure.step("Ожидаем сообщение 'Комментарий отправлен на модерацию'")
    def wait_comment_sent(self):
        return self.wait_visible(BlogDetailLocators.COMMENT_SENT_MODAL)

    @allure.step("Ждём и закрываем модалку")
    def wait_and_close_comment_sent(self):
        msg = self.wait_comment_sent()
        close_btn = self.wait_visible(BlogDetailLocators.COMMENT_SENT_CLOSE)
        self.driver.execute_script("arguments[0].click();", close_btn)
        return msg



