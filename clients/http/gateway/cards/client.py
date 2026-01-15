from clients.http.client import HTTPClient
from typing import TypedDict
from httpx import Response

class CreateUserRequestDict(TypedDict):
    """
    Структура данных для создания нового пользователя.
    """
    email: str
    lastName: str
    firstName: str
    middleName: str
    phoneNumber: str

class UsersGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с /api/v1/users сервиса http-gateway.
    """
    def get_user_api(self, user_id: str) -> Response:
        """
        Получить данные пользователя по его user_id.

        :param user_id: Идентификатор пользователя.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get(f"/api/v1/users/{user_id}")

class CardsGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с /api/v1/cards сервиса http-gateway.
    """
    def issue_virtual_card_api(self, request: CreateUserRequestDict) -> Response:
        """
        Выполняет POST-запрос к эндпоинту /api/v1/cards/issue-virtual-card для создания виртуальной карты.

        :param request: словарь с данными для создания виртуальной карты.
        :return: ответ от сервера (httpx.Response).
        """
        return self.post(f"/api/v1/cards/issue-virtual-card", json=request)

    def issue_physical_card_api(self, request: CreateUserRequestDict) -> Response:
        """
        Выполняет POST-запрос к эндпоинту /api/v1/cards/issue-physical-card для создания физической карты.

        :param request: словарь с данными для создания физической карты.
        :return: ответ от сервера (httpx.Response).
        """
        return self.post(f"/api/v1/cards/issue-physical-card", json=request.json)

