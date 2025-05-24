from pydantic import BaseModel
import uvicorn
from fastapi import FastAPI

app = FastAPI()


class Item(BaseModel):
    id: int
    title: str
    disc: str | None


@app.get("/")
def get_hi():
    return {"message": "Hello, World!"}

@app.get("/items/item_id")
def get_item_id(item_id: int):
    return {"item_id": item_id}

@app.post("/items/")
def post_item(item: Item):
    return {
        "message": "seccessfull",
        "item": item
    }

def main():
    uvicorn.run("main:app", reload=True)

if __name__ == "__main__":
    main()
