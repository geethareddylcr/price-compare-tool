from currency_converter import CurrencyConverter

cc = CurrencyConverter()

def convert_prices(results, target_currency):
    for r in results:
        if r["currency"] != target_currency:
            r["price"] = round(cc.convert(r["price"], r["currency"], target_currency), 2)
            r["currency"] = target_currency
    return results
