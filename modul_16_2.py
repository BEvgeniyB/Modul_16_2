from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()


@app.get("/")
async def welcome() -> dict:
    return {"message": "hello"}



@app.get("/user/admin")
async def admin_page() -> dict:
    return {"message": "Вы вошли как администратор"}



@app.get("/user/{user_id}")
async def users(user_id: int = Path(ge=1, le=100, description="Enter User ID", example="10")) -> dict:
    return {"message": f"Вы вошли как пользователь № {user_id}"}


@app.get("/user/{user_name}/{age}")
async def users_info(
        user_name:Annotated[ str,Path(min_length=5, max_length=20, description="Enter username", example="UrbanUser")]
        , age: int = Path(ge=18, le=120, description="Enter age", example="24")) -> dict:
    return {"message": f"Информация о пользователе. Имя: {user_name}, Возраст:{age} "}
