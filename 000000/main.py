from fastapi import FastAPI
from pydantic import BaseModel  # ✅ 이 줄을 추가하세요

app = FastAPI()

@app.get("/hello")
def say_hello(name:str, age:int):
    return {"message" : f"hello, {name}!, age {age}"}

@app.get("/board")
def display():
    return {"body" : f"게시판"}

class Item(BaseModel):
    name : str
    price : float
    is_offer : bool = False

@app.post('/items/')
def create_item(item:Item):
    return {'received_item' : item}
