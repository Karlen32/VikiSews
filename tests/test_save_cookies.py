import json
import time
import pytest


@pytest.mark.skip
def test_save_cookies_and_localstorage(driver):
    driver.get("https://vikisews.com/")  # ← твой сайт
    time.sleep(40)  # время, чтобы ты вручную залогинился

    # === Сохраняем cookies ===
    cookies = driver.get_cookies()
    with open("cookies.json", "w", encoding="utf-8") as f:
        json.dump(cookies, f, ensure_ascii=False, indent=4)

    # === Сохраняем localStorage ===
    ls = driver.execute_script("return JSON.stringify(window.localStorage);")
    with open("cookies.json", "w", encoding="utf-8") as f:
        f.write(ls)

    print("✅ Cookies и localStorage сохранены.")
