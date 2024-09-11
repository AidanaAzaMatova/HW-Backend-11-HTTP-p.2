# 1-post-form
#
# Создайте HTTP-запрос POST, который отправит форму с полями "username" и "password" на
# URL "[www.example.com/login](http://www.example.com/login)".
# Используйте "Content-Type: application/x-www-form-urlencoded".
#
# Поле "username" должно содержать "admin", а поле "password" - "secret".
#
# Запрос должен использовать HTTP/1.1.
from fastapi import FastAPI, Form, Query
from pydantic import BaseModel

app = FastAPI()

@app.post("/login")
async def login(username: str, password: str):
    return {"username": username, "password": password}

## 2-post-json

# Создайте HTTP-запрос POST, который отправит данные в формате JSON на
# URL "[www.example.com/api/users](http://www.example.com/api/users)".
# Данные должны содержать поля "name" и "email". "name" должно содержать "John Doe",
# а "email" - "[john.doe@example.com](mailto:john.doe@example.com)".
#
# Используйте "Content-Type: application/json".
#
# Запрос должен использовать HTTP/1.1. Не забудьте указать длину контента с помощью заголовка "Content-Length".

# Определяем модель данных с использованием Pydantic
class User(BaseModel):
    name: str
    email: str

@app.post("/api/users")
async def create_user(user: User):
    return {"name": user.name, "email": user.email}

## 3-get-query-string

# Создайте HTTP-запрос GET, который запрашивает данные с сервера
# по URL "[www.example.com/search](http://www.example.com/search)".
# Запрос должен содержать строку запроса, которая передает ключ "query" со значением "blue shoes".
#
# Ваш запрос должен использовать HTTP/1.1.
@app.get("/search")
async def search(query: str):
    return {"query": query}