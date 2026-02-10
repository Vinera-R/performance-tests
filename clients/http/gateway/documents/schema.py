from pydantic import BaseModel, Field, ConfigDict


class DocumentRequestSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    account_id: str = Field(alias="accountId")
    document_type: str = Field(alias="documentType")


class DocumentSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    url: str
    document: str

class GetTariffDocumentResponseSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    tariff: DocumentSchema

class GetContractDocumentResponseSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    contract: DocumentSchema

