from pydantic import BaseModel, Field, ConfigDict
from enum import StrEnum, Enum
from clients.http.gateway.cards.schema import CardSchema


class AccountType(str, Enum):
    DEPOSIT = "DEPOSIT"
    SAVINGS = "SAVINGS"
    DEBIT_CARD = "DEBIT_CARD"
    CREDIT_CARD = "CREDIT_CARD"

class AccountStatus(str, Enum):
    ACTIVE = "ACTIVE"
    CLOSED = "CLOSED"
    PENDING_CLOSURE = "PENDING_CLOSURE"


class AccountSchema(BaseModel):
    id: str
    type: AccountType
    cards: list[CardSchema]
    status: AccountStatus
    balance: float



class GetAccountsQuerySchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    user_id: str = Field(alias='userId')

class GetAccountsResponseSchema(BaseModel):
    accounts: list[AccountSchema]


class OpenDepositAccountRequestSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    user_id: str = Field(alias='userId')

class OpenDepositAccountResponseSchema(BaseModel):
    account: AccountSchema

class OpenSavingsAccountRequestSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    user_id: str = Field(alias='userId')

class OpenSavingsAccountResponseSchema(BaseModel):

    account: AccountSchema


class OpenDebitCardAccountRequestSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    user_id: str = Field(alias='userId')

class OpenDebitCardAccountResponseSchema(BaseModel):
    account: AccountSchema

class OpenCreditCardAccountRequestSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    user_id: str = Field(alias='userId')

class OpenCreditCardAccountResponseSchema(BaseModel):
    account: AccountSchema

