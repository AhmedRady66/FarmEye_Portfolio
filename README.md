# Fruits and Vegetables Recognition System

Welcome to the **Fruits & Vegetables Recognition System**, a user-friendly web application powered by AI to identify fruits and vegetables with precision. This application uses advanced image processing and machine learning techniques to classify produce effectively.

---

## 🌟 Features

- **User-friendly Interface**: Easily navigate through the application with a clean and intuitive design.
- **AI-Powered Predictions**: Accurately classify fruits and vegetables using a trained deep learning model.
- **Informative Dashboard**: Learn about the project's functionality and dataset details.

---

## 🚀 How It Works

1. **Upload an Image**: Select an image of a fruit or vegetable from your device.
2. **Model Prediction**: The app uses a trained TensorFlow model to process the image and predict the category.
3. **View Results**: Instantly get the prediction along with the corresponding label.

---

## 🛠️ Technologies Used

- **Frontend**: [Streamlit](https://streamlit.io/) for building the web application.
- **Backend**: TensorFlow for deep learning model training and inference.
- **Programming Language**: Python
- **Dataset**: A comprehensive collection of labeled images of fruits and vegetables.

---

## 📂 Dataset Details

The dataset includes images of fruits and vegetables captured in diverse conditions for robust training. 

### Categories
#### Fruits:
`Banana, Apple, Pear, Grapes, Orange, Kiwi, Watermelon, Pomegranate, Pineapple, Mango`

#### Vegetables:
`Cucumber, Carrot, Capsicum, Onion, Potato, Lemon, Tomato, Radish, Beetroot, Cabbage, Lettuce, Spinach, Soybean, Cauliflower, Bell Pepper, Chilli Pepper, Turnip, Corn, Sweetcorn, Sweet Potato, Paprika, Jalapeño, Ginger, Garlic, Peas, Eggplant`

### Dataset Structure
- **Train**: 100 images per category for training the model.
- **Test**: 10 images per category for evaluating the model.
- **Validation**: 10 images per category for fine-tuning.

---

## 🔧 Installation Guide

Follow these steps to set up the project locally:

1. Clone the repository:

   ```bash
   git clone https://github.com/AhmedRady66/FarmEye_Portfolio
   cd main.py
2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
3. Run the application:

   ```bash
   streamlit run app.py
4. Open the app in your browser at http://localhost:8501.

---
## 📑 File Structure

- `app.py`: Main application file for Streamlit.
- `training_model.h5`: Pre-trained TensorFlow model.
- `label.txt`: List of labels for predictions.
- `image/`: Contains images used for the interface.
- `requirements.txt`: List of dependencies.

---

## 📚 How to Use

1. Navigate to the **Prediction** tab.
2. Upload an image of a fruit or vegetable.
3. Click **Predict** to get the results.

---

## 🌟 Acknowledgements

- TensorFlow for the powerful machine learning framework.
- Streamlit for the seamless web app development platform.
