import httpx
import time

create_user_payload = {
    "email": f"user{time.time()}@example.com",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string",
    "phoneNumber": "string"
}

# Создание пользователя
create_user_response = httpx.post("http://localhost:8003/api/v1/users", json=create_user_payload)
print("Create user response:", create_user_response.json())
print("Status code:", create_user_response.status_code)

# Получение user_id
user_id = create_user_response.json()['user']['id']

# Открытие депозитного счета с передачей user_id в теле
response = httpx.post(
    "http://localhost:8003/api/v1/accounts/open-deposit-account",
    json={"userId": user_id}
)

print("Ответ на открытие депозита:", response.json())
print("Статус-код:", response.status_code)



