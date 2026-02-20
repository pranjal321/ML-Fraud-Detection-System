import streamlit as st
import numpy as np
import joblib

model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")

def risk_decision(score):
    if score > 0.8:
        return "HIGH RISK – CANCEL"
    elif score > 0.5:
        return "SUSPICIOUS – VERIFY ID"
    else:
        return "LEGIT – APPROVE"

st.title("ML Fraud Detection Demo")
st.write("Enter order details to get fraud risk score and recommendation")

amount = st.number_input(
    "Order Amount",
    min_value=0.0,
    value=500.0,
    step=50.0
)

is_first_time_buyer = st.selectbox(
    "First Time Buyer?",
    [0, 1]
)

country_mismatch = st.selectbox(
    "Billing / Shipping Country Mismatch?",
    [0, 1]
)

avs_failed = st.selectbox(
    "AVS Failed?",
    [0, 1]
)

cvv_failed = st.selectbox(
    "CVV Failed?",
    [0, 1]
)

num_orders_last_7_days = st.slider(
    "Number of Orders in Last 7 Days",
    min_value=0,
    max_value=10,
    value=1
)

high_velocity = 1 if num_orders_last_7_days >= 4 else 0

if st.button("Predict Fraud Risk"):
    log_amount = np.log1p(amount)

    X = np.array([[
        log_amount,
        is_first_time_buyer,
        country_mismatch,
        avs_failed,
        cvv_failed,
        high_velocity,
        num_orders_last_7_days
    ]])

    X_scaled = scaler.transform(X)
    score = model.predict_proba(X_scaled)[0][1]

    st.metric("Fraud Score", round(float(score), 2))
    st.success(f"Decision: {risk_decision(score)}")

    st.caption(f"Feature vector shape: {X.shape}")