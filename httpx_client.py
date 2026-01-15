# import time
# import httpx  # Импортируем HTTPX
#
# # Шаг 1. Создание пользователя
# create_user_payload = {
#     "email": f"user.{time.time()}@example.com",  # Уникальный email с timestamp
#     "lastName": "string",
#     "firstName": "string",
#     "middleName": "string",
#     "phoneNumber": "string"
# }
# create_user_response = httpx.post("http://localhost:8003/api/v1/users", json=create_user_payload)
# create_user_response_data = create_user_response.json()
#
# print(create_user_response.json())

import time
import httpx  # Импортируем HTTPX

client = httpx.Client(base_url="http://localhost:8003",
                      timeout=100,
                      headers={"Authorization": "Bearer..."})

# Шаг 1. Создание пользователя
payload = {
    "email": f"user.{time.time()}@example.com",  # Уникальный email с timestamp
    "lastName": "string",
    "firstName": "string",
    "middleName": "string",
    "phoneNumber": "string"
}
response = client.post("/api/v1/users", json=payload)
print(response.text)
print(response.request.headers)



