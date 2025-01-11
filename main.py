import streamlit as st

# Sidebar Navigation
st.sidebar.title("Dashboard")
app_mode = st.sidebar.selectbox("Navigate to", ["Home", "About", "Prediction"])

# Home Page
if (app_mode == "Home"):
    st.header("Fruits & Vegetables Recognition System")
    st.image("image/Fruits_Vegetables.jpg", caption="Empowering Food Recognition with AI", use_column_width=True)
    st.markdown(
        """
        Welcome to the **Fruits & Vegetables Recognition System**, a user-friendly tool powered by AI to identify 
        fruits and vegetables with precision. This application uses advanced image processing techniques to 
        help you quickly and accurately classify a wide variety of produce.
        """
    )
    st.markdown("Navigate through the sidebar to learn more about the project or try out the prediction feature!")

# About Page
elif (app_mode == "About"):
    st.title("About the Project")
    st.subheader("Project Overview")
    st.markdown(
        """
        The **Fruits & Vegetables Recognition System** leverages a comprehensive dataset of images 
        representing a wide array of fruits and vegetables. It is designed to assist in quick and efficient 
        classification, making it a valuable tool for various applications, including:
        - Automated grocery checkout systems
        - Dietary tracking apps
        - Educational tools for children
        """
    )

    st.subheader("About the Dataset")
    st.markdown(
        """
        This dataset includes images of **fruits** and **vegetables** in diverse conditions, ensuring robust 
        model training and accurate predictions. Here are the key details:
        """
    )
    st.markdown("### Categories:")
    st.markdown("#### Fruits:")
    st.code("Banana, Apple, Pear, Grapes, Orange, Kiwi, Watermelon, Pomegranate, Pineapple, Mango")
    st.markdown("#### Vegetables:")
    st.code(
        "Cucumber, Carrot, Capsicum, Onion, Potato, Lemon, Tomato, Radish, Beetroot, Cabbage, "
        "Lettuce, Spinach, Soybean, Cauliflower, Bell Pepper, Chilli Pepper, Turnip, Corn, Sweetcorn, "
        "Sweet Potato, Paprika, Jalapeño, Ginger, Garlic, Peas, Eggplant"
    )

    st.subheader("Dataset Content")
    st.markdown(
        """
        The dataset is structured into three main folders to facilitate efficient training and evaluation:
        - **Train**: Contains 100 images per category, used to train the model.
        - **Test**: Contains 10 images per category, used to evaluate model performance.
        - **Validation**: Contains 10 images per category, used to fine-tune the model.
        """
    )

    st.info("Explore the 'Prediction' page to see the model in action!")

# Prediction Page
elif(app_mode == "Prediction"):
    st.header("Prediction Model")
    test_image = st.file_uploader("Choose an Image")
    if(st.button("Show Image")):
        st.image(test_image)
