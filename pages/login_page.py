from pages.base_page import BasePage
from locators.login_logout_locators import LoginLogoutLocators
import allure


class LoginPage(BasePage):

    @allure.step("Открываем страницу входа")
    def open_login(self):
        self.click(LoginLogoutLocators.PROFILE_ICON)

    @allure.step("Вводим email: {1}")
    def enter_email(self, email):
        self.send_keys(LoginLogoutLocators.EMAIL_INPUT, email)

    @allure.step("Вводим пароль: {1}")
    def enter_password(self, password):
        self.send_keys(LoginLogoutLocators.PASSWORD_INPUT, password)

    @allure.step("Отправляем форму входа")
    def submit(self):
        self.click(LoginLogoutLocators.LOGIN_BUTTON)


    @allure.step("email пользователя видимый")
    def email_visible(self):
        return self.wait_visible(LoginLogoutLocators.USER_EMAIL)

    @allure.step("email пользователя не видимый")
    def email_not_visible(self):
        return self.wait_not_visible(LoginLogoutLocators.USER_EMAIL)

    @allure.step("кнопка выхода")
    def logout_button(self):
        return self.click(LoginLogoutLocators.LOGOUT_BUTTON)

    @allure.step("кнопка выхода в модальном окне")
    def logout_confirm_button(self):
        return self.click(LoginLogoutLocators.LOGOUT_CONFIRM_BUTTON)