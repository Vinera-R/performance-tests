
from clients.http.client import HTTPClient
from httpx import Response, QueryParams
from typing import TypedDict

from clients.http.gateway.client import build_gateway_http_client


class OperationDict(TypedDict):
    id: str
    type: str
    status: str
    amount: float
    cardId: str
    category: str
    createdAt: str
    accountId: str

class GetOperationResponseDict(TypedDict):
    """Тип данных для ответа по конкретной операции."""
    operation_id: OperationDict



class OperationReceiptDict(TypedDict):
        url: str
        document: str

class GetOperationReceiptResponse(TypedDict):
    """Тип данных для ответа с чеком операции."""
    operation_id: OperationReceiptDict



class OperationDict(TypedDict):
    id: str
    type: str
    status: str
    amount: float
    cardId: str
    category: str
    createdAt: str
    accountId: str

class GetOperationsResponseDict(TypedDict):
    operations: list[OperationDict]

class GetOperationsQueryDict(TypedDict):
    """Тип данных для параметров запроса списка операций."""
    accountId: str


class OperationsSummaryDict(TypedDict):
    spentAmount: float
    receivedAmount: float
    cashbackAmount: float

class GetOperationsSummaryResponseDict(TypedDict):
    summary: OperationsSummaryDict

class GetOperationSummaryQueryDict(TypedDict):
    """Тип данных для параметров запроса статистики операций."""
    accountId: str




class MakeFeeOperationResponseDict(TypedDict):
    operation: list[OperationDict]


class MakeFeeOperationRequestDict(TypedDict):
    """Тип данных для запроса создания операции комиссии."""
    status: str
    amount: float
    cardId: str
    accountId: str



class MakeTopUpOperationResponseDict(TypedDict):
    operation: list[OperationDict]


class MakeTopUpOperationRequestDict(TypedDict):
    """Тип данных для запроса создания операции пополнения."""
    status: str
    amount: float
    cardId: str
    accountId: str


class MakeCashbackOperationResponseDict(TypedDict):
    operation: list[OperationDict]

class MakeCashbackOperationRequestDict(TypedDict):
    """Тип данных для запроса создания операции кэшбэка."""
    status: str
    amount: float
    cardId: str
    accountId: str


class MakeTransferOperationResponseDict(TypedDict):
    operation: list[OperationDict]

class MakeTransferOperationRequestDict(TypedDict):
    """Тип данных для запроса создания операции перевода."""
    status: str
    amount: float
    cardId: str
    accountId: str


class MakePurchaseOperationResponseDict(TypedDict):
    operation: list[OperationDict]

class MakePurchaseOperationRequestDict(TypedDict):
    """Тип данных для запроса создания операции покупки."""
    status: str
    amount: float
    cardId: str
    accountId: str
    category: str


class MakeBillPaymentOperationResponseDict(TypedDict):
    operation: list[OperationDict]

class MakeBillPaymentOperationRequestDict(TypedDict):
    """Тип данных для запроса создания операции оплаты по счету."""
    status: str
    amount: float
    cardId: str
    accountId: str

class MakeCashWithdrawalOperationResponseDict(TypedDict):
    operation: list[OperationDict]

class MakeCashWithdrawalOperationRequestDict(TypedDict):
    """Тип данных для запроса создания операции снятия наличных."""
    status: str
    amount: float
    cardId: str
    accountId: str


class OperationsGatewayHTTPClient(HTTPClient):
    """
    Клиент API для взаимодействия с эндпоинтами /api/v1/operations.
    """

    def get_operation_api(self, operation_id: str) -> Response:
        """
        Получает информацию об операции по её идентификатору.

        :param operation_id: Уникальный идентификатор операции.
        :return: Объект Response с данными операции.
        """
        return self.get(f"/api/v1/operations/{operation_id}")

    def get_operation_receipt_api(self, operation_id: str) -> Response:
        """
        Получает чек по операции по её идентификатору.

        :param operation_id: Уникальный идентификатор операции.
        :return: Объект Response с чеком операции.
        """
        return self.get(f"/api/v1/operations/operation-receipt/{operation_id}")

    def get_operations_api(self, query: GetOperationsQueryDict) -> Response:
        """
        Получает список операций для указанного счета.

        :param query: Параметры запроса, содержащие accountId.
        :return: Объект Response со списком операций.
        """
        return self.get("/api/v1/operations", params=QueryParams(**query))

    def get_operations_summary_api(self, query: GetOperationSummaryQueryDict) -> Response:
        """
        Получает сводную статистику по операциям для указанного счета.

        :param query: Параметры запроса, содержащие accountId.
        :return: Объект Response со сводной информацией.
        """
        return self.get("/api/v1/operations/operations-summary", params=QueryParams)

    def make_fee_operation_api(self, request: MakeFeeOperationRequestDict) -> Response:
        """
        Создает операцию по комиссии.

        :param request: Данные для создания операции.
        :return: Объект Response с результатом выполнения.
        """
        return self.post("/api/v1/operations/make-fee-operation", json=request)

    def make_top_up_operation_api(self, request: MakeTopUpOperationRequestDict) -> Response:
        """
        Создает операцию пополнения.

        :param request: Данные для создания операции.
        :return: Объект Response с результатом выполнения.
        """
        return self.post("/api/v1/operations/make-top-up-operation", json=request)

    def make_cashback_operation_api(self, request: MakeCashbackOperationRequestDict) -> Response:
        """
        Создает операцию кэшбэка.

        :param request: Данные для создания операции.
        :return: Объект Response с результатом выполнения.
        """
        return self.post("/api/v1/operations/make-cashback-operation", json=request)

    def make_transfer_operation_api(self, request: MakeTransferOperationRequestDict) -> Response:
        """
        Создает операцию перевода.

        :param request: Данные для создания операции.
        :return: Объект Response с результатом выполнения.
        """
        return self.post("/api/v1/operations/make-transfer-operation", json=request)

    def make_purchase_operation_api(self, request: MakePurchaseOperationRequestDict) -> Response:
        """
        Создает операцию покупки.

        :param request: Данные для создания операции.
        :return: Объект Response с результатом выполнения.
        """
        return self.post("/api/v1/operations/make-purchase-operation", json=request)

    def make_bill_payment_operation_api(self, request: MakeBillPaymentOperationRequestDict) -> Response:
        """
        Создает операцию оплаты по счету.

        :param request: Данные для создания операции.
        :return: Объект Response с результатом выполнения.
        """
        return self.post("/api/v1/operations/make-bill-payment-operation", json=request)

    def make_cash_withdrawal_operation_api(self, request: MakeCashWithdrawalOperationRequestDict) -> Response:
        """
        Создает операцию снятия наличных.

        :param request: Данные для создания операции.
        :return: Объект Response с результатом выполнения.
        """
        return self.post("/api/v1/operations/make-cash-withdrawal-operation", json=request)

    def get_operation(self, operation_id: str) -> GetOperationResponseDict:
        response = self.get(f"/api/v1/operations/{operation_id}")
        return response.json()

    def get_operation_receipt(self, operation_id: str) -> GetOperationReceiptResponse:
        response = self.get(f"/api/v1/operations/{operation_id}/receipt")
        return response.json()

    def get_operations(self, account_id: str) -> GetOperationsResponseDict:
        query = GetOperationsQueryDict(accountId=account_id)
        response = self.get_operations_api(query)
        return response.json()

    def get_operations_summary(self, account_id: str) -> GetOperationsSummaryResponseDict:
        query = GetOperationSummaryQueryDict(accountId=account_id)
        response = self.get(f"/api/v1/operations/summary")
        return response.json()

    def make_fee_operation(self, card_id: str, account_id: str) -> MakeFeeOperationResponseDict:
        request = MakeFeeOperationRequestDict(
            status="COMPLETED",
            amount=55.77,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_fee_operation_api(request)
        return response.json()

    def make_top_up_operation(self, card_id: str, account_id: str) -> MakeTopUpOperationResponseDict:
        request = MakeTopUpOperationRequestDict(
            status="COMPLETED",
            amount=55.77,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_top_up_operation_api(request)
        return response.json()

    def make_cashback_operation(self, card_id: str, account_id: str) -> MakeCashbackOperationResponseDict:
        request = MakeCashbackOperationRequestDict(
            status="COMPLETED",
            amount=55.77,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_cashback_operation_api(request)
        return response.json()

    def make_transfer_operation(self, card_id: str, account_id: str) -> MakeTransferOperationResponseDict:
        request = MakeTransferOperationRequestDict(
            status="COMPLETED",
            amount=55.77,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_transfer_operation_api(request)
        return response.json()

    def make_purchase_operation(self, card_id: str, account_id: str) -> MakePurchaseOperationResponseDict:
        request = MakePurchaseOperationRequestDict(
            status="COMPLETED",
            amount=55.77,
            cardId=card_id,
            accountId=account_id,
            category="str"

        )
        response = self.make_purchase_operation_api(request)
        return response.json()

    def make_bill_payment_operation(self, card_id: str, account_id: str) -> MakeBillPaymentOperationResponseDict:
        request = MakeBillPaymentOperationRequestDict(
            status="COMPLETED",
            amount=55.77,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_bill_payment_operation_api(request)
        return response.json()

    def make_cash_withdrawal_operation(self, card_id: str, account_id: str) -> MakeCashWithdrawalOperationResponseDict:
        request = MakeCashWithdrawalOperationRequestDict(
            status="COMPLETED",
            amount=55.77,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_cash_withdrawal_operation_api(request)
        return response.json()



# Добавляем builder для DocumentsGatewayHTTPClient
def build_operations_gateway_http_client() -> OperationsGatewayHTTPClient:
    """
           Функция создаёт экземпляр OperationsGatewayHTTPClient с уже настроенным HTTP-клиентом.

           :return: Готовый к использованию OperationsGatewayHTTPClient.
           """
    return OperationsGatewayHTTPClient(client=build_gateway_http_client())




























