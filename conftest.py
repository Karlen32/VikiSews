import pytest
import json
import time
from selenium.common.exceptions import WebDriverException
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.vykrojki_locators import VykrojkiLocators
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from urls.urls import Urls
from utils.test_helpers import navigate_to_patterns, select_product_params, DEFAULT_TIMEOUT


# === базовый драйвер ===
@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    # Больше стабильности при нестабильном DOM
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


# === фикстура с prelogin cookies (без авторизации) ===
@pytest.fixture(scope="function")
def driver_prelogin():
    """
    Стабильно загружает prelogin_cookies даже в режиме инкогнито.
    Делает:
    1. старт инкогнито
    2. ждет полной загрузки страницы
    3. добавляет куки
    4. выполняет двойной refresh (важно!)
    5. проверяет, что куки установились
    """

    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")

    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()),
        options=options
    )

    # 1 — открываем главную
    driver.get(Urls.BASE_URL)
    time.sleep(1)  # даем странице "осесть"

    try:
        with open("prelogin_cookies.json", "r", encoding="utf-8") as f:
            cookies = json.load(f)

        applied = 0
        for cookie in cookies:
            cookie.pop("sameSite", None)
            cookie.pop("domain", None)

            try:
                driver.add_cookie(cookie)
                applied += 1
            except WebDriverException:
                pass

        print(f"✅ Загружено prelogin cookies: {applied} из {len(cookies)}")

    except FileNotFoundError:
        pytest.skip("⚠ prelogin_cookies.json не найден — сначала запусти test_save_prelogin_cookies.py")

    # 3 — критически важно: дважды обновить
    driver.refresh()
    time.sleep(0.6)
    driver.refresh()

    # 4 — проверка что куки действительно живые
    current_cookies = driver.get_cookies()
    if len(current_cookies) == 0:
        raise RuntimeError("❌ Cookies НЕ применились! Chrome в инкогнито их отбросил.")

    print("🎉 prelogin cookies успешно применены!")

    yield driver
    driver.quit()


# === фикстура с login cookies (уже авторизованный пользователь) ===
@pytest.fixture(scope="function")
def driver_logged(driver):
    """
    Загружает логин-сессию через cookies и localStorage.
    Работает даже если localstorage.json отсутствует.
    """

    # 1. Полная очистка куков перед началом
    driver.delete_all_cookies()

    # 2. Открываем сайт — база для куков
    driver.get(Urls.BASE_URL)
    try:
        with open("cookies.json", "r", encoding="utf-8") as f:
            cookies = json.load(f)

        for cookie in cookies:
            cookie.pop("sameSite", None)
            cookie.pop("domain", None)

            try:
                driver.add_cookie(cookie)
            except WebDriverException:
                # Пропускаем куки, которые Selenium не принимает
                pass

        print(f"✅ Загружено cookies: {len(cookies)}")

    except FileNotFoundError:
        pytest.skip("⚠ cookies.json не найден — сначала сохрани куки вручную (test_save_cookies)")

    try:
        with open("localstorage.json", "r", encoding="utf-8") as f:
            localstorage_data = json.loads(f.read())

        for key, value in localstorage_data.items():
            driver.execute_script(
                "window.localStorage.setItem(arguments[0], arguments[1]);",
                key, value
            )

        print("✅ localStorage восстановлен")

    except FileNotFoundError:
        print("⚠ localstorage.json не найден — продолжаю без него (это НЕ ошибка)")

    # 5. Финальный refresh — сессия активируется
    driver.refresh()

    return driver


# === базовый URL ===
@pytest.fixture(scope="session")
def base_url():
    return Urls.BASE_URL



@pytest.fixture
def select_product(driver_logged):
    """
    Универсальная фикстура:
    driver = select_product(name="Джуанна платье", height="162-168", size="38")
    """
    def _select(name: str, height: str, size: str):
        driver = driver_logged

        # 1. Переход в «Выкройки»
        navigate_to_patterns(driver)

        # 2. Открываем нужную карточку
        WebDriverWait(driver, DEFAULT_TIMEOUT).until(
            EC.element_to_be_clickable(VykrojkiLocators.pattern_card_by_name(name))
        ).click()

        # 3. Выбор параметров
        select_product_params(driver, height, size)

        print(f"✅ Товар '{name}' выбран (рост {height}, размер {size})")

        return driver

    return _select