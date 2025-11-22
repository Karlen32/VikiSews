from pages.base_page import BasePage
from locators.login_logout_locators import LoginLogoutLocators


class LoginPage(BasePage):

    def open_login(self):
        self.click(LoginLogoutLocators.PROFILE_ICON)

    def enter_email(self, email):
        self.send_keys(LoginLogoutLocators.EMAIL_INPUT, email)

    def enter_password(self, password):
        self.send_keys(LoginLogoutLocators.PASSWORD_INPUT, password)

    def submit(self):
        self.click(LoginLogoutLocators.LOGIN_BUTTON)
