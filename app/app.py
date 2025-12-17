import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load trained model
model = joblib.load("../models/random_forest_model.pkl")


st.set_page_config(page_title="Solar Power Prediction", layout="centered")

st.title("🔆 Solar Power Production Prediction")
st.markdown("""
Aplikasi ini digunakan untuk memprediksi **produksi energi listrik panel surya**
berdasarkan kondisi lingkungan menggunakan **Random Forest Regression**.
""")


st.subheader("📥 Masukkan Kondisi Lingkungan")

windspeed = st.number_input("Wind Speed (m/s)", min_value=0.0, value=1.5)
sunshine = st.number_input("Sunshine Duration (minutes)", min_value=0.0, value=60.0)
air_pressure = st.number_input("Air Pressure (hPa)", value=1010.0)
radiation = st.number_input("Solar Radiation (W/m²)", min_value=0.0, value=200.0)
air_temp = st.number_input("Air Temperature (°C)", value=25.0)
humidity = st.number_input("Relative Air Humidity (%)", min_value=0.0, max_value=100.0, value=70.0)


input_data = pd.DataFrame({
    "WindSpeed": [windspeed],
    "Sunshine": [sunshine],
    "AirPressure": [air_pressure],
    "Radiation": [radiation],
    "AirTemperature": [air_temp],
    "RelativeAirHumidity": [humidity]
})

if st.button("🔮 Predict Energy Production"):
    prediction = model.predict(input_data)[0]

    st.success(f"⚡ Predicted System Production: **{prediction:.2f} kWh**")