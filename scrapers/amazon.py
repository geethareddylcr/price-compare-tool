import requests
from bs4 import BeautifulSoup

def fetch_amazon(query, country):
    base_url = "https://www.amazon.in" if country == "in" else "https://www.amazon.com"
    search_url = f"{base_url}/s?k={query.replace(' ', '+')}"
    headers = {"User-Agent": "Mozilla/5.0"}
    
    html = requests.get(search_url, headers=headers).text
    soup = BeautifulSoup(html, "html.parser")
    
    results = []
    for item in soup.select(".s-result-item"):
        title = item.select_one("h2 span")
        price_whole = item.select_one(".a-price-whole")
        price_fraction = item.select_one(".a-price-fraction")
        link = item.select_one("a.a-link-normal")

        if title and price_whole and link:
            price = float(price_whole.text.replace(",", "") + "." + (price_fraction.text if price_fraction else "00"))
            results.append({
                "productName": title.text.strip(),
                "price": price,
                "currency": "INR" if country == "in" else "USD",
                "link": base_url + link['href']
            })
    return results
