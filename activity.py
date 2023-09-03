import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import requests
import datetime

# Define Fitbit API credentials
CLIENT_ID = 'YOUR_CLIENT_ID'
CLIENT_SECRET = 'YOUR_CLIENT_SECRET'
USER_ID = 'YOUR_USER_ID'  # You need to replace this with the Fitbit user's ID
BASE_URL = 'https://api.fitbit.com/1/'

# Fitbit API endpoints
ACTIVITY_ENDPOINT = f'user/{USER_ID}/activities/active-zone-minutes/date/'
CALORIES_ENDPOINT = f'user/{USER_ID}/activities/calories/date/'
VO2_MAX_ENDPOINT = f'user/{USER_ID}/activities/vo2Max/date/'

# Streamlit app
st.title("Fitbit Data Analysis")

# Input fields for date and period
date = st.date_input("Select a date for the past week:")
period = st.radio("Select a period:", ["1d", "7d"])  # 1d for daily data, 7d for weekly data

# Calculate the start date for the API request
end_date = date
start_date = end_date - datetime.timedelta(days=6) if period == "7d" else end_date

# Format the date strings for the API request
start_date_str = start_date.strftime("%Y-%m-%d")
end_date_str = end_date.strftime("%Y-%m-%d")

# Make API requests to Fitbit
response_active_zone = requests.get(BASE_URL + ACTIVITY_ENDPOINT + f'{start_date_str}/{end_date_str}.json', headers={"Authorization": f"Bearer {ACCESS_TOKEN}"})
response_calories = requests.get(BASE_URL + CALORIES_ENDPOINT + f'{start_date_str}/{end_date_str}.json', headers={"Authorization": f"Bearer {ACCESS_TOKEN}"})
response_vo2_max = requests.get(BASE_URL + VO2_MAX_ENDPOINT + f'{start_date_str}/{end_date_str}.json', headers={"Authorization": f"Bearer {ACCESS_TOKEN}"})

# Process and display the data
if response_active_zone.status_code == 200 and response_calories.status_code == 200 and response_vo2_max.status_code == 200:
    active_zone_data = response_active_zone.json()["activities-activeZoneMinutes"]
    calories_data = response_calories.json()["activities-calories"]
    vo2_max_data = response_vo2_max.json()["activities-vo2Max"]

    # Convert the data to a DataFrame
    df_active_zone = pd.DataFrame(active_zone_data)
    df_calories = pd.DataFrame(calories_data)
    df_vo2_max = pd.DataFrame(vo2_max_data)

    # Create a Matplotlib figure to display the data
    fig, axs = plt.subplots(3, 1, figsize=(10, 12))

    # Plot Active Zone Minutes
    axs[0].plot(df_active_zone['dateTime'], df_active_zone['value'], marker='o', linestyle='-', color='b')
    axs[0].set_title('Active Zone Minutes')
    axs[0].set_xlabel('Date')
    axs[0].set_ylabel('Minutes')

    # Plot Calories Burnt
    axs[1].plot(df_calories['dateTime'], df_calories['value'], marker='o', linestyle='-', color='g')
    axs[1].set_title('Calories Burnt')
    axs[1].set_xlabel('Date')
    axs[1].set_ylabel('Calories')

    # Plot VO2 Max
    axs[2].plot(df_vo2_max['dateTime'], df_vo2_max['value'], marker='o', linestyle='-', color='r')
    axs[2].set_title('VO2 Max')
    axs[2].set_xlabel('Date')
    axs[2].set_ylabel('VO2 Max')

    st.pyplot(fig)
else:
    st.error("Error fetching Fitbit data. Please check your credentials and try again.")
