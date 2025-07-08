# scrapers/walmart.py
import requests
from bs4 import BeautifulSoup

def fetch_walmart(query, country):
    if country.lower() != "us":
        return []

    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    search_url = f"https://www.walmart.com/search?q={query.replace(' ', '+')}"
    response = requests.get(search_url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    results = []
    items = soup.select("div.mb1.ph1.pa0-xl.bb.b--near-white.w-25")  # Try fallback selector if empty

    for item in items:
        title = item.select_one("a.lh-title")
        price_whole = item.select_one("span.price-main .visuallyhidden")
        link = item.select_one("a")

        if title and price_whole and link:
            try:
                price_value = float(price_whole.text.replace("$", "").strip())
                results.append({
                    "productName": title.text.strip(),
                    "price": price_value,
                    "currency": "USD",
                    "link": "https://www.walmart.com" + link["href"]
                })
            except:
                continue

    return results
