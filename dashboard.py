import pandas as pandas
import streamlit as streamlit
import matplotlib.pyplot as plt

st.set_page_config(page_title = "Dashboard Commerical Venue", layout="left")
st.title("Commercial Dashboard🗞")
st.subheader("Kota Yang Pesanan Jumlah Banyak")

data = pd.read_csv("main_data.csv")

top_n = st.slider("Tampilkan Kota Meriah"), min_value=7, max_value=len(data), value=12)

filtered = data.sort_values(by="total_orders", ascending=False).

fig, ax = plt.subplots(figsize=(12,7))
ax.bar(filtered["customer_city"], filtered["total_orders"], color="yellow"
ax.set_title ("Kota Yang Pesnan Jumlah Banyak")
ax.set_xlabel ("Kota")
ax.set_ylabel ("Jumlah Pesanan")
plt.xticks(rotation=45)
st.pyplot(fig)

with st.expander("🔍Fitur Data Netral")
    st.dataframe(filtered.reset_index(drop=True))
