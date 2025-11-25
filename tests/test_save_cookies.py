import time
import json
import pytest
from urls.urls import Urls



@pytest.mark.skip
def test_save_cookies_and_localstorage(driver):
    driver.get(Urls.BASE_URL)
    time.sleep(60)  # Время, чтобы вручную залогиниться

    # === Сохраняем cookies ===
    cookies = driver.get_cookies()

    with open("cookies.json", "w", encoding="utf-8") as f:
        json.dump(cookies, f, ensure_ascii=False, indent=4)

    print("✅ Cookies сохранены в cookies.json")

