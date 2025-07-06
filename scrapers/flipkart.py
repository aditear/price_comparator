def get_flipkart_price(query: str) -> dict:
    return {
        "productName": f"{query} - Flipkart",
        "price": 81999,
        "currency": "INR",
        "link": "https://www.flipkart.com/search?q=" + query.replace(" ", "+")
    }