from fastapi import FastAPI

app = FastAPI()

inventory = {
    1: {
        "Name": "Milk",
        "price": 3.99,
        "Brand": "Arla"
    }

}

@app.get("/get_item/{item_id}")
def get_item(item_id: int):
    return inventory[item_id]
