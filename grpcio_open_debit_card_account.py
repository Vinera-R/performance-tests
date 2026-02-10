import grpc
from contracts.services.gateway.users.rpc_create_user_pb2 import CreateUserRequest, CreateUserResponse
from contracts.services.gateway.accounts.rpc_open_debit_card_account_pb2 import OpenDebitCardAccountRequest, OpenDebitCardAccountResponse
from contracts.services.gateway.accounts.accounts_gateway_service_pb2_grpc import AccountsGatewayServiceStub
from contracts.services.gateway.users.users_gateway_service_pb2_grpc import UsersGatewayServiceStub
from tools.fakers import fake

# Устанавливаем соединение с gRPC-gateway
channel = grpc.insecure_channel("localhost:9003")

# Инициализируем сервисы (stubs)
users_gateway_service = UsersGatewayServiceStub(channel)
accounts_gateway_service = AccountsGatewayServiceStub(channel)

# Создание пользователя
create_user_request = CreateUserRequest(
     email=fake.email(),
    last_name=fake.last_name(),
    first_name=fake.first_name(),
    middle_name=fake.last_name(),
    phone_number=fake.phone_number()
)

# Выполняем вызов и сохраняем ответ
create_user_response: CreateUserRequest = users_gateway_service.CreateUser(create_user_request)
print('Create_user_response:', create_user_response)

# Извлекаем ID только что созданного пользователя
new_user_id = create_user_response.user.id

# Формируем запрос на открытие дебетового счета
open_debit_card_account_request = OpenDebitCardAccountRequest(
    user_id=new_user_id
)

# Выполняем вызов сервиса AccountsGatewayService
open_debit_card_account_response:OpenDebitCardAccountResponse = accounts_gateway_service.OpenDebitCardAccount(open_debit_card_account_request)

print('OpenDebitCardAccountResponse:', open_debit_card_account_response)