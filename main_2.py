from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

@app.get("/")
async def main_page() -> dict:
    return {"message": "Главная страница"}

@app.get("/user/admin")
async def admin_page() -> dict:
    return {"message": "Вы вошли как администратор"}

@app.get("/user/{user_id}")
async def user_id_page(user_id: int=Path(ge=1, le=100, description="Enter User ID", example="25, 55")) -> dict:
    return {"message": f"Вы вошли как пользователь N {user_id}"}

@app.get("/user/{username}/{age}")
async def user(username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example='UrbanUser')],
              age: Annotated[int, Path(ge=18, le=120, description='Enter age', example='24')]) -> str:
  return f'Информация о пользователе. Имя: {username}, Возраст: {age}'
