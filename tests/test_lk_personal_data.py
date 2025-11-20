import pytest
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.lk_personal_data_locators import LKPersonalDataLocators
from locators.lk_locators import LKLocators
from data.personal_info_data import PERSONAL_INFO_DATA
from selenium.webdriver.common.action_chains import ActionChains


class TestLKPersonalData:

    @pytest.mark.smoke
    @allure.title("Изменение персональных данных в личном кабинете")
    @allure.description("Проверка изменения персональных данных: ввод имени, фамилии, параметров тела, сохранение изменений")
    def test_lk_personal_data(self, driver_logged):
        driver = driver_logged


        lk_icon = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(LKLocators.LK_ICON_BUTTON)
        )
        ActionChains(driver).move_to_element(lk_icon).perform()

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(LKLocators.MENU_PROFILE)
        ).click()
        
        first_name_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(LKPersonalDataLocators.INPUT_FIRST_NAME)
        )
        first_name_input.clear()
        first_name_input.send_keys(PERSONAL_INFO_DATA["first_name"])

        last_name_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(LKPersonalDataLocators.INPUT_LAST_NAME)
        )
        last_name_input.clear()
        last_name_input.send_keys(PERSONAL_INFO_DATA["last_name"])

        chest_girth_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(LKPersonalDataLocators.INPUT_CHEST_GIRTH)
        )
        chest_girth_input.clear()
        chest_girth_input.send_keys(PERSONAL_INFO_DATA["boobs"])

        waist_girth_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(LKPersonalDataLocators.INPUT_WAIST_GIRTH)
        )
        waist_girth_input.clear()
        waist_girth_input.send_keys(PERSONAL_INFO_DATA["waist"])

        hips_girth_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(LKPersonalDataLocators.INPUT_HIPS_GIRTH)
        )
        hips_girth_input.clear()
        hips_girth_input.send_keys(PERSONAL_INFO_DATA["hips"])

        height_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(LKPersonalDataLocators.INPUT_HEIGHT)
        )
        height_input.clear()
        height_input.send_keys(PERSONAL_INFO_DATA["height"])

        # ---------- Кнопка сохранить ----------
        save_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(LKPersonalDataLocators.SAVE_CHANGES_BUTTON)
        )

        # ---------- Правильный, гарантированный скролл ----------
        driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center', behavior: 'instant'});",
            save_button
        )

        # Поднимаем чуть выше, чтобы не перекрывалось шапкой
        driver.execute_script("window.scrollBy(0, -150);")

        # ------ Кликаем ------
        save_button.click()

        SUCCESS_MESSAGE = LKLocators.get_message_locator("Данные успешно сохранены")

        message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(SUCCESS_MESSAGE)
        )

        assert "Данные успешно сохранены" in message.text

    