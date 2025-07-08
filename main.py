from fastapi import FastAPI, Request
from src.fetch import fetch_product_prices

app = FastAPI()

@app.get("/compare")
def compare(country: str, query: str):
    return fetch_product_prices(query, country)

