import pytest
import allure
from pages.wheel_page import WheelPage


class TestWheelOfFortune:

    @pytest.mark.smoke
    @allure.title("Крутка колеса фортуны уменьшает счетчик попыток")
    def test_spin_decreases_attempts(self, driver_logged):
        page = WheelPage(driver_logged)

        with allure.step("Открываем колесо и смотрим счётчик"):
            page.open_wheel()
            before = page.get_attempts_count()

        with allure.step("Крутим колесо"):
            page.spin()
            after = page.get_attempts_count()

        assert after == before - 1, f"Ожидали {before-1} попыток, а получили {after}"
