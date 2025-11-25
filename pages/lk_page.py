import allure
from pages.base_page import BasePage
from locators.lk_locators import LKLocators
from locators.lk_personal_data_locators import LKPersonalDataLocators
from locators.lk_personal_locators import LKPersonalLocators


class LKPage(BasePage):

    # ==========================
    #      БАЗОВАЯ НАВИГАЦИЯ
    # ==========================
    @allure.step("Открываем меню личного кабинета")
    def open_menu(self):
        self.hover(LKLocators.LK_ICON_BUTTON)

    @allure.step("клик по иконке входа")
    def click_login_icon(self):
        self.click(LKLocators.LK_ICON_BUTTON)

    @allure.step("Переходим в профиль")
    def go_to_profile(self):
        self.click(LKLocators.MENU_PROFILE)

    # ==========================
    #     ПЕРСОНАЛЬНЫЕ ДАННЫЕ
    # ==========================
    @allure.step("Вводим имя: {1}")
    def set_first_name(self, value):
        self.send_keys(LKPersonalDataLocators.INPUT_FIRST_NAME, value)

    @allure.step("Вводим фамилию: {1}")
    def set_last_name(self, value):
        self.send_keys(LKPersonalDataLocators.INPUT_LAST_NAME, value)

    @allure.step("Вводим обхват груди: {1}")
    def set_chest(self, value):
        self.send_keys(LKPersonalDataLocators.INPUT_CHEST_GIRTH, value)

    @allure.step("Вводим обхват талии: {1}")
    def set_waist(self, value):
        self.send_keys(LKPersonalDataLocators.INPUT_WAIST_GIRTH, value)

    @allure.step("Вводим обхват бёдер: {1}")
    def set_hips(self, value):
        self.send_keys(LKPersonalDataLocators.INPUT_HIPS_GIRTH, value)

    @allure.step("Вводим рост: {1}")
    def set_height(self, value):
        self.send_keys(LKPersonalDataLocators.INPUT_HEIGHT, value)

    @allure.step("Сохраняем персональные данные")
    def save_personal_data(self):
        save_btn = self.wait_visible(LKPersonalDataLocators.SAVE_CHANGES_BUTTON)
        self.driver.execute_script( "arguments[0].scrollIntoView({block: 'center', behavior: 'instant'});", save_btn )
        save_btn.click()

    # ==========================
    #       СМЕНА ПАРОЛЯ
    # ==========================
    @allure.step("Открываем раздел изменения пароля")
    def open_change_password_modal(self):
        self.click(LKPersonalLocators.CHANGE_PASSWORD_BUTTON)

    @allure.step("Вводим новый пароль")
    def set_new_password(self, value):
        self.send_keys(LKPersonalLocators.INPUT_NEW_PASSWORD, value)

    @allure.step("Повторяем новый пароль")
    def set_repeat_password(self, value):
        self.send_keys(LKPersonalLocators.INPUT_REPEAT_PASSWORD, value)

    @allure.step("Сохраняем новый пароль")
    def save_new_password(self):
        self.click(LKPersonalLocators.SAVE_PASSWORD_BUTTON)

    # ==========================
    #         СООБЩЕНИЯ
    # ==========================
    @allure.step("Ожидаем появление сообщения: {1}")
    def wait_success_message(self, text):
        locator = LKLocators.get_message_locator(text)
        return self.wait_visible(locator)



