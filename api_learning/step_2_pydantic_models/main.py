from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field,  ValidationError, EmailStr
import uvicorn

app = FastAPI()

users_db = []

class User_Model(BaseModel):
    name: str = Field(min_length=3)
    age: int | None = Field(ge=18)
    email: EmailStr

@app.post("/users/")
def add_user(user: User_Model) -> dict[str, str]:
    try:
        users_db.append({
            "id": len(users_db) + 1,
            "name": user.name,
            "age": user.age,
            "email": user.email
        })
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=e.errors())
    else:
        return {
            "message": "user added successfully",
            "user": users_db[-1]
        }


def main():
    uvicorn.run("main:app", reload=True)


if __name__ == "__main__":
    main()
