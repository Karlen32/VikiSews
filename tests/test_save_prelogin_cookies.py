import json
import time
import pytest
from urls.urls import Urls


@pytest.mark.skip
def test_save_prelogin_cookies(driver):
    """
    Вручную закрыть окно cookies и окно геолокации, 
    НЕ авторизовываться, и сохранить cookies текущей сессии.
    """
    driver.get(Urls.BASE_URL)

    print("\n🔹 Открыл сайт. Сейчас ты можешь вручную:")
    print("   ✅ закрыть окно с cookies,")
    print("   ✅ разрешить или отклонить доступ к геолокации.")
    print("⚠️ Не авторизуйся! Просто закрой всплывающие окна.")
    print("⏳ У тебя есть 60 секунд, потом я сохраню cookies.\n")

    time.sleep(60)  # можешь увеличить, если нужно больше времени

    cookies = driver.get_cookies()
    with open("prelogin_cookies.json", "w", encoding="utf-8") as f:
        json.dump(cookies, f, indent=4, ensure_ascii=False)

    print("✅ Cookies без авторизации сохранены в 'prelogin_cookies.json'")
