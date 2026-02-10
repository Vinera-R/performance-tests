from pydantic import BaseModel, Field, ConfigDict
from enum import StrEnum, IntEnum

class CardType(StrEnum):
    PHYSICAL = 'PHYSICAL'
    VIRTUAL = 'VIRTUAL'

class CardStatus(StrEnum):
    ACTIVE = 'ACTIVE'
    FROZEN = 'FROZEN'
    CLOSED = 'CLOSED'
    BLOCKED = 'BLOCKED'

class CardPaymentSystem(StrEnum):
    VISA = 'VISA'
    MASTERCARD = 'MASTERCARD'


class IssueVirtualCardRequestSchema(BaseModel):
    """
    Структура данных для выпуска виртуальной карты.
    """
    model_config = ConfigDict(populate_by_name=True)
    card_type: CardType = Field(alias='type')

    user_id: str = Field(alias='userId')
    account_id: str = Field(alias='accountId')

class CardSchema(BaseModel):
     id: str
     pin: str
     cvv: str
     type: CardType
     status: CardStatus
     account_id: str = Field(alias='accountId')
     card_number: str = Field(alias='cardNumber')
     card_holder: str = Field(alias='cardHolder')
     expiry_date: str = Field(alias='expiryDate')
     payment_system: CardPaymentSystem = Field(alias='paymentSystem')

class IssueVirtualCardResponseSchema(BaseModel):
    card: CardSchema

class IssuePhysicalCardRequestSchema(BaseModel):
    """
    Структура данных для выпуска физической карты.
    """
    user_id: str = Field(alias='userId')
    account_id: str = Field(alias='accountId')

class IssuePhysicalCardResponseSchema(BaseModel):
    card: CardSchema

