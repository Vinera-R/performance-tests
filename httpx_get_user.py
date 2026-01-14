import httpx
import time

create_user_payload = {
  "email": f"user{time.time()}@example.com",
  "lastName": "string",
  "firstName": "string",
  "middleName": "string",
  "phoneNumber": "string"
}

# POST-запрос на создание пользователя
create_user_response = httpx.post("http://localhost:8003/api/v1/users", json=create_user_payload)
print("Create user response:", create_user_response.json())
print("Status code:", create_user_response.status_code)

# Получение user_id из ответа
user_id = create_user_response.json()['user']['id']

# GET-запрос для получения информации по user_id
get_user_response = httpx.get(f"http://localhost:8003/api/v1/users/{user_id}")
print("Get user response:", get_user_response.json())
print("Status code:", get_user_response.status_code)


