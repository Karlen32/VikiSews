import allure
from pages.base_page import BasePage
from locators.wheel_of_fortune_locators import WheelLocators


class WheelPage(BasePage):

    @allure.step("Открываем модалку 'Колесо фортуны'")
    def open_wheel(self):
        self.click(WheelLocators.OPEN_WHEEL_BUTTON)
        # Ждём, пока модалка откроется и кнопка спина станет видимой
        self.wait_visible(WheelLocators.SPIN_BUTTON)

    @allure.step("Получаем текущее количество попыток")
    def get_attempts_count(self) -> int:
        text = self.wait_visible(WheelLocators.SPIN_COUNTER).text.strip()
        return int(text)

    @allure.step("Крутим колесо")
    def spin(self):
        self.click(WheelLocators.SPIN_BUTTON)
        # Ждём, пока анимация завершится и счетчик обновится
        # Ожидаем, что элемент счетчика станет видимым (или обновится)
        self.wait_visible(WheelLocators.SPIN_COUNTER)

    @allure.step("Закрываем модалку подарка кнопкой 'вернуться к колесу'")
    def close_gift_button(self):
        self.click(WheelLocators.GIFT_CLOSE_BUTTON)

    @allure.step("Закрываем модалку подарка через иконку 'X'")
    def close_gift_icon(self):
        self.click(WheelLocators.GIFT_CLOSE_ICON_BUTTON)

    @allure.step("Переходим к покупкам из модалки")
    def go_to_purchases(self):
        self.click(WheelLocators.GO_TO_PURCHASES_LINK)
