from pydantic import BaseModel
class Address(BaseModel):
    city: str
    zip_code: str

class User(BaseModel):
    id: int
    name: str
    email: str
    address: Address
    is_active: bool = False

user = User(
    id=1,
    name='Alise',
    email='alice@example.com',
    address={"city": "New_York", "zip_code": "10001"}
)
print(user.name)
print(user.email)
print(user.address.city)




