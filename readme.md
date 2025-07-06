# 📦 Product Price Comparator

This tool fetches and compares product prices from multiple e-commerce websites and displays them sorted in ascending order. It helps users find the best deal available based on their selected country.

---

## 🔧 Features
- Compare product prices from different sources.
- Country-specific pricing (currently supports US & India).
- Automatically ranks results by ascending price.
- Web UI built using Streamlit.

---

## 🧪 Sample Input
```json
{
  "country": "US",
  "query": "iPhone 16 Pro, 128GB"
}

## 📤 Sample Output (for query: {"country": "US", "query":"iPhone 16 Pro, 128GB"})
[
  {
    "link": "https://www.apple.com/shop/buy-iphone/iphone-16-pro",
    "price": 999,
    "currency": "USD",
    "productName": "Apple iPhone 16 Pro"
  },
  {
    "link": "https://www.bestbuy.com/site/searchpage.jsp?st=iphone+16+pro",
    "price": 1049,
    "currency": "USD",
    "productName": "Apple iPhone 16 Pro - BestBuy"
  }
]