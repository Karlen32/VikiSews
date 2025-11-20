from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.base_locators import BaseLocators
from locators.courses_locators import CoursesLocators
from utils.test_helpers import DEFAULT_TIMEOUT
from selenium.webdriver import ActionChains
from locators.favorits_locators import FavoritesLocators

import pytest
import allure
import time


class TestCoursesFavorites:
    @pytest.mark.smoke
    @allure.title("Проверка добавления курса в избранное")
    @allure.description("Проверка добавления курса в избранное через модальное окно")
    def test_add_course_to_favorites(self, driver_logged):
        driver = driver_logged


        WebDriverWait(driver, DEFAULT_TIMEOUT).until(
            EC.element_to_be_clickable(BaseLocators.BURGER_BUTTON)
        ).click()

        WebDriverWait(driver, DEFAULT_TIMEOUT).until(
            EC.element_to_be_clickable(BaseLocators.BURGER_ITEM_COURSES)
        ).click()

        WebDriverWait(driver, DEFAULT_TIMEOUT).until(
            EC.visibility_of_element_located(CoursesLocators.COURSES_TITLE)
        )

        course_card = WebDriverWait(driver, DEFAULT_TIMEOUT).until(
            EC.presence_of_element_located(CoursesLocators.COURSE_CARD)
        )

        # Скроллим к карточке
        driver.execute_script("arguments[0].scrollIntoView({block:'center'});", course_card)

        # ---------- 3. Ховер ----------
        time.sleep(2)
        ActionChains(driver).move_to_element(course_card).pause(0.4).perform()

        driver.execute_script("""
            arguments[0].dispatchEvent(new MouseEvent('mouseover', {bubbles:true}));
            arguments[0].dispatchEvent(new MouseEvent('mouseenter', {bubbles:true}));
        """, course_card)


        favorite_button = WebDriverWait(driver, DEFAULT_TIMEOUT).until(
            EC.element_to_be_clickable(CoursesLocators.COURSE_CARD_FAVORITE_BUTTON))


        favorite_button.click()

        classes = favorite_button.get_attribute("class")
        assert any(c in classes for c in ["active", "added"]), "❌ Курс не добавлен в избранное"



    @pytest.mark.smoke
    @allure.title("Проверка удаления курса из избранного")
    @allure.description("Проверка удаления курса из избранного")
    def test_delete_course_from_favorites(self, driver_logged):
        driver = driver_logged


        WebDriverWait(driver, DEFAULT_TIMEOUT).until(
            EC.element_to_be_clickable(FavoritesLocators.HEADER_FAVORITES_BUTTON)
        ).click()

        WebDriverWait(driver, DEFAULT_TIMEOUT).until(
            EC.visibility_of_element_located(FavoritesLocators.FAVORITES_PAGE_TITLE))

        delete_btn = WebDriverWait(driver, DEFAULT_TIMEOUT).until(
            EC.element_to_be_clickable(FavoritesLocators.FAVORITE_REMOVE_BUTTON))


        delete_btn.click()

        WebDriverWait(driver, DEFAULT_TIMEOUT).until_not(
            EC.presence_of_element_located(FavoritesLocators.FAVORITE_REMOVE_BUTTON))