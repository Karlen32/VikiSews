import json
import os
from locust import HttpUser, task, between


class FortuneSpinUser(HttpUser):
    """
    Нагрузочный пользователь для Fortune Spin API на PROD.
    Использует cookies из cookies_prod.json и реальный PHPSESSID из cookies.
    """
    host = "https://viki-prod.ilar.dev-ilar.com"
    wait_time = between(1, 2)

    def on_start(self):
        """
        Загружает cookies из cookies_prod.json для авторизации пользователя.
        Сохраняет PHPSESSID для использования в запросах.
        """
        cookies_file = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            "cookies_prod.json"
        )

        self.phpsessid = None

        try:
            with open(cookies_file, "r", encoding="utf-8") as f:
                cookies = json.load(f)

            cookie_parts = []
            loaded_count = 0

            for cookie in cookies:
                name = cookie.get("name")
                value = cookie.get("value")

                if name and value:
                    cookie_parts.append(f"{name}={value}")
                    loaded_count += 1

                    # Сохраняем PHPSESSID для использования в запросах
                    if name == "PHPSESSID":
                        self.phpsessid = value

            if cookie_parts:
                cookie_header = "; ".join(cookie_parts)
                self.client.headers.update({"Cookie": cookie_header})

                important_cookies = ["PHPSESSID", "YCLB"]
                found_important = [c for c in cookies if c.get("name") in important_cookies]
                if found_important:
                    print(f"✔ FortuneSpin: установлено {loaded_count} cookies (включая авторизационные)")
                    if self.phpsessid:
                        print(f"✔ FortuneSpin: PHPSESSID загружен: {self.phpsessid[:20]}...")
                else:
                    print(f"⚠ FortuneSpin: установлено {loaded_count} cookies, но важные cookies авторизации не найдены")
            else:
                print("⚠ FortuneSpin: cookies не найдены в файле")

        except FileNotFoundError:
            print(f"⚠ Файл cookies_prod.json не найден по пути: {cookies_file}")
            print("⚠ Тест Fortune Spin будет выполняться без авторизации")
        except Exception as e:
            print(f"❌ Ошибка загрузки cookies Fortune Spin: {e}")

    @task
    def trigger_fortune_spin(self):
        """
        Выполняет запрос к Fortune Spin API с реальным PHPSESSID из cookies.
        """
        # Используем реальный PHPSESSID из cookies
        if not self.phpsessid:
            # Если PHPSESSID не загружен, пробуем получить из заголовков
            cookie_header = self.client.headers.get("Cookie", "")
            if "PHPSESSID=" in cookie_header:
                # Извлекаем PHPSESSID из заголовка
                for part in cookie_header.split("; "):
                    if part.startswith("PHPSESSID="):
                        self.phpsessid = part.split("=", 1)[1]
                        break

        if not self.phpsessid:
            # Если PHPSESSID всё ещё не найден, используем пустую строку
            # и запрос вернёт ошибку, что поможет выявить проблему
            self.phpsessid = ""

        # Исправлена опечатка: fortune-speen.php -> fortune-spin.php
        endpoint = f"/local/action/fortune/fortune-spin.php?action=spin&sessid={self.phpsessid}"

        with self.client.get(endpoint, catch_response=True, name="Fortune Spin API") as response:
            if response.status_code == 200:
                # Проверяем, не перебросило ли на login
                if "login" in response.url.lower() or "auth" in response.url.lower():
                    response.failure("Редирект на страницу логина - авторизация не работает")
                else:
                    # Проверяем, что ответ валидный (может быть JSON с результатом)
                    try:
                        response.json()  # Проверяем, что ответ - валидный JSON
                        response.success()
                    except (ValueError, AttributeError):
                        # Если ответ не JSON, но статус 200 - считаем успешным
                        response.success()

            elif response.status_code in (401, 403):
                response.failure(f"Ошибка авторизации Fortune Spin: статус {response.status_code}")

            elif response.status_code in (301, 302, 307, 308):
                redirect_location = response.headers.get("Location", "")
                if "login" in redirect_location.lower() or "auth" in redirect_location.lower():
                    response.failure(f"Редирект на страницу логина: {redirect_location}")
                else:
                    response.failure(f"Неожиданный редирект: {redirect_location}")

            else:
                response.failure(f"Неожиданный статус-код: {response.status_code}")
