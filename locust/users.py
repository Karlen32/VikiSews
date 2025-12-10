import json
import os
from locust import HttpUser, task, between


class VikiProdUser(HttpUser):
    """
    Пользователь для нагрузочного тестирования страницы заказов на PROD.
    Использует авторизацию через cookies из cookies_prod.json.
    """
    host = "https://viki-prod.ilar.dev-ilar.com"
    wait_time = between(1, 3)

    def on_start(self):
        """
        Загружает cookies из cookies_prod.json для авторизации пользователя.
        Использует заголовок Cookie для надежной установки всех cookies.
        """
        cookies_file = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            "cookies_prod.json"
        )

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

            # Устанавливаем все cookies через заголовок Cookie
            if cookie_parts:
                cookie_header = "; ".join(cookie_parts)
                self.client.headers.update({"Cookie": cookie_header})
                # Проверяем наличие важных cookies для авторизации
                important_cookies = ["PHPSESSID", "YCLB"]
                found_important = [c for c in cookies if c.get("name") in important_cookies]
                if found_important:
                    print(f"✔ Установлено {loaded_count} cookies (включая важные для авторизации)")
                else:
                    print(f"⚠ Установлено {loaded_count} cookies, но важные cookies авторизации не найдены")
            else:
                print("⚠ Не найдено валидных cookies в файле")

        except FileNotFoundError:
            print(f"⚠ Файл cookies_prod.json не найден по пути: {cookies_file}")
            print("⚠ Тест будет выполняться без авторизации")
        except Exception as e:
            print(f"❌ Ошибка загрузки cookies: {e}")

    @task
    def open_orders_page(self):
        """
        Открывает страницу заказов авторизованного пользователя.
        Проверяет статус ответа и обрабатывает различные сценарии.
        """
        with self.client.get("/personal/orders/", catch_response=True, name="Открытие страницы заказов") as response:
            if response.status_code == 200:
                # Проверяем, что не произошел редирект на страницу логина
                if "login" in response.url.lower() or "auth" in response.url.lower():
                    response.failure("Редирект на страницу логина - авторизация не работает")
                else:
                    response.success()
            elif response.status_code in (401, 403):
                response.failure(f"Ошибка авторизации: статус {response.status_code}")
            elif response.status_code in (301, 302, 307, 308):
                # Редирект - проверяем куда
                redirect_location = response.headers.get("Location", "")
                if "login" in redirect_location.lower() or "auth" in redirect_location.lower():
                    response.failure(f"Редирект на страницу логина: {redirect_location}")
                else:
                    response.failure(f"Неожиданный редирект: {redirect_location}")
            else:
                response.failure(f"Неожиданный статус-код: {response.status_code}")

