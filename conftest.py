import pytest
import json
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.vykrojki_locators import VykrojkiLocators
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from urls.urls import Urls
from utils.test_helpers import navigate_to_patterns, select_product_params, DEFAULT_TIMEOUT
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.firefox import GeckoDriverManager
from pages.login_page import LoginPage
from utils.credentials import Credentials
from pages.lk_page import LKPage


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser to run tests: chrome or firefox"
    )


@pytest.fixture(scope="function")
def driver(request):
    browser = request.config.getoption("--browser")

    if browser == "chrome":
        options = ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--no-sandbox")

        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=options
        )

    elif browser == "firefox":
        options = FirefoxOptions()
        options.set_preference("dom.webnotifications.enabled", False)
        options.set_preference("dom.push.enabled", False)
        # Firefox не умеет start-maximized как Chrome
        options.add_argument("--width=1920")
        options.add_argument("--height=1080")

        driver = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install()),
            options=options
        )

    else:
        raise ValueError(f"Unknown browser: {browser}")

    driver.implicitly_wait(5)
    yield driver
    driver.quit()

# === фикстура с prelogin cookies (без авторизации) ===
@pytest.fixture(scope="function")
def driver_prelogin():
    options = ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")

    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()),
        options=options
    )

    # 1 — открываем главную (важно — ДО добавления cookies)
    driver.get(Urls.BASE_URL)
    time.sleep(0.5)

    # 2 — загружаем prelogin cookies
    try:
        with open("prelogin_cookies.json", "r", encoding="utf-8") as f:
            cookies = json.load(f)

        applied = 0
        for cookie in cookies:
            cookie.pop("sameSite", None)
            cookie.pop("domain", None)
            cookie.pop("expiry", None)     # ⚠ обязательно

            try:
                driver.add_cookie(cookie)
                applied += 1
            except Exception:
                pass

        print(f"✅ Загружено prelogin cookies: {applied} из {len(cookies)}")

    except FileNotFoundError:
        pytest.skip("⚠ prelogin_cookies.json не найден — сначала создай через test_save_prelogin_cookies")

    # 3 — два обновления для активации cookies
    driver.refresh()
    time.sleep(0.5)
    driver.refresh()

    # 4 — Проверяем, что есть хотя бы одна кука, которую ты загрузил
    driver.get_cookies()

    if applied == 0:
        raise RuntimeError("❌ Ни одна cookie не была применена — проверь файл prelogin_cookies.json")

    print("🎉 prelogin cookies успешно применены!")
    
    yield driver
    driver.quit()


# Авторизованный пользователь
@pytest.fixture(scope="function")
def driver_logged(driver):
    driver.get(Urls.BASE_URL)

    try:
        with open("cookies.json", "r", encoding="utf-8") as f:
            cookies = json.load(f)

        for cookie in cookies:
            cookie.pop("sameSite", None)
            cookie.pop("domain", None)
            cookie.pop("expiry", None)
            driver.add_cookie(cookie)

    except FileNotFoundError:
        pytest.skip("⚠ cookies.json не найден — сначала сохрани куки вручную (test_save_cookies)")

    driver.refresh()

    return driver




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


@pytest.fixture
def driver_login_ui(driver):
    driver.get(Urls.BASE_URL)

    login = LoginPage(driver)
    login.open_login()
    login.enter_email(Credentials.USER["email"])
    login.enter_password(Credentials.USER["password"])
    login.submit()

    # Ожидание появления профиля или другой индикатор успешного входа
    lk = LKPage(driver)
    lk.open_menu()

    yield driver
    driver.quit()