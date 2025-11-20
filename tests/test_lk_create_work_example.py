import pytest
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.lk_locators import LKLocators
from locators.lk_examples_locators import LKExamplesLocators
from data.work_example_data import WORK_EXAMPLE_DATA
from selenium.webdriver.common.action_chains import ActionChains


class TestLKCreateWorkExample:

    @pytest.mark.smoke
    @allure.title("Создание примера работы в личном кабинете")
    @allure.description("Проверка создания примера работы: заполнение названия, описания, загрузка изображений, выбор продукта, публикация")
    def test_lk_create_work_example(self, driver_logged):
        driver = driver_logged

        # ---------- 🔐 Открываем меню ЛК ----------
        lk_icon = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(LKLocators.LK_ICON_BUTTON)
        )
        ActionChains(driver).move_to_element(lk_icon).perform()

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(LKLocators.MENU_EXAMPLES)
        ).click()

        # ---------- Кликаем "Добавить работу" ----------
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(LKExamplesLocators.ADD_WORK_BUTTON)
        ).click()

        # ---------- Название ----------
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(LKExamplesLocators.WORK_NAME_INPUT)
        ).send_keys(WORK_EXAMPLE_DATA["work_name"])

        # ---------- Описание ----------
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(LKExamplesLocators.WORK_DESCRIPTION_INPUT)
        ).send_keys(WORK_EXAMPLE_DATA["description"])

        # ---------- Загрузка обложки ----------
        cover_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(LKExamplesLocators.COVER_UPLOAD_IMAGE_INPUT)
        )
        cover_input.send_keys(WORK_EXAMPLE_DATA["images"])

        # ---------- Загрузка галереи ----------
        gallery_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(LKExamplesLocators.WORK_IMAGES_UPLOAD_INPUT)
        )
        gallery_input.send_keys(WORK_EXAMPLE_DATA["images_2"])
        gallery_input.send_keys(WORK_EXAMPLE_DATA["images_3"])
        gallery_input.send_keys(WORK_EXAMPLE_DATA["images_4"])

        # ---------- Открываем селект продуктов ----------
        dropdown = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(LKExamplesLocators.PRODUCT_SELECT_DROPDOWN_BUTTON)
        )
        # ---------- скролл ----------
        driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center', behavior: 'instant'});",
            dropdown
        )

        # Поднимаем чуть выше, чтобы не перекрывалось шапкой
        driver.execute_script("window.scrollBy(0, -250);")

        # ------ Кликаем ------
        dropdown.click()

        # ---------- Выбираем продукт ----------
        product_item = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                LKExamplesLocators.product_option_by_text(WORK_EXAMPLE_DATA["product_name"])
            )
        )
        product_item.click()

        # ---------- Фамилия ----------
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(LKExamplesLocators.WORK_AUTHOR_LASTNAME_INPUT)
        ).send_keys(WORK_EXAMPLE_DATA["lastname"])

        # ---------- Имя ----------
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(LKExamplesLocators.WORK_AUTHOR_NAME_INPUT)
        ).send_keys(WORK_EXAMPLE_DATA["name"])

        # ---------- Публикуем ----------
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(LKExamplesLocators.WORK_PUBLISH_BUTTON)
        ).click()

        # ---------- Проверка ----------
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(LKExamplesLocators.SUCCESS_MODAL_CLOSE_BUTTON)
        ).click()


        

