import pytest
import allure
from pages.lk_certificates_page import LKCertificatesPage
from data.title_text import AllTexts


class TestBuyCertificateSelf:

    @pytest.mark.smoke
    @allure.title("Покупка сертификата для себя")
    @allure.description("Проверка покупки сертификата для себя: условия программы, выбор цвета, ввод суммы, оплата")
    def test_buy_certificate_self(self, driver_logged):

        page = LKCertificatesPage(driver_logged)

        with allure.step("Открываем раздел Бонусы и сертификаты"):
            page.open_certificates_section()

        with allure.step("Проверяем условия программы"):
            page.open_program_conditions()
            assert page.get_program_conditions_title() == AllTexts.PROGRAM_BONUSES_TITLE
            assert page.get_program_conditions_text() == AllTexts.PROGRAM_BONUSES_TEXT
            page.close_program_conditions()

        with allure.step("Открываем покупку сертификата"):
            page.start_buy_certificate()

        with allure.step("Выбираем цвет"):
            page.select_color()

        with allure.step("Вводим сумму"):
            page.enter_price(1000)
            page.move_slider()

        with allure.step("Переходим к оплате"):
            page.proceed_to_pay()

        with allure.step("Проверяем iframe оплаты"):
            header = page.wait_payment_iframe()
            assert header.text == AllTexts.PAYMENT_PAGE_HEADER



