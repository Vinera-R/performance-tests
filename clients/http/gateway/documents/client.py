from httpx import Response
from typing_extensions import TypedDict

from clients.http.client import HTTPClient
from clients.http.gateway.client import build_gateway_http_client


class DocumentDict(TypedDict):
        url: str
        document: str

class GetTariffDocumentResponseDict(TypedDict):
    tariff: DocumentDict

class GetContractDocumentResponseDict(TypedDict):
    contract: DocumentDict

class DocumentsGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с /api/v1/documents сервиса http-gateway.
    """

    def get_tariff_document_api(self, account_id: str) -> Response:
        """
        Получить тарифа по счету.

        :param account_id: Идентификатор счета.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get(f"/api/v1/documents/tariff-document/{account_id}")

    def get_contract_document_api(self, account_id: str) -> Response:
        """
        Получить контракта по счету.

        :param account_id: Идентификатор счета.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get(f"/api/v1/documents/contract-document/{account_id}")

    def get_tariff_document(self, account_id: str) -> GetTariffDocumentResponseDict:
        response = self.get_tariff_document_api(account_id)
        print(f"Response status: {response.status_code}")
        print(f"Response content: {response.text}")

        if response.status_code != 200:
            raise Exception(f"Ошибка при получении тарифа: статус {response.status_code}")
        if not response.content:
            raise Exception("Пустой ответ от сервера при получении тарифа")
        return response.json()


    def get_contract_document(self, account_id: str) -> GetContractDocumentResponseDict:
        response = self.get_contract_document_api(account_id)
        print(f"Response status: {response.status_code}")
        print(f"Response content: {response.text}")

        if response.status_code != 200:
            raise Exception(f"Ошибка при получении контракта: статус {response.status_code}")
        if not response.content:
            raise Exception("Пустой ответ от сервера при получении контракта")
        return response.json()


# Добавляем builder для DocumentsGatewayHTTPClient
def build_documents_gateway_http_client() -> DocumentsGatewayHTTPClient:
    """
       Функция создаёт экземпляр DocumentsGatewayHTTPClient с уже настроенным HTTP-клиентом.

       :return: Готовый к использованию DocumentsGatewayHTTPClient.
       """
    return DocumentsGatewayHTTPClient(client=build_gateway_http_client())



