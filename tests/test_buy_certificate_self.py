import pytest
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.lk_bonus_certificates_buy_locators import LKBonusCertificatesBuyLocators
from locators.lk_locators import LKLocators
from selenium.webdriver.common.by import By
from locators.vykrojki_locators import VykrojkiLocators
from data.title_text import AllTexts
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time


class TestBuyCertificateSelf:
    @pytest.mark.smoke
    @allure.title("Покупка сертификата для себя")
    @allure.description("Проверка покупки сертификата для себя: просмотр условий программы, выбор цвета, ввод суммы, переход к оплате")
    def test_buy_certificate_self(self, driver_logged):
        driver = driver_logged

        # ---------- 🔐 Открываем меню ЛК ----------
        lk_icon = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(LKLocators.LK_ICON_BUTTON)
        )
        ActionChains(driver).move_to_element(lk_icon).perform()

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(LKLocators.MENU_BONUSES_CERTIFICATES)
        ).click()

        # ---------- 📄 Открываем условия программы ----------
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(LKBonusCertificatesBuyLocators.PROGRAM_CONDITIONS_BUTTON)
        ).click()

        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(LKBonusCertificatesBuyLocators.PROGRAM_CONDITIONS_TITLE)
        ).text == AllTexts.PROGRAM_BONUSES_TITLE

        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(LKBonusCertificatesBuyLocators.PROGRAM_CONDITIONS_TEXT)
        ).text == AllTexts.PROGRAM_BONUSES_TEXT

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(LKBonusCertificatesBuyLocators.PROGRAM_CONDITIONS_CLOSE_BUTTON)
        ).click()

        # ---------- 🎁 Нажимаем «Купить сертификат» ----------
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(LKBonusCertificatesBuyLocators.BUY_CERTIFICATE_BUTTON)
        ).click()

        # ---------- 🎨 Выбор цвета ----------
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(LKBonusCertificatesBuyLocators.CERTIFICATE_COLOR_1_GREEN)
        ).click()

        # ---------- 💵 Ввод суммы вручную ----------
        price_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(LKBonusCertificatesBuyLocators.CERTIFICATE_PRICE_INPUT)
        )

        # Скроллим так, чтобы 100% было видно
        driver.execute_script(
            "arguments[0].scrollIntoView({block: 'nearest'});", price_input
        )
        driver.execute_script(
            "window.scrollTo(0, arguments[0].getBoundingClientRect().top + window.scrollY - 150);",
            price_input
        )

        ActionChains(driver).move_to_element(price_input).perform()

        # Ввод как у человека
        price_input.click()
        price_input.send_keys(Keys.CONTROL, "a")
        price_input.send_keys(Keys.DELETE)

        for ch in "1000":
            price_input.send_keys(ch)
            time.sleep(0.12)

        price_input.send_keys(Keys.ENTER)

        # ---------- 🎚 Двигаем ползунок (обновить UI) ----------
        slider_handle = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#m-slider .noUi-handle-lower"))
        )

        actions = ActionChains(driver)
        actions.click_and_hold(slider_handle).move_by_offset(10, 0).release().perform()
        time.sleep(0.3)

        # ---------- ⏭ Переход к оплате ----------
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(LKBonusCertificatesBuyLocators.NEXT_BUTTON)
        ).click()

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(LKBonusCertificatesBuyLocators.PAY_BUTTON)
        ).click()

        # ---------- 💰 Проверка цены на странице оплаты ----------
        iframe = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.TAG_NAME, "iframe"))
        )

        driver.switch_to.frame(iframe)

        assert WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located(VykrojkiLocators.PAYMENT_PAGE_HEADER)
        ).text == AllTexts.PAYMENT_PAGE_HEADER


