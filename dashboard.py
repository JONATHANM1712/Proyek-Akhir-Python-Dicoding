import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="Dashboard Commercial Venue", layout="wide")
st.title("📊 Commercial Dashboard")
st.subheader("Kota dengan Jumlah Pesanan Terbanyak")

data = pd.read_csv("main_data.csv")

top_n = st.slider("Kota Yang Paling Bagus", min_value=7, max_value=len(data), value=12)

# Filter data
filtered = data.sort_values(by="total_orders", ascending=False).head(top_n)

# Plot bar chart
fig, ax = plt.subplots(figsize=(12, 7))
ax.bar(filtered["customer_city"], filtered["total_orders"], color="blue")
ax.set_title("Jumlah Pesanan Terbanyak")
ax.set_xlabel("Kota")
ax.set_ylabel("Jumlah Pesanan")
plt.xticks(rotation=60)
st.pyplot(fig)

# Ekspander: tampilkan data mentah
with st.expander("🔍Lihat Data Sebenarnya"):
    st.dataframe(filtered.reset_index(drop=True))
