Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import pandas as pd
... import streamlit as st
... import matplotlib.pyplot as plt
... 
... # Load data
... data = pd.read_csv("main_data.csv")
... 
... st.title("E-Commerce Dashboard - Top Cities by Orders")
... 
... # Slider
... top_n = st.slider("Tampilkan Top N Kota", 5, 20, 10)
... 
... # Filter
... filtered = data.sort_values(by="total_orders", ascending=False).head(top_n)
... 
... # Visualisasi
... fig, ax = plt.subplots()
... ax.bar(filtered["customer_city"], filtered["total_orders"], color="skyblue")
... ax.set_title("Top Cities by Total Orders")
... ax.set_xlabel("Kota")
... ax.set_ylabel("Jumlah Pesanan")
... plt.xticks(rotation=45)
... st.pyplot(fig)
... 
... # Data mentah
... with st.expander("Lihat data mentah"):
...     st.dataframe(filtered)
