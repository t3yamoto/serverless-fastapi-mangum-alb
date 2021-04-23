from fastapi import FastAPI
from mangum import Mangum
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

@app.post("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return Item(name=item.name)


handler = Mangum(app)
