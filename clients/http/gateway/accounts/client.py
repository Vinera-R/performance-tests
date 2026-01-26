
from clients.http.client import HTTPClient
from httpx import Response, QueryParams
from typing import TypedDict

from clients.http.gateway.cards.client import CardDict
from clients.http.gateway.client import build_gateway_http_client

class AccountDict(TypedDict):
    id: str
    type: str
    cards: list[CardDict]
    balance: float


class GetAccountsQueryDict(TypedDict):
    userId: str

class GetAccountsResponseDict(TypedDict):
    accounts: list[AccountDict]


class OpenDepositAccountRequestDict(TypedDict):
    userId: str

class OpenDepositAccountResponseDict(TypedDict):
    account: AccountDict

class OpenSavingsAccountRequestDict(TypedDict):
    userId: str

class OpenSavingsAccountResponseDict(TypedDict):
    account: AccountDict


class OpenDebitCardAccountRequestDict(TypedDict):
    userId: str

class OpenDebitCardAccountResponseDict(TypedDict):
    account: AccountDict

class OpenCreditCardAccountRequestDict(TypedDict):
    userId: str

class OpenCreditCardAccountResponseDict(TypedDict):
    account: AccountDict

class AccountsGatewayHTTPClient(HTTPClient):
    def get_accounts_api(self, query: GetAccountsQueryDict) -> Response:
        return self.get("/api/v1/accounts", params=QueryParams(**query))


    def open_deposit_account_api(self, request: OpenDepositAccountRequestDict) -> Response:
        return self.post("/api/v1/accounts/open_deposit_account", json=request)

    def open_savings_account_api(self, request: OpenSavingsAccountRequestDict) -> Response:
        return self.post("/api/v1/accounts/open_savings_account", json=request)

    def open_debit_card_account_api(self, request: OpenDebitCardAccountRequestDict) -> Response:
        return self.post("/api/v1/accounts/open-debit-card-account", json=request)

    def open_credit_card_account_api(self, request: OpenCreditCardAccountRequestDict) -> Response:
        return self.post("/api/v1/accounts/open-credit-card-account", json=request)

    def get_accounts(self, user_id: str) -> GetAccountsResponseDict:
        query = GetAccountsQueryDict(userId=user_id)
        response = self.get_accounts_api(query)
        return response.json()

    def open_deposit_account(self, user_id: str) -> OpenDepositAccountResponseDict:
        request = OpenDepositAccountRequestDict(userId=user_id)
        response = self.open_deposit_account_api(request)
        return response.json()

    def open_savings_account(self, user_id: str) -> OpenSavingsAccountResponseDict:
        request = OpenSavingsAccountRequestDict(userId=user_id)
        response = self.open_savings_account_api(request)
        return response.json()

    def open_debit_card_account(self, user_id: str) -> OpenDebitCardAccountResponseDict:
        request = OpenDebitCardAccountRequestDict(userId=user_id)
        response = self.open_debit_card_account_api(request)
        return response.json()

    def open_credit_card_account(self, user_id: str) -> OpenCreditCardAccountResponseDict:
        request = OpenCreditCardAccountRequestDict(userId=user_id)
        response = self.open_credit_card_account_api(request)
        return response.json()



# Добавляем builder для AccountsGatewayHTTPClient
def build_account_gateway_http_client() -> AccountsGatewayHTTPClient:
    """
        Функция создаёт экземпляр AccountsGatewayHTTPClient с уже настроенным HTTP-клиентом.

        :return: Готовый к использованию AccountsGatewayHTTPClient.
        """
    return AccountsGatewayHTTPClient(client=build_gateway_http_client())

