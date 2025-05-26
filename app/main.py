import json
from fastapi import FastAPI, HTTPException

app = FastAPI()

DATA_FILE = "fruits.json"

def load_data():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_data(fruits):
    with open(DATA_FILE, "w") as f:
        json.dump(fruits, f, indent=4)

@app.get("/fruits")
def get_all_fruits():
    return load_data()

@app.get("/fruits/{fruit_id}")
def get_fruit(fruit_id: int):
    fruits = load_data()
    for fruit in fruits:
        if fruit["id"] == fruit_id:
            return fruit
    raise HTTPException(status_code=404, detail="Fruit not found")

@app.post("/fruits")
def add_fruit(fruit: dict):
    fruits = load_data()
    fruit["id"] = len(fruits) + 1
    fruits.append(fruit)
    save_data(fruits)
    return fruit
