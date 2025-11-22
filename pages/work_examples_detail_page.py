import time
import allure
from pages.base_page import BasePage
from locators.work_examples_detail_locators import WorkExamplesDetailLocators
from locators.base_locators import BaseLocators


class WorkExamplesDetailPage(BasePage):

    # ==========================
    #        НАВИГАЦИЯ
    # ==========================
    @allure.step("Открываем бургер-меню")
    def open_burger(self):
        self.click(BaseLocators.BURGER_BUTTON)

    @allure.step("Переходим в раздел 'Примеры работ'")
    def open_work_examples_from_menu(self):
        self.click(BaseLocators.BURGER_ITEM_WORK_EXAMPLES)
        self.wait_visible(WorkExamplesDetailLocators.WORK_EXAMPLES_TITLE)

    @allure.step("Открываем карточку № {1}")
    def open_card_by_index(self, index):
        cards = self.wait.until(
            lambda d: d.find_elements(
                *WorkExamplesDetailLocators.WORK_EXAMPLES_CARD_LINK
            )
        )

        assert len(cards) > index, "Недостаточно карточек для клика"

        card = cards[index]

        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", card)
        self.wait.until(lambda d: card.is_enabled())

        card.click()

        self.wait.until(lambda d: "/work-examples/" in d.current_url)

    # ==========================
    #         ИЗБРАННОЕ
    # ==========================
    @allure.step(" Добавляем пример в избранное")
    def add_to_favorites(self):
        fav_btn = self.wait_visible(WorkExamplesDetailLocators.USER_ACTIVITY_FAVORITE_BUTTON)
        fav_count_el = self.wait_visible(WorkExamplesDetailLocators.USER_ACTIVITY_FAVORITE_COUNT)

        before = int(fav_count_el.text.strip() or 0)

        self.driver.execute_script("arguments[0].click();", fav_btn)

        self.wait.until(
            lambda d: int(
                d.find_element(*WorkExamplesDetailLocators.USER_ACTIVITY_FAVORITE_COUNT).text.strip() or 0
            ) == before + 1
        )

    # ==========================
    #         КОММЕНТАРИИ
    # ==========================
    @allure.step("Переходим в раздел комментариев")
    def go_to_comments(self):
        self.click(WorkExamplesDetailLocators.USER_ACTIVITY_COMMENTS_BUTTON)

    @allure.step("Ставим лайк работе")
    def like_work(self):
        like_btn = self.wait_visible(WorkExamplesDetailLocators.LIKE_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", like_btn)

        time.sleep(0.3)

        self.driver.execute_script("arguments[0].click();", like_btn)
        time.sleep(0.6)

    # ==========================
    #           ШАРИНГ
    # ==========================
    @allure.step("Открываем модалку шаринга")
    def open_share(self):
        share_btn = self.wait_visible(WorkExamplesDetailLocators.SHARE_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", share_btn)
        time.sleep(0.2)

        self.driver.execute_script("arguments[0].click();", share_btn)

        self.wait_visible(WorkExamplesDetailLocators.SHARE_MODAL)

    @allure.step("Закрываем модалку шаринга")
    def close_share(self):
        close_btn = self.wait_visible(WorkExamplesDetailLocators.SHARE_MODAL_CLOSE_BUTTON)
        self.driver.execute_script("arguments[0].click();", close_btn)

    # ==========================
    #     ОТПРАВКА КОММЕНТАРИЯ
    # ==========================
    @allure.step("Оставляем комментарий")
    def send_comment(self, text, image_path):
        input_el = self.wait_visible(WorkExamplesDetailLocators.COMMENTS_TEXTAREA_INPUT)
        input_el.send_keys(text)

        img_input = self.wait_visible(WorkExamplesDetailLocators.COMMENTS_UPLOAD_IMAGE_INPUT)
        img_input.send_keys(image_path)

        self.click(WorkExamplesDetailLocators.COMMENTS_SEND_BUTTON)

    @allure.step("Проверяем сообщение после отправки")
    def wait_comment_sent(self):
        modal = self.wait_visible(WorkExamplesDetailLocators.COMMENT_SENT_MODAL_TEXT)
        return modal
