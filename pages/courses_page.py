import allure
from pages.base_page import BasePage
from locators.base_locators import BaseLocators
from locators.courses_locators import CoursesLocators
import time
from selenium.webdriver import ActionChains


class CoursesPage(BasePage):

    @allure.step("Открываем раздел 'Курсы' через бургер-меню")
    def open_from_burger(self):
        self.click(BaseLocators.BURGER_BUTTON)
        self.click(BaseLocators.BURGER_ITEM_COURSES)
        self.wait_visible(CoursesLocators.COURSES_TITLE)

    @allure.step("Открываем раздел 'Курсы' через главное меню")
    def open_from_header(self):
        self.click(BaseLocators.COURSES)
        self.wait_visible(CoursesLocators.COURSES_TITLE)

    @allure.step("Получаем список карточек курсов")
    def get_courses(self):
        return self.wait.until(
            lambda d: d.find_elements(*CoursesLocators.COURSE_CARD)
        )

    @allure.step("Открываем курс по индексу: {1}")
    def open_course_by_index(self, index):
        courses = self.get_courses()
        assert len(courses) > index, "Курсов меньше, чем ожидалось"

        courses[index].click()

    @allure.step("Берём первую карточку курса")
    def get_first_course(self):
        cards = self.get_courses()
        assert len(cards) > 0, "Курсы не найдены"
        card = cards[0]
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});", card
        )
        return card

    @allure.step("Делаем hover на карточку курса")
    def hover_course(self, card):
        time.sleep(1)
        ActionChains(self.driver).move_to_element(card).pause(0.4).perform()

        # JS hover — как в твоём тесте
        self.driver.execute_script("""
            arguments[0].dispatchEvent(new MouseEvent('mouseover', {bubbles:true}));
            arguments[0].dispatchEvent(new MouseEvent('mouseenter', {bubbles:true}));
        """, card)

    @allure.step("Кликаем по избранному на карточке курса")
    def click_favorite(self):
        fav_btn = self.wait_clickable(CoursesLocators.COURSE_CARD_FAVORITE_BUTTON)
        fav_btn.click()
        return fav_btn  # чтобы потом проверить какие классы есть

    @allure.step("Нажимаем кнопку 'В корзину' на карточке курса")
    def click_add_to_basket(self):
        btn = self.wait_clickable(CoursesLocators.COURSE_CARD_BASKET_BUTTON)
        btn.click()

    @allure.step("Кликаем по кнопке 'В корзину' на первой карточке курса (с hover)")
    def click_add_to_basket_first_course(self):
        self.hover(CoursesLocators.COURSE_CARD)
        btn = self.wait_clickable(CoursesLocators.COURSE_CARD_BASKET_BUTTON)
        btn.click()
