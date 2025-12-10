import allure
from pages.base_page import BasePage
from locators.blog_locators import BlogDetailLocators
from locators.base_locators import BaseLocators


class BlogMainPage(BasePage):

    @allure.step("Открываем бургер-меню")
    def open_burger(self):
        self.click(BaseLocators.BURGER_BUTTON)

    @allure.step("Переходим в раздел 'Блог'")
    def open_blog_from_menu(self):
        self.click(BaseLocators.BURGER_ITEM_BLOG)
        self.wait_visible(BlogDetailLocators.BLOG_CARD)  # ждём появление карточек

    # ===============================
    #        Открытие статьи
    # ===============================

    @allure.step("Открываем статью по индексу: {index}")
    def open_article_by_index(self, index: int):
        cards = self.driver.find_elements(*BlogDetailLocators.BLOG_CARD)

        if len(cards) <= index:
            raise AssertionError(
                f"Нет карточки с индексом {index}. Найдено: {len(cards)}"
            )

        card = cards[index]

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});", card
        )
        card.click()

        # Дождаться детальной статьи
        return self.wait_visible(BlogDetailLocators.BLOG_DETAIL_TITLE)

    @allure.step("Открываем статью по названию: {title}")
    def open_article_by_title(self, title: str):
        locator = BlogDetailLocators.card_by_title(title)
        card = self.wait_visible(locator)

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});", card
        )
        card.click()
        self.wait_visible(BlogDetailLocators.BLOG_DETAIL_TITLE)

    # ===============================
    #   Методы получения данных
    # ===============================

    @allure.step("Получаем заголовок статьи")
    def get_article_title(self):
        return self.wait_visible(BlogDetailLocators.BLOG_DETAIL_TITLE).text

    @allure.step("Получаем описание статьи")
    def get_article_description(self):
        return self.wait_visible(BlogDetailLocators.BLOG_DESCRIPTION).text

    @allure.step("Получаем дату публикации статьи")
    def get_article_date(self):
        return self.wait_visible(BlogDetailLocators.BLOG_DATE).text
