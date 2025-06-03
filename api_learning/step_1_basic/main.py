from pydantic import BaseModel
import uvicorn
from fastapi import FastAPI, HTTPException, Query

app = FastAPI()

items = [
    {
    "id": 1,
    "title": "item1",
    "disc": "disc1"
    },
    {
    "id": 2,
    "title": "item2",
    "disc": "disc2"
    }]


class ItemModel(BaseModel):
    title: str
    disc: str | None


@app.get("/")
def get_hi():
    return {"message": f"Hello, User!", "items": f"You have {len(items)} items"}

@app.post("/items/")
def post_item(item: ItemModel):
    items.append({
        "id": len(items) + 1, 
        "title": item.title, 
        "disc": item.disc
    })
    return {"message": "seccessfull"}

@app.get("/items/{item_id}")
def get_item_by_id(item_id: int) -> ItemModel:
    for i in items:
        if i["id"] == item_id:
            return ItemModel(title=i["title"], disc=i["disc"])
    raise HTTPException(status_code=404, detail="item not found")


@app.get("/items/title/{item_title}")
def get_item_id(item_title: str):
    for i in items:
        if i["title"] == item_title:
            return {"your_item_id": i["id"]}
    raise HTTPException(status_code=404, detail="Item not found")

def main():
    uvicorn.run("main:app", reload=True)


if __name__ == "__main__":
    main()
