from locators.wheel_of_fortune_locators import WheelLocators
from pages.wheel_page import WheelPage
from pages.lk_page import LKPage
import pytest
import allure


class TestWheelOfFortune:

    @pytest.mark.smoke
    @allure.title("Крутка колеса фортуны уменьшает счетчик попыток")
    def test_spin_decreases_attempts(self, driver_logged):
        page = WheelPage(driver_logged)
        lk = LKPage(driver_logged)

        with allure.step("Открываем меню личного кабинета"):
            lk.open_menu()
        with allure.step("Переходим в профиль"):
            lk.go_to_profile()

        with allure.step("Открываем колесо и смотрим счётчик"):
            page.open_wheel()
            before = page.get_attempts_count()

        with allure.step("Крутим колесо"):
            page.spin()
            after = page.get_attempts_count()

        assert after == before - 1, f"Ожидали {before-1} попыток, а получили {after}"


    @pytest.mark.smoke
    @allure.title("Крутка колеса фортуны открывает модалку с поздравлением")
    def test_spin_opens_congratulation_modal(self, driver_logged):
        page = WheelPage(driver_logged)
        lk = LKPage(driver_logged)

        with allure.step("Открываем меню личного кабинета"):
            lk.open_menu()
        with allure.step("Переходим в профиль"):
            lk.go_to_profile()

        with allure.step("Открываем колесо и смотрим счётчик"):
            page.open_wheel()

        with allure.step("Крутим колесо"):
            page.spin()

        with allure.step("Закрываем модалку подарка кнопкой 'вернуться к колесу'"):
            page.close_gift_button()

        with allure.step("Проверяем, что открылась модалка с поздравлением"):
            assert page.is_congratulation_modal_visible(), "Модалка с поздравлением не открылась"

        with allure.step("Закрываем модалку подарка через иконку 'X'"):
            page.close_gift_icon()

        with allure.step("Проверяем, что снова видна кнопка 'Крутить колесо'"):
            assert page.wait_visible(WheelLocators.OPEN_WHEEL_BUTTON) is not None, \
                "Кнопка 'Крутить колесо' не появилась после закрытия модалки"
           

        
            

        
