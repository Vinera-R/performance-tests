import time
import httpx  # Импортируем HTTPX

# Шаг 1. Создание пользователя
create_user_payload = {
    "email": f"user.{time.time()}@example.com",  # Уникальный email с timestamp
    "lastName": "string",
    "firstName": "string",
    "middleName": "string",
    "phoneNumber": "string"
}
create_user_response = httpx.post("http://localhost:8003/api/v1/users", json=create_user_payload)
create_user_response_data = create_user_response.json()

print(create_user_response.json())

# Шаг 2. Открытие кредитного счёта
open_credit_card_account_payload = {
    "userId": create_user_response_data["user"]["id"]
}
open_credit_card_account_response = httpx.post(
    "http://localhost:8003/api/v1/accounts/open-credit-card-account",
    json=open_credit_card_account_payload
)
open_credit_card_account_response_data = open_credit_card_account_response.json()

get_contract_document_response = httpx.get(
    f"http://localhost:8003/api/v1/documents/contract-document/"
    f"{open_credit_card_account_response_data['account']['id']}")

get_contract_document_response_data = get_contract_document_response.json()
print("Get contract document response:", get_contract_document_response_data)
print("Get contract status code:", get_contract_document_response.status_code)


