from locust import HttpUser, between, task
from tools.fakers import fake  # генератор случайных данных

class OpenDebitCardAccountScenarioUser(HttpUser):
    # Пауза между запросами для каждого виртуального пользователя (в секундах)
    wait_time = between(1, 3)
    user_data: dict

    def on_start(self) -> None:
        request = {
            "email": fake.email(),
            "lastName": fake.last_name(),
            "firstName": fake.first_name(),
            "middleName": fake.middle_name(),
            "phoneNumber": fake.phone_number()
        }
        response = self.client.post("/api/v1/users", json=request)

        # Сохраняем полученные данные, включая ID пользователя
        self.user_data = response.json()

    @task
    def open_debit_account(self) -> None:
        request = {
            "userId": self.user_data["user"]["id"]
        }
        self.client.post(
            "/api/v1/accounts/open-debit-card-account",
            json=request,
            name="/api/v1/accounts/open-debit-card-account"
        )







