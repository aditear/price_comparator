import streamlit as st
from scrapers.apple import get_apple_price
from scrapers.bestbuy import get_bestbuy_price
from scrapers.flipkart import get_flipkart_price

st.set_page_config(page_title="Product Price Comparator", layout="wide")
st.title("📦 Product Price Comparison Tool")

query = st.text_input("Enter Product Name (e.g., iPhone 16 Pro, 128GB)")
countries = st.multiselect("Select countries to compare", ["US", "India"], default=["US"])

if st.button("Compare Prices") and query and countries:
    with st.spinner("🔎 Fetching prices..."):
        all_prices = []

        if "US" in countries:
            try:
                apple_price = get_apple_price(query)
                apple_price["source"] = "Apple (US)"
                all_prices.append(apple_price)

                bestbuy_price = get_bestbuy_price(query)
                bestbuy_price["source"] = "BestBuy (US)"
                all_prices.append(bestbuy_price)
            except:
                st.warning("Could not fetch US prices.")

        if "India" in countries:
            try:
                flipkart_price = get_flipkart_price(query)
                flipkart_price["source"] = "Flipkart (India)"
                all_prices.append(flipkart_price)
            except:
                st.warning("Could not fetch India prices.")

        # Sort all_prices by price
        try:
            sorted_prices = sorted(all_prices, key=lambda x: x["price"])
        except:
            sorted_prices = all_prices  # Fallback

        # Show results
        st.subheader("📊 Price Comparison (Lowest to Highest)")
        for item in sorted_prices:
            st.write(f"🔹 {item['source']}: {item['price']} {item['currency']} — [View]({item['link']})")