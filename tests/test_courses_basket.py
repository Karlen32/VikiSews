from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.base_locators import BaseLocators
from locators.courses_locators import CoursesLocators
from utils.test_helpers import DEFAULT_TIMEOUT
from selenium.webdriver import ActionChains

import pytest
import allure
import time


class TestCoursesBasket:
    @pytest.mark.smoke
    @allure.title("Проверка добавления курса в корзину")
    @allure.description("Проверка редиректа при добавлении курса в корзину")
    def test_add_course_to_basket(self, driver_logged):
        driver = driver_logged

        # 1. Открываем бургер и курсы
        WebDriverWait(driver, DEFAULT_TIMEOUT).until(
            EC.element_to_be_clickable(BaseLocators.BURGER_BUTTON)
        ).click()

        WebDriverWait(driver, DEFAULT_TIMEOUT).until(
            EC.element_to_be_clickable(BaseLocators.BURGER_ITEM_COURSES)
        ).click()

        WebDriverWait(driver, DEFAULT_TIMEOUT).until(
            EC.visibility_of_element_located(CoursesLocators.COURSES_TITLE)
        )

        # 2. Берём первую карточку
        course_card = WebDriverWait(driver, DEFAULT_TIMEOUT).until(
            EC.presence_of_element_located(CoursesLocators.COURSE_CARD)
        )

        driver.execute_script("arguments[0].scrollIntoView({block:'center'});", course_card)

        # 3. Ховер
        time.sleep(1)
        ActionChains(driver).move_to_element(course_card).pause(0.4).perform()

        driver.execute_script("""
            arguments[0].dispatchEvent(new MouseEvent('mouseover', {bubbles:true}));
            arguments[0].dispatchEvent(new MouseEvent('mouseenter', {bubbles:true}));
        """, course_card)

        # 4. Кликаем «В корзину»
        basket_button = WebDriverWait(driver, DEFAULT_TIMEOUT).until(
            EC.element_to_be_clickable(CoursesLocators.COURSE_CARD_BASKET_BUTTON)
        )
        basket_button.click()

        # 5. Проверяем, что произошёл редирект
        WebDriverWait(driver, DEFAULT_TIMEOUT).until(
            EC.url_contains("https://vikisews.online/mini-kurs-po")
        )

        assert "https://vikisews.online/mini-kurs-po" in driver.current_url.lower(), \
            f"❌ Редирект не произошёл! Сейчас URL: {driver.current_url}"



        