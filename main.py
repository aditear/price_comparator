from scrapers.apple import get_apple_price
from scrapers.bestbuy import get_bestbuy_price 

def fetch_prices(query: str, country: str):
    prices = []

    country = country.strip().lower()

    if country == "us":
        prices.append(get_apple_price(query))
        prices.append(get_bestbuy_price(query))
    else:
        print(f"❌ Sorry, country '{country}' not supported yet.\n")
        return []

    return sorted(prices, key=lambda x: x["price"])

if __name__ == "__main__":
    print("🛒 Product Price Comparator\n")

    query = input("🔍 Enter product name: ")
    country = input("🌍 Enter country (e.g., US): ")

    print("\n📡 Fetching prices...\n")
    results = fetch_prices(query, country)

    if results:
        print("✅ Sorted Price Results:\n")
        for item in results:
            print(f"📦 {item['productName']}")
            print(f"💰 Price: {item['price']} {item['currency']}")
            print(f"🔗 Link: {item['link']}\n")
    else:
        print("⚠ No results found.")