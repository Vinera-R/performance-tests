from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import date

''' Добавили модель UserSchema'''
class UserSchema(BaseModel):

        id: str
        email: EmailStr
        last_name: str = Field(alias="lastName")
        first_name: str = Field(alias="firstName")
        middle_name: str = Field(alias="middleName")
        phone_number: str = Field(alias="phoneNumber")

''' Создание пользователя'''
class CreateUserRequestSchema(BaseModel):
        email: EmailStr
        lastName: str = Field(alias="lastName", default="Иванов")
        firstName: str = Field(alias="firstName", default="Иван")
        middleName: str= Field(alias="middleName", default="Иванович")
        phoneNumber: str = Field(alias="phoneNumber", default="87998757466")

'''ответ API, содержащий объект пользователя в ключе 'user' '''
class CreateUserResponseSchema(BaseModel):
    user: UserSchema


''' Инициализируем модель CreateUserResponseSchema через JSON'''
user_json = """
{
  "user": {
    "id": "user-id",
    "email": "user@example.com",
    "lastName": "Иванов",
    "firstName": "Иван",
    "middleName": "Иванович",
    "phoneNumber": "87998757466"
  }
}
"""

response_model = CreateUserResponseSchema.model_validate_json(user_json)
print('Response JSON model:', response_model)

'''Инициализируем модель CreateUserResponseSchema через распаковку словаря'''
user_dict = {
  "user": {
    "id": "user-id",
    "email": "user@example.com",
    "lastName": "Иванов",
    "firstName": "Иван",
    "middleName": "Иванович",
    "phoneNumber": "87998757466"
  }
}
user_dict_model = CreateUserResponseSchema(**user_dict)
print('User dict model:', user_dict_model)






