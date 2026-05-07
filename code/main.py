from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/about")
async def about():
    return {
        "name": "shaza",
        "time": datetime.now()
    }

@app.get("/tuple")
async def tuple_example():
    coordinates: tuple[int, int] = (10, 20)

    return {
        "coordinates": coordinates
    }

@app.get("/set")
async def set_example():
    tags: set[str] = {"python", "fastapi", "python"}

    return {
        "tags": tags
    }

@app.post("/create")
async def create_item():
    return {"message": "Item created"}

@app.put("/update")
async def update_item():
    return {"message": "Item updated"}

@app.delete("/delete")
async def delete_item():
    return {"message": "Item deleted"}
