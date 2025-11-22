import time
import allure
from selenium.webdriver import ActionChains
from pages.base_page import BasePage
from utils.product_config import ProductConfig
from locators.base_locators import BaseLocators
from locators.favorits_locators import FavoritesLocators


class ProductCatalogPage(BasePage):

    # ==========================
    #      Навигация в каталог
    # ==========================
    @allure.step("Переходим в каталог выкроек")
    def open_patterns_catalog(self):
        self.click(BaseLocators.PATTERNS_SUBMENU_LINK)
        self.click(BaseLocators.ALL_PATTERNS_LINK)
        self.wait.until(lambda d: "/vykrojki/vse-vykrojki/" in d.current_url)

    # ==========================
    #       Работа с карточкой
    # ==========================
    @allure.step("Находим первую карточку товара")
    def get_first_card(self):
        card = self.wait_visible(ProductConfig.CARD)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", card)
        return card

    @allure.step("Наводим мышь на карточку товара")
    def hover_card(self, card):
        ActionChains(self.driver).move_to_element(card).pause(0.4).perform()

        # дополнительный js, как в твоём тесте
        self.driver.execute_script("""
            arguments[0].dispatchEvent(new MouseEvent('mouseover', {bubbles:true}));
            arguments[0].dispatchEvent(new MouseEvent('mouseenter', {bubbles:true}));
        """, card)

        time.sleep(0.2)

    @allure.step("Нажимаем кнопку избранного на карточке")
    def click_favorite(self):
        fav_button = self.wait_clickable(ProductConfig.FAVORITE)
        fav_button.click()

    @allure.step("Ожидаем сообщение об успешном добавлении в избранное")
    def wait_favorite_added_message(self):
        return self.wait_visible(FavoritesLocators.FAVORITE_ADDED_MESSAGE)


    @allure.step("Нажимаем кнопку 'В корзину' на карточке")
    def click_add_to_cart_button(self):
        btn = self.wait_clickable(ProductConfig.BASKET)
        btn.click()

    # ==========================
    #     Параметры товара в модалке
    # ==========================
    @allure.step("Выбираем параметры товара: рост {1}, размер {2}")
    def select_product_params(self, height, size):
        from utils.test_helpers import select_product_params
        select_product_params(self.driver, height, size, use_modal=True)

