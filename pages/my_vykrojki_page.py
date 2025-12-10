import time
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from locators.my_vykrojki_locators import MyVykrojkiLocators
from locators.lk_locators import LKLocators
from pages.base_page import BasePage


class MyVykrojkiPage(BasePage):

    # ---------------------- Навигация ----------------------

    @allure.step("Открываем раздел Мои выкройки")
    def open_my_vykrojki_section(self):
        lk_icon = self.wait_visible(LKLocators.LK_ICON_BUTTON)
        ActionChains(self.driver).move_to_element(lk_icon).perform()
        self.click(LKLocators.MENU_MY_PATTERNS)

    @allure.step("Открываем список категорий")
    def open_sort_dropdown(self):
        open_btn = self.wait_visible(MyVykrojkiLocators.PATTERN_SORT_OPEN_BUTTON)
        open_btn.click()
        time.sleep(0.2)

    @allure.step("Выбираем категорию 'Новая коллекция'")
    def select_category_new_collection(self):
        radio_btn = self.wait_clickable(MyVykrojkiLocators.RADIO_NEW_COLLECTION)
        radio_btn.click()
        time.sleep(0.2)

    @allure.step("Выбираем категорию 'Платья и сарафаны'")
    def select_category_dresses(self):
        radio_btn = self.wait_clickable(MyVykrojkiLocators.RADIO_DRESSES)
        radio_btn.click()
        time.sleep(0.2)

    @allure.step("Выбираем категорию 'Худи, футболки, лонгсливы'")
    def select_category_hoodies_tshirts_longsleeves(self):
        radio_btn = self.wait_clickable(MyVykrojkiLocators.RADIO_HOODIES_TSHIRTS_LONGSLEEVES)
        radio_btn.click()
        time.sleep(0.2)

    @allure.step("Получаем список карточек")
    def get_cards(self):
        return self.driver.find_elements(*MyVykrojkiLocators.CARDS_LIST)

    @allure.step("Ожидаем обновления списка карточек")
    def wait_cards_updated(self, timeout: int = 10):
        old_cards = self.driver.find_elements(*MyVykrojkiLocators.CARDS_LIST)

        WebDriverWait(self.driver, timeout).until(
            lambda d: self.__cards_changed(old_cards)
        )
        return True

    @allure.step("Проверяем, что список карточек обновился")
    def __cards_changed(self, old_cards):
        # 1. Если какие-то карточки стали "старые" (обновился DOM)
        try:
            for card in old_cards:
                if EC.staleness_of(card)(self.driver):
                    return True
        except Exception:
            return True

        # 2. Проверяем изменение количества карточек
        new_cards = self.driver.find_elements(*MyVykrojkiLocators.CARDS_LIST)
        if len(new_cards) != len(old_cards):
            return True

        return False


    # ---------------------- Статусы ----------------------
    @allure.step("Меняем статус карточек на '{1}'")
    def change_status(self, status_text):
        btn = self.wait_clickable(MyVykrojkiLocators.BUTTON_STATUS(status_text))
        btn.click()
        self.wait_cards_updated()


    @allure.step("Проверяем, что у всех карточек статус '{1}'")
    def assert_all_cards_have_status(self, status_text):
        cards = self.get_cards()
        assert len(cards) > 0, "Карточки отсутствуют"

        for index, card in enumerate(cards, start=1):
            # Находим текст статуса в карточке
            try:
                status_element = card.find_element(
                    By.CSS_SELECTOR,
                    "span.status span.js-select-value"
                )
                actual_status = status_element.text.strip()
            except Exception:
                raise AssertionError(f"Карточка #{index}: статус не найден вообще!")

            # Добавляем в отчёт Allure
            allure.attach(
                actual_status,
                f"Статус карточки #{index}",
                allure.attachment_type.TEXT
            )

            # Проверяем совпадение
            if actual_status.lower() != status_text.lower():
                raise AssertionError(
                    f"Карточка #{index}: ожидали статус '{status_text}', "
                    f"но получили '{actual_status}'"
                )

    # ---------------------- Поиск ----------------------
    @allure.step("Ищем по запросу: {1}")
    def search(self, text: str):
        # Открываем строку поиска
        btn = self.wait_clickable(MyVykrojkiLocators.SEARCH_OPEN_BUTTON)
        btn.click()

        # Вводим текст
        input_el = self.wait_visible(MyVykrojkiLocators.SEARCH_INPUT)
        input_el.clear()
        input_el.send_keys(text)

        # Нажимаем кнопку поиска
        submit = self.wait_clickable(MyVykrojkiLocators.SEARCH_SUBMIT_BUTTON)
        submit.click()

        # Ждём обновления карточек
        self.wait_cards_updated()

    # ---------------------- Получение списка названий ----------------------

    @allure.step("Получаем список названий карточек")
    def get_card_names(self):
        cards = self.get_cards()
        names = []
        for card in cards:
            name_el = card.find_element(*MyVykrojkiLocators.CARD_NAME)
            names.append(name_el.text.strip())
        return names


    # ---------------------- Проверка наличия выкройки ----------------------
    @allure.step("Проверяем, что найдена выкройка '{1}'")
    def assert_found_pattern_exact(self, pattern_name: str):
        names = [name.lower().strip() for name in self.get_card_names()]
        target = pattern_name.lower().strip()

        if target not in names:
            raise AssertionError(
                f"Выкройка '{pattern_name}' не найдена. "
                f"Существующие: {names}"
            )






        



                


