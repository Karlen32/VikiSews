import allure
from pages.base_page import BasePage
from locators.blog_locators import BlogLocators
from locators.base_locators import BaseLocators


class BlogMainPage(BasePage):

    @allure.step("Открываем бургер-меню")
    def open_burger(self):
        self.click(BaseLocators.BURGER_BUTTON)

    @allure.step("Переходим в раздел 'Блог'")
    def open_blog_from_menu(self):
        self.click(BaseLocators.BURGER_ITEM_BLOG)
        self.wait_visible(BlogLocators.BLOG_CARD)  # ждём любую карточку

    # ===============================
    #        Методы получения
    # ===============================

    @allure.step("Получаем карточку статьи по названию: {title}")
    def get_card_by_title(self, title: str):
        locator = BlogLocators.card_by_title(title)
        card = self.wait_visible(locator)
        return card

    @allure.step("Открываем статью по индексу: {index}")
    def open_article_by_index(self, index: int):
        cards = self.driver.find_elements(*BlogLocators.BLOG_CARD)
        assert len(cards) > index, f"Нет карточки с индексом {index}"

        card = cards[index]
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", card)
        card.click()

        return self.wait_visible(BlogLocators.BLOG_TITLE)

    # ===============================
    #        Методы действий
    # ===============================

    @allure.step("Открываем статью по названию: {title}")
    def open_article_by_title(self, title: str):
        card = self.get_card_by_title(title)
        self.scroll_into_view(BlogLocators.card_by_title(title))
        card.click()
        self.wait_visible(BlogLocators.BLOG_TITLE)

    @allure.step("Открываем статью по индексу: {index}")
    def open_article_by_index(self, index: int):
        cards = self.driver.find_elements(*BlogLocators.BLOG_CARD)
        try:
            card = cards[index]
        except IndexError:
            raise AssertionError(f"❌ Карточки с индексом {index} не существует")

        self.scroll_to_element(card)
        card.click()
        self.wait_visible(BlogLocators.BLOG_TITLE)

    # ===============================
    #   Методы получения данных статьи
    # ===============================

    @allure.step("Получаем заголовок статьи")
    def get_article_title(self):
        return self.wait_visible(BlogLocators.BLOG_TITLE).text

    @allure.step("Получаем короткое описание статьи")
    def get_article_description(self):
        return self.wait_visible(BlogLocators.BLOG_DESCRIPTION).text

    @allure.step("Получаем теги статьи")
    def get_article_tags(self):
        return [t.text for t in self.driver.find_elements(*BlogLocators.BLOG_TAGS_LIST)]

    @allure.step("Получаем дату публикации статьи")
    def get_article_date(self):
        return self.wait_visible(BlogLocators.BLOG_DATE).text

    # ===============================
    #   Вспомогательный скролл
    # ===============================

    def scroll_to_element(self, element):
        """Скроллит именно к элементу, если на вход подан сам element, не локатор."""
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
