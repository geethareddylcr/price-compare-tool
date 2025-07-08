# scrapers/flipkart.py
import requests
from bs4 import BeautifulSoup

def fetch_flipkart(query, country):
    if country.lower() != "in":
        return []

    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    search_url = f"https://www.flipkart.com/search?q={query.replace(' ', '+')}"
    response = requests.get(search_url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    results = []
    items = soup.select("._1AtVbE")  # Each product block

    for item in items:
        title = item.select_one("._4rR01T") or item.select_one(".s1Q9rs")
        price = item.select_one("._30jeq3")
        link = item.select_one("a._1fQZEK") or item.select_one("a.s1Q9rs")

        if title and price and link:
            price_text = price.text.replace("₹", "").replace(",", "").strip()
            try:
                price_value = float(price_text)
                results.append({
                    "productName": title.text.strip(),
                    "price": price_value,
                    "currency": "INR",
                    "link": "https://www.flipkart.com" + link["href"]
                })
            except:
                continue

    return results
