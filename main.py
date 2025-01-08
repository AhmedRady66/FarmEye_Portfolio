import streamlit as st

# Sidebar
st.sidebar.title("Dashboard")
app_mode = st.sidebar.selectbox("Select Page", ["Home", "About", "Prediction"])

# Home Page
if(app_mode == "Home"):
    st.header("Fruits & Vegetables Recognition System")
    st.image("image\Fruits_Vegetables.jpg")

# About Page
elif(app_mode == "About"):
    st.header("About")
    st.subheader("About Dataset")
    st.text("This dataset encompasses images of various fruits and vegetables items:")
    st.code("Fruits: Banana, Apple, Pear, Grapes, Orange, Kiwi, Watermelon, Pomegranate, Pineapple, Mango")
    st.code("Vegetables: Cucumber, Carrot, Capsicum, Onion, Potato, Lemon, Tomato, Radish, Beetroot, Cabbage, Lettuce, Spinach, Soybean, Cauliflower, Bell Pepper, Chilli Pepper, Turnip, Corn, Sweetcorn, Sweet Potato, Paprika, Jalapeño, Ginger, Garlic, Peas, Eggplant")
    st.subheader("Content")
    st.text("The dataset is organized into three main folders:")
    st.text("1. Train: Contains 100 images per category.")
    st.text("2. Test: Contains 10 images per category.")
    st.text("3. Validation: Contains 10 images per category.")
    