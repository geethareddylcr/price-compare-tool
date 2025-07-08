# scrapers/croma.py
import requests
from bs4 import BeautifulSoup

def fetch_croma(query, country):
    if country.lower() != "in":
        return []

    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    search_url = f"https://www.croma.com/searchB?q={query.replace(' ', '%20')}"
    response = requests.get(search_url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    results = []
    items = soup.select(".product-item")

    for item in items:
        title = item.select_one(".product-title")
        price = item.select_one(".new-price")
        link = item.select_one("a")

        if title and price and link:
            price_text = price.text.replace("₹", "").replace(",", "").strip()
            try:
                price_value = float(price_text)
                results.append({
                    "productName": title.text.strip(),
                    "price": price_value,
                    "currency": "INR",
                    "link": "https://www.croma.com" + link["href"]
                })
            except:
                continue

    return results