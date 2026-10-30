import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("insurance_model.pkl")

st.set_page_config(
    page_title="Insurance Cost Predictor",
    page_icon="💰",
    layout="centered"
)

st.title("💰 Insurance Cost Predictor")
st.write("Predict your medical insurance charges using Machine Learning.")

st.subheader("Customer Information")

age = st.number_input("Age", min_value=18, max_value=100, value=25)

sex = st.selectbox("Gender", ["male", "female"])

bmi = st.number_input(
    "BMI",
    min_value=10.0,
    max_value=60.0,
    value=24.5
)

children = st.number_input(
    "Number of Children",
    min_value=0,
    max_value=10,
    value=0
)

smoker = st.selectbox("Smoker", ["yes", "no"])

region = st.selectbox(
    "Region",
    ["southwest", "southeast", "northwest", "northeast"]
)

if st.button("Predict Insurance Cost"):

    customer = pd.DataFrame([{
        "age": age,
        "sex": sex,
        "bmi": bmi,
        "children": children,
        "smoker": smoker,
        "region": region
    }])

    prediction = model.predict(customer)

    st.success(
        f"Estimated Insurance Charges: ${prediction[0]:,.2f}"
    )