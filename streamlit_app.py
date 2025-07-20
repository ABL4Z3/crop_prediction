import streamlit as st
import requests

st.title("🌾 Smart Crop Recommender")

st.markdown("### Enter Soil and Weather Conditions Below")


with st.form("crop_form", clear_on_submit=False):
    col1, col2 = st.columns(2)

    with col1:
        Nitrogen = st.slider("Nitrogen (0–140)", 0, 140, 45)
        Potassium = st.slider("Potassium (5–145)", 5, 145, 50)
        Humidity = st.slider("Humidity (14%–100%)", 14.0, 100.0, 70.0)
        Rainfall = st.slider("Rainfall (103–300 mm)", 103.0, 300.0, 100.0)

    with col2:
        Phosphorus = st.slider("Phosphorus (5–145)", 5, 145, 30)
        Temperature = st.slider("Temperature (8°C–44°C)", 8.0, 44.0, 30.0)
        pH_Value = st.slider("pH Value (3–10)", 3.0, 10.0, 6.5)

    submitted = st.form_submit_button("🚀 Predict Crop Suitability")

    if submitted:
        input_payload = {
            "Nitrogen": Nitrogen,
            "Phosphorus": Phosphorus,
            "Potassium": Potassium,
            "Temperature": Temperature,
            "Humidity": Humidity,
            "pH_Value": pH_Value,
            "Rainfall": Rainfall,
        }

        try:
            response = requests.post("http://localhost:8000/predict", json=input_payload)
            if response.status_code == 200:
                result = response.json()
                st.success(f"Prediction: {result}")
            else:
                st.error(f"Failed with status {response.status_code}: {response.text}")
        except Exception as e:
            st.error(f"Error connecting to API: {str(e)}")
