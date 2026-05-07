from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/about")
async def about():
    return {
        "name": "Salsa",
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