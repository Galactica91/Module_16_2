from fastapi import FastAPI, Path
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
async def user_info(username: str=Path(min_length=5, max_length=20, description="Enter your username", example="universe"),
                    age: int=Path(le=120, ge=18, description="Enter your age", example="35")) -> dict:
    return {"message": f"Информация о пользователе: имя - {username}, возраст - {age}"}