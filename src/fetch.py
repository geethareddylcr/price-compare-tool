from scrapers.amazon import fetch_amazon
from scrapers.flipkart import fetch_flipkart
from scrapers.croma import fetch_croma
from scrapers.walmart import fetch_walmart

def fetch_product_prices(query: str, country: str) -> list:
    all_results = []

    all_results += fetch_amazon(query, country)
    all_results += fetch_flipkart(query, country)
    all_results += fetch_croma(query, country)

    print(f"Raw Results: {all_results}")  # <-- Add this for debugging

    if not all_results:
        return []  # early exit

    from ai.matcher import ai_match
    from utils.currency import convert_prices
    from utils.sorter import sort_by_price

    matched = ai_match(query, all_results)
    converted = convert_prices(matched, "USD")
    return sort_by_price(converted)

