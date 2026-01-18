
from clients.http.client import HTTPClient
from httpx import Response, QueryParams
from typing import TypedDict

class GetOperationResponse(TypedDict):
    """Тип данных для ответа по конкретной операции."""
    operation_id: str

class GetOperationReceiptResponse(TypedDict):
    """Тип данных для ответа с чеком операции."""
    operation_id: str

class GetOperationsQueryDict(TypedDict):
    """Тип данных для параметров запроса списка операций."""
    accountId: str

class GetOperationSummaryQueryDict(TypedDict):
    """Тип данных для параметров запроса статистики операций."""
    accountId: str

class MakeFeeOperationRequestDict(TypedDict):
    """Тип данных для запроса создания операции комиссии."""
    status: str
    amount: float
    cardId: str
    accountId: str

class MakeTopUpOperationRequestDict(TypedDict):
    """Тип данных для запроса создания операции пополнения."""
    status: str
    amount: float
    cardId: str
    accountId: str

class MakeCashbackOperationRequestDict(TypedDict):
    """Тип данных для запроса создания операции кэшбэка."""
    status: str
    amount: float
    cardId: str
    accountId: str

class MakeTransferOperationRequestDict(TypedDict):
    """Тип данных для запроса создания операции перевода."""
    status: str
    amount: float
    cardId: str
    accountId: str

class MakePurchaseOperationRequestDict(TypedDict):
    """Тип данных для запроса создания операции покупки."""
    status: str
    amount: float
    cardId: str
    accountId: str
    category: str

class MakeBillPaymentOperationRequestDict(TypedDict):
    """Тип данных для запроса создания операции оплаты по счету."""
    status: str
    amount: float
    cardId: str
    accountId: str

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
        return self.get(f"/api/v1/operations/operation-receipt/{operation_id}/receipt")

    def get_operations_api(self, query: GetOperationsQueryDict) -> Response:
        """
        Получает список операций для указанного счета.

        :param query: Параметры запроса, содержащие accountId.
        :return: Объект Response со списком операций.
        """
        return self.get("/api/v1/operations", params=QueryParams)

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



























