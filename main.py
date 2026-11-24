from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Shakhverdyan API")


class User(BaseModel):
    first_name: str
    last_name: str
    login: str
    email: str
    password: str


class UserUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    login: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None


# --- Чтение (Read) ---

@app.get("/users",
         summary="Получение списка пользователей",
         description="Возвращает список пользователей с пагинацией",
         status_code=200)
def get_users(limit: Optional[int] = None, page: Optional[int] = None):
    return {
        "users": [],
        "page": page if page is not None else 1,
        "limit": limit if limit is not None else 20,
    }


@app.get("/users/{user_id}",
         summary="Получение пользователя по ID",
         description="Возвращает пользователя по его уникальному идентификатору",
         status_code=200)
def get_user(user_id: int):
    return {"user_id": user_id}


# --- Создание (Create) ---

@app.post("/user/create_user",
          summary="Создаёт пользователя",
          description="Эндпоинт который создаёт нового пользователя",
          status_code=200,
          response_model=User)
def create_user(user: User) -> Optional[User]:
    return user


# --- Обновление (Update) ---

@app.put("/user/update_user/{user_id}",
         summary="Обновление пользователя (полное)",
         description="Полностью обновляет данные пользователя по его ID",
         status_code=200,
         response_model=User)
def update_user(user_id: int, user: User) -> Optional[User]:
    return user


@app.patch("/user/update_user/{user_id}",
           summary="Обновление пользователя (частичное)",
           description="Частично обновляет данные пользователя по его ID",
           status_code=200,
           response_model=UserUpdate)
def update_user_partial(user_id: int, user: UserUpdate) -> Optional[UserUpdate]:
    return user


# --- Удаление (Delete) ---

@app.delete("/user/delete_user/{user_id}",
            summary="Удаление пользователя",
            description="Удаляет пользователя по его ID",
            status_code=200)
def delete_user(user_id: int):
    return {"user_id": user_id}