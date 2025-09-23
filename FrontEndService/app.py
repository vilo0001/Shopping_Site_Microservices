import requests
import streamlit as st

products = requests.get("http://localhost:5004/products").json()
categories = set()
for product in products:
    categories.add(product["category"])

st.set_page_config(page_title="Webshop Microservices", page_icon="😎")

st.title("Webshop Microservices")

st.selectbox(label = "Category", options=categories, key="categoryFilter")

productContainer = st.container(border = True)
with productContainer:
    col1, col2, col3 = st.columns(3)
productColumns = [col1, col2, col3]

columnIndex = 0
for product in products:
    with productContainer:
        with productColumns[columnIndex]:
            with st.container(border=True, height=300, key=str(product["id"])):
                st.image(product["images"][0])
                st.write(product["title"])
                with st.container(vertical_alignment="center", horizontal=True, horizontal_alignment="distribute"):
                    st.write(f"${product["price"]}")
                    st.button("🛒", key=f"button_{str(product["id"])}")
            if(columnIndex == 2):
                columnIndex = 0
            else:
                columnIndex += 1