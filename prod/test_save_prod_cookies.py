import os
import time
import json
import pytest
import allure


PROD_URL = "https://viki-prod.ilar.dev-ilar.com"
COOKIES_FILE = "cookies_prod.json"


@pytest.mark.manual
@allure.title("Сохранение cookies с авторизацией на PROD")
def test_save_prod_cookies(driver):
    """
    Тест для сохранения cookies с авторизацией на PROD.
    Использует фикстуру driver, но работает с отдельным PROD доменом.
    Открывает PROD, дает время для ручной авторизации, затем сохраняет cookies в cookies_prod.json.
    """
    # 1. Открываем PROD (отдельный домен, независимо от других тестов)
    driver.get(PROD_URL)
    time.sleep(1)

    print("\n" + "="*60)
    print("🔹 Открыт PROD сайт")
    print("🔹 Сейчас ты можешь вручную авторизоваться")
    print("⚠️ У тебя есть 60 секунд для авторизации")
    print("="*60 + "\n")

    # 2. Даем время для ручной авторизации
    time.sleep(60)

    # 3. Сохраняем cookies
    cookies = driver.get_cookies()

    if not cookies:
        print("⚠️ Cookies не найдены — возможно, авторизация не выполнена")
        pytest.skip("Cookies не найдены — авторизация не выполнена")

    # 4. Определяем путь к файлу (корень проекта)
    cookies_file_path = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        COOKIES_FILE
    )

    # 5. Сохраняем cookies в файл
    with open(cookies_file_path, "w", encoding="utf-8") as f:
        json.dump(cookies, f, ensure_ascii=False, indent=4)

    print(f"\n✔ PROD cookies сохранены в {cookies_file_path}")
    print(f"✔ Сохранено {len(cookies)} cookies")
    
    # Показываем некоторые сохраненные cookies для проверки
    important_cookies = [c for c in cookies if c.get("name") in ["PHPSESSID", "YCLB", "BITRIX_SM_GUEST_ID"]]
    if important_cookies:
        print("\n🔹 Важные cookies:")
        for cookie in important_cookies:
            print(f"   - {cookie.get('name')}: {cookie.get('value')[:20]}...")
