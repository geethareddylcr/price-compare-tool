import requests
from bs4 import BeautifulSoup

def fetch_flipkart(query, country=None):
    url = f"https://www.flipkart.com/search?q={query}"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print("Failed to fetch Flipkart page.")
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    products = soup.select("._1AtVbE")

    results = []
    for product in products:
        name = product.select_one("._4rR01T")
        price = product.select_one("._30jeq3")
        link = product.select_one("a")

        if name and price and link:
            results.append({
                "productName": name.text.strip(),
                "price": price.text.strip().replace("₹", "").replace(",", ""),
                "currency": "INR",
                "link": "https://www.flipkart.com" + link['href']
            })

    print("Flipkart results:", results)
    return results
