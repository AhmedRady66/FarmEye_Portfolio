import streamlit as st

# Sidebar
st.sidebar.title("Dashboard")
app_mode = st.sidebar.selectbox("Select Page", ["Home", "About", "Prediction"])

# Home Page
if(app_mode == "Home"):
    st.header("Fruits & Vegetables Recognition System")
    st.image("image\Fruits_Vegetables.jpg")