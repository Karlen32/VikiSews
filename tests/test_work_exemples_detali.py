import pytest
import allure
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data.work_example_data import WORK_EXAMPLE_DATA
from locators.work_examples_detail_locators import WorkExamplesDetailLocators
from locators.base_locators import BaseLocators
from locators.favorits_locators import FavoritesLocators


class TestWorkExamplesDetail:

    @pytest.mark.smoke
    @allure.title("Взаимодействие с примером работы")
    @allure.description("Проверка: избранное, лайк, шаринг, комментарии")
    def test_work_examples_detail(self, driver_logged):
        driver = driver_logged

        wait = WebDriverWait(driver, 15)

        # ---------- Открываем бургер ----------        
        wait.until(EC.element_to_be_clickable(BaseLocators.BURGER_BUTTON)).click()

        # ---------- Переход в Примеры работ ----------
        wait.until(EC.element_to_be_clickable(BaseLocators.BURGER_ITEM_WORK_EXAMPLES)).click()

        wait.until(EC.visibility_of_element_located(WorkExamplesDetailLocators.WORK_EXAMPLES_TITLE))

        # ---------- Берём вторую карточку ----------
        cards = wait.until(
            EC.presence_of_all_elements_located(WorkExamplesDetailLocators.WORK_EXAMPLES_CARD_LINK)
        )
        assert len(cards) >= 2, "Ожидается минимум 2 карточки"

        second_card = cards[3]

        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", second_card)
        wait.until(EC.element_to_be_clickable(second_card))
        second_card.click()

        wait.until(EC.url_contains("/work-examples/"))

        # ---------- Добавление в избранное ----------
        fav_btn = wait.until(
            EC.element_to_be_clickable(WorkExamplesDetailLocators.USER_ACTIVITY_FAVORITE_BUTTON)
        )

        fav_count_el = wait.until(
            EC.visibility_of_element_located(WorkExamplesDetailLocators.USER_ACTIVITY_FAVORITE_COUNT)
        )

        fav_before = int(fav_count_el.text.strip() or 0)

        driver.execute_script("arguments[0].click();", fav_btn)

        wait.until(
            lambda d: int(d.find_element(
                *WorkExamplesDetailLocators.USER_ACTIVITY_FAVORITE_COUNT
            ).text.strip() or 0) == fav_before + 1
        )

        # ---------- Переход к комментариям ----------
        wait.until(
            EC.element_to_be_clickable(WorkExamplesDetailLocators.USER_ACTIVITY_COMMENTS_BUTTON)
        ).click()

        # ---------- Лайк ----------
        like_btn = wait.until(EC.presence_of_element_located(WorkExamplesDetailLocators.LIKE_BUTTON))

        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", like_btn)
        time.sleep(0.3)

        wait.until(
            EC.element_to_be_clickable(WorkExamplesDetailLocators.LIKE_BUTTON)
        )

        # Лайк иногда перекрывается SVG → делаем JS-клик
        driver.execute_script("arguments[0].click();", like_btn)

        time.sleep(0.6)  # ждём анимацию лайка

        # ---------- Шаринг ----------
        share_btn = wait.until(
            EC.element_to_be_clickable(WorkExamplesDetailLocators.SHARE_BUTTON)
        )

        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", share_btn)
        time.sleep(0.2)

        driver.execute_script("arguments[0].click();", share_btn)

        wait.until(EC.visibility_of_element_located(WorkExamplesDetailLocators.SHARE_MODAL))

        close_btn = wait.until(
            EC.element_to_be_clickable(WorkExamplesDetailLocators.SHARE_MODAL_CLOSE_BUTTON)
        )
        driver.execute_script("arguments[0].click();", close_btn)

        # ---------- Комментарии ----------
        comment_input = wait.until(
            EC.element_to_be_clickable(WorkExamplesDetailLocators.COMMENTS_TEXTAREA_INPUT)
        )

        comment_input.send_keys(WORK_EXAMPLE_DATA["comment"])

        image_input = wait.until(
            EC.presence_of_element_located(WorkExamplesDetailLocators.COMMENTS_UPLOAD_IMAGE_INPUT)
        )

        image_input.send_keys(WORK_EXAMPLE_DATA["images_2"])

        wait.until(
            EC.element_to_be_clickable(WorkExamplesDetailLocators.COMMENTS_SEND_BUTTON)
        ).click()

        modal_text = wait.until(
            EC.visibility_of_element_located(WorkExamplesDetailLocators.COMMENT_SENT_MODAL_TEXT)
        )

        assert modal_text.text.strip() == "Комментарий отправлен на модерацию", \
            f"Ожидали сообщение об успехе, но получили: '{modal_text.text}'"

    @pytest.mark.smoke
    @allure.title("Проверка удаления примера работы из избранного")
    def test_work_examples_detail_from_favorites(self, driver_logged):
        driver = driver_logged
        wait = WebDriverWait(driver, 15)

        # ---------- Переход в избранное ----------
        wait.until(
            EC.element_to_be_clickable(FavoritesLocators.HEADER_FAVORITES_BUTTON)
        ).click()

        wait.until(
            EC.visibility_of_element_located(FavoritesLocators.FAVORITES_PAGE_TITLE)
        )

        # ---------- Берём список кнопок удаления ----------
        remove_buttons = wait.until(
            EC.presence_of_all_elements_located(FavoritesLocators.FAVORITE_REMOVE_BUTTON)
        )

        assert len(remove_buttons) > 0, "Нет карточек для удаления"

        # ---------- Удаляем первую карточку ----------
        first_remove_btn = remove_buttons[0]
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'})", first_remove_btn)
        driver.execute_script("arguments[0].click();", first_remove_btn)

        # ---------- Проверяем, что кнопка исчезла ----------
        wait.until_not(
            EC.presence_of_element_located(FavoritesLocators.FAVORITE_REMOVE_BUTTON)
        )


        

    


        







