import json
import os
import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager


PROD_URL = "https://viki-prod.ilar.dev-ilar.com"
COOKIES_FILE = "cookies_prod.json"


@pytest.mark.manual
def test_login_check_prod():
    """
    Независимый тест для проверки авторизации на PROD.
    Загружает cookies_prod.json, открывает PROD и проверяет — вошёл ли пользователь.
    Тест полностью независим от других тестов и conftest.py.
    """
    # Настройка Chrome драйвера
    options = ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")

    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()),
        options=options
    )

    try:
        # 1. Открываем PROD (важно — ДО добавления cookies)
        driver.get(PROD_URL)
        time.sleep(0.5)

        # 2. Загружаем cookies из cookies_prod.json
        cookies_file_path = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            COOKIES_FILE
        )

        try:
            with open(cookies_file_path, "r", encoding="utf-8") as f:
                cookies_prod = json.load(f)

            applied = 0
            for cookie in cookies_prod:
                # Проверяем наличие обязательных полей
                if "name" not in cookie or "value" not in cookie:
                    continue

                # Подготавливаем cookie для Selenium
                cookie_for_selenium = {
                    "name": cookie["name"],
                    "value": cookie["value"],
                }

                # Используем domain из файла, если есть, иначе используем домен по умолчанию
                domain = cookie.get("domain", "viki-prod.ilar.dev-ilar.com")
                # Убираем точку в начале, если есть (Selenium требует без точки для текущего домена)
                if domain.startswith("."):
                    domain = domain[1:]
                cookie_for_selenium["domain"] = domain

                # Используем path из файла, если есть
                if "path" in cookie:
                    cookie_for_selenium["path"] = cookie["path"]

                # Удаляем поля, которые могут вызвать проблемы в Selenium
                # sameSite и expiry не нужны для add_cookie

                try:
                    driver.add_cookie(cookie_for_selenium)
                    applied += 1
                except Exception as e:
                    print(f"⚠ Не удалось добавить cookie {cookie.get('name')}: {e}")

            print(f"✔ Загружено {applied} cookies из {len(cookies_prod)}")

            if applied == 0:
                raise RuntimeError("❌ Ни одна cookie не была применена — проверь файл cookies_prod.json")

        except FileNotFoundError:
            pytest.skip(f"⚠ Файл {cookies_file_path} не найден — сначала создай через test_save_prod_cookies")

        # 3. Обновляем страницу для применения cookies
        driver.refresh()
        time.sleep(2)

        # 4. Проверяем результат авторизации
        current_url = driver.current_url
        print(f">>> Текущий URL после применения cookies: {current_url}")

        if "login" in current_url.lower() or "auth" in current_url.lower():
            print("❌ НЕ авторизован — редирект на страницу логина")
            assert False, "Пользователь не авторизован — произошел редирект на страницу логина"
        else:
            print("✔ Пользователь авторизован — доступ к странице открыт")
            assert True, "Пользователь успешно авторизован"

    finally:
        driver.quit()
