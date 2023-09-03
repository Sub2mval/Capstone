import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import requests
import joblib
import datetime

# Define Fitbit API credentials
CLIENT_ID = 'YOUR_CLIENT_ID'
CLIENT_SECRET = 'YOUR_CLIENT_SECRET'
USER_ID = 'YOUR_USER_ID'  # You need to replace this with the Fitbit user's ID
BASE_URL = 'https://api.fitbit.com/1/'

# Fitbit API endpoints
HRV_ENDPOINT = f'user/{USER_ID}/activities/heart/date/'
HRV_PERIOD = '1m'  # 1 minute data, you can adjust as needed

# Load the pickled logistic regression model
model = joblib.load('finalized_model.sav')

# Streamlit app
st.title("Heart Disease Risk Assessment")

# Input field for serum cholesterol
serum_cholesterol = st.number_input("Enter Your Serum Cholesterol (mg/dl):")

# Input field for fasting blood sugar
fasting_blood_sugar = st.number_input("Enter Your Fasting Blood Sugar (mg/dl):")

# Calculate heart disease probability
heart_disease_probability = model.predict_proba([[serum_cholesterol, fasting_blood_sugar]])[:, 1][0]

# Report fasting blood sugar status
blood_sugar_status = "Normal" if fasting_blood_sugar <= 120 else "High"

# Display results
st.write(f"Serum Cholesterol: {serum_cholesterol} mg/dl")
st.write(f"Fasting Blood Sugar: {fasting_blood_sugar} mg/dl (Status: {blood_sugar_status})")
st.write(f"Heart Disease Probability: {heart_disease_probability:.2f}")

# Fetch HRV data from Fitbit
response_hrv = requests.get(BASE_URL + HRV_ENDPOINT + f'{datetime.date.today()}.json', headers={"Authorization": f"Bearer {ACCESS_TOKEN}"})

if response_hrv.status_code == 200:
    hrv_data = response_hrv.json()["activities-heart-intraday"]["dataset"]

    # Create a DataFrame for HRV data
    df_hrv = pd.DataFrame(hrv_data)
    df_hrv['time'] = pd.to_datetime(df_hrv['time'])
    df_hrv.set_index('time', inplace=True)

    # Plot HRV data
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(df_hrv.index, df_hrv['value'], marker='o', linestyle='-', color='b')
    ax.set_title('Heart Rate Variability (HRV) Data')
    ax.set_xlabel('Time')
    ax.set_ylabel('HRV')
    st.pyplot(fig)
else:
    st.error("Error fetching HRV data from Fitbit. Please check your credentials and try again.")
