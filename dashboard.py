import streamlit as st
import pandas as pd
import requests
import matplotlib.pyplot as plt
import seaborn as sns

# Set page config
st.set_page_config(page_title="Crypto Dashboard", layout="wide")

# Title
st.title("📊 Top 10 Cryptocurrencies by Market Cap")

# Fetch data
url = "https://api.coingecko.com/api/v3/coins/markets"
params = {
    'vs_currency': 'usd',
    'order': 'market_cap_desc',
    'per_page': 10,
    'page': 1,
    'sparkline': False
}
response = requests.get(url, params=params)
data = response.json()
df = pd.DataFrame(data)

# Display Data
st.subheader("📋 Data Table")
st.dataframe(df[['name', 'symbol', 'current_price', 'market_cap', 'price_change_percentage_24h']])

# Bar Chart: Market Cap
st.subheader("📈 Market Cap of Top 10 Cryptocurrencies")
fig1, ax1 = plt.subplots(figsize=(10, 5))
sns.barplot(data=df, x='market_cap', y='name', ax=ax1)
ax1.set_title("Top 10 Cryptocurrencies by Market Cap")
ax1.set_xlabel("Market Cap (USD)")
ax1.set_ylabel("Cryptocurrency")
st.pyplot(fig1)

# Line Chart: Price Changes
st.subheader("📉 Price Change (24h) of Top 10 Cryptos")
fig2, ax2 = plt.subplots(figsize=(10, 5))
sns.barplot(data=df, x='price_change_percentage_24h', y='name', ax=ax2, palette='coolwarm')
ax2.set_title("24h Price Change Percentage")
ax2.set_xlabel("Change (%)")
ax2.set_ylabel("Cryptocurrency")
st.pyplot(fig2)

# Heatmap: Correlation Matrix
st.subheader("🔍 Correlation Between Key Numeric Features")

# Filter only numeric columns relevant to correlation
numeric_df = df[['current_price', 'market_cap', 'price_change_percentage_24h']]
corr = numeric_df.corr().round(2)

fig3, ax3 = plt.subplots(figsize=(6, 4))
sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax3)
st.pyplot(fig3)
