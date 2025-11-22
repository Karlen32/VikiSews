import pytest
import allure
from pages.lk_certificates_page import LKCertificatesPage
from data.title_text import AllTexts
from data.certificate_data import CERTIFICATE_FRIEND_DATA


class TestBuyCertificateFriend:

    @pytest.mark.smoke
    @allure.title("Покупка сертификата для друга")
    @allure.description("Проверка покупки сертификата: условия, цвет, сумма, 'для друга', телефон, оплата")
    def test_buy_certificate_friend(self, driver_logged):

        page = LKCertificatesPage(driver_logged)

        with allure.step("Открываем раздел Бонусы и сертификаты"):
            page.open_certificates_section()

        with allure.step("Проверяем условия программы"):
            page.open_program_conditions()
            assert page.get_program_conditions_title() == AllTexts.PROGRAM_BONUSES_TITLE
            assert page.get_program_conditions_text() == AllTexts.PROGRAM_BONUSES_TEXT
            page.close_program_conditions()

        with allure.step("Начинаем оформление сертификата"):
            page.start_buy_certificate()
            page.select_color()

        with allure.step("Вводим сумму сертификата"):
            page.enter_price(CERTIFICATE_FRIEND_DATA["amount"])
            page.move_slider()

        with allure.step("Заполняем данные для друга"):
            page.select_tab_for_friend()
            page.enter_to_whom(CERTIFICATE_FRIEND_DATA["to_whom"])
            page.enter_from_who(CERTIFICATE_FRIEND_DATA["from_who"])
            page.enter_congrats(CERTIFICATE_FRIEND_DATA["congrats_text"])

        with allure.step("Заполняем номер телефона"):
            page.select_phone_tab()
            page.enter_phone(CERTIFICATE_FRIEND_DATA["phone"])

        with allure.step("Переходим к оплате"):
            page.proceed_to_pay()

        with allure.step("Проверяем iframe оплаты"):
            frame_header = page.wait_payment_iframe()
            assert frame_header.text == AllTexts.PAYMENT_PAGE_HEADER

        


        