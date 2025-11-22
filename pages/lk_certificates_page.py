import time
import allure
from selenium.webdriver import ActionChains, Keys
from pages.base_page import BasePage
from locators.lk_bonus_certificates_buy_locators import LKBonusCertificatesBuyLocators
from locators.vykrojki_locators import VykrojkiLocators
from locators.lk_locators import LKLocators
from selenium.webdriver.common.by import By


class LKCertificatesPage(BasePage):

    # ==========================
    #      НАВИГАЦИЯ
    # ==========================
    @allure.step("Открываем раздел Бонусы и сертификаты в ЛК")
    def open_certificates_section(self):
        lk_icon = self.wait_visible(LKLocators.LK_ICON_BUTTON)
        ActionChains(self.driver).move_to_element(lk_icon).perform()

        self.click(LKLocators.MENU_BONUSES_CERTIFICATES)

    # ==========================
    #       УСЛОВИЯ ПРОГРАММЫ
    # ==========================
    @allure.step("Открываем условия бонусной программы")
    def open_program_conditions(self):
        self.click(LKBonusCertificatesBuyLocators.PROGRAM_CONDITIONS_BUTTON)

    @allure.step("Получаем заголовок условий программы")
    def get_program_conditions_title(self):
        return self.wait_visible(LKBonusCertificatesBuyLocators.PROGRAM_CONDITIONS_TITLE).text

    @allure.step("Получаем текст условий программы")
    def get_program_conditions_text(self):
        return self.wait_visible(LKBonusCertificatesBuyLocators.PROGRAM_CONDITIONS_TEXT).text

    @allure.step("Закрываем модалку условий программы")
    def close_program_conditions(self):
        self.click(LKBonusCertificatesBuyLocators.PROGRAM_CONDITIONS_CLOSE_BUTTON)

    # ==========================
    #     ПОКУПКА СЕРТИФИКАТА
    # ==========================
    @allure.step("Переходим к покупке сертификата")
    def start_buy_certificate(self):
        self.click(LKBonusCertificatesBuyLocators.BUY_CERTIFICATE_BUTTON)

    @allure.step("Выбираем цвет сертификата")
    def select_color(self):
        self.click(LKBonusCertificatesBuyLocators.CERTIFICATE_COLOR_1_GREEN)

    @allure.step("Вводим сумму сертификата {1}")
    def enter_price(self, price):
        price_input = self.wait_visible(LKBonusCertificatesBuyLocators.CERTIFICATE_PRICE_INPUT)

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});", price_input
        )
        time.sleep(0.2)

        ActionChains(self.driver).move_to_element(price_input).perform()

        price_input.click()
        price_input.send_keys(Keys.CONTROL, "a")
        price_input.send_keys(Keys.DELETE)

        for ch in str(price):
            price_input.send_keys(ch)
            time.sleep(0.12)

        price_input.send_keys(Keys.ENTER)

    @allure.step("Сдвигаем слайдер суммы")
    def move_slider(self):
        slider_handle = self.wait_clickable((By.CSS_SELECTOR, "#m-slider .noUi-handle-lower"))
        actions = ActionChains(self.driver)
        actions.click_and_hold(slider_handle).move_by_offset(10, 0).release().perform()
        time.sleep(0.3)

    @allure.step("Переходим к оплате")
    def proceed_to_pay(self):
        self.click(LKBonusCertificatesBuyLocators.NEXT_BUTTON)
        self.click(LKBonusCertificatesBuyLocators.PAY_BUTTON)

    @allure.step("Ждём iframe оплаты")
    def wait_payment_iframe(self):
        iframe = self.wait_visible((By.TAG_NAME, "iframe"))
        self.driver.switch_to.frame(iframe)
        return self.wait_visible(VykrojkiLocators.PAYMENT_PAGE_HEADER)

        # ==========================
    #     СЕРТИФИКАТ ДЛЯ ДРУГА
    # ==========================
    @allure.step("Выбираем вкладку 'Для друга'")
    def select_tab_for_friend(self):
        self.click(LKBonusCertificatesBuyLocators.CERTIFICATE_TAB_FOR_FRIEND)

    @allure.step("Вводим кому предназначен сертификат: {1}")
    def enter_to_whom(self, text):
        self.send_keys(LKBonusCertificatesBuyLocators.FIELD_TO_WHOM, text)

    @allure.step("Вводим от кого: {1}")
    def enter_from_who(self, text):
        self.send_keys(LKBonusCertificatesBuyLocators.FIELD_FROM_WHO, text)

    @allure.step("Вводим поздравительный текст")
    def enter_congrats(self, text):
        self.send_keys(LKBonusCertificatesBuyLocators.FIELD_CONGRATS_TEXTAREA, text)

    @allure.step("Выбираем отправку через телефон")
    def select_phone_tab(self):
        self.click(LKBonusCertificatesBuyLocators.TAB_SEND_PHONE)

    @allure.step("Вводим телефон с маской")
    def enter_phone(self, phone):
        # клик по wrapper
        wrap = self.wait_clickable((By.XPATH, "//span[contains(text(),'Телефон')]/.."))
        wrap.click()

        phone_input = self.wait_visible(LKBonusCertificatesBuyLocators.FIELD_PHONE)

        for ch in phone:
            phone_input.send_keys(ch)
            time.sleep(0.08)

        phone_input.send_keys(Keys.TAB)
