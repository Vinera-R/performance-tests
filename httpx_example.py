from importlib.metadata import files

import httpx

response = httpx.get("https://jsonplaceholder.typicode.com/todos/1")
print(response.status_code)
print(response.json())

data = {
    "title": "Новая задача",
    "completed": False,
    "userId": 1
}
response = httpx.post("https://jsonplaceholder.typicode.com/todos/1", json=data, verify=False)
print(response.status_code)
print(response.json())

headers = {"Authorization": "Bearer my_secret_token"}

response = httpx.get("https://httpbin.org/get", headers=headers, verify=False)
print(response.status_code)
if response.content:
    print(response.json())
else:
    print("Пустой ответ")

    response = httpx.get("https://jsonplaceholder.typicode.com/todos?userId=1", headers=headers, verify=False)
    print(response.status_code)
    print(response.json())


files = {"file": ("example.txt", open("example.txt", "rb"))}
response = httpx.post("https://httpbin.org/post", files=files, verify=False)
print(response.status_code)
print(response.text)

client = httpx.Client(
    base_url="https://jsonplaceholder.typicode.com",
    headers = {"Authorization": "Bearer my_secret_token"})
response1 = client.get("/todos/1")
response2 = client.get("/todos/2")


print(response1.json())
print(response1.request.headers)
print(response2.json())



try:
    response = httpx.get("https://jsonplaceholder.typicode.com/invalid-url")
    response.raise_for_status()

except httpx.HTTPStatusError as e:
    print(f"Ошибка запроса: {e}")


try:
    response = httpx.get("https://httpbin.org/delay/5", timeout=2)

except httpx.ReadTimeout as e:
    print("Запрос превысил лимит времени")










