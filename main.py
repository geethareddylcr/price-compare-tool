from fastapi import FastAPI, Request
from src.fetch import fetch_product_prices

app = FastAPI()

@app.get("/compare")
def compare(country: str, query: str):
    return fetch_product_prices(query, country)
@app.get("/")
def read_root():
    return {"message": "Welcome to the Price Compare Tool"}

