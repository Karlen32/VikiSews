import allure
from pages.base_page import BasePage
from locators.favorits_locators import FavoritesLocators


class FavoritesPage(BasePage):

    @allure.step("Открываем избранное")
    def open_favorites(self):
        self.click(FavoritesLocators.HEADER_FAVORITES_BUTTON)
        self.wait_visible(FavoritesLocators.FAVORITES_PAGE_TITLE)

    @allure.step("Удаляем первый товар из избранного")
    def delete_first_favorite(self):
        delete_btn = self.wait_clickable(FavoritesLocators.FAVORITE_REMOVE_BUTTON)
        delete_btn.click()

        self.wait.until_not(
            lambda d: d.find_elements(*FavoritesLocators.FAVORITE_REMOVE_BUTTON)
        )
