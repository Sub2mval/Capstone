import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import datetime

# Create a dataframe to store user data
data = pd.DataFrame(columns=["Name", "Birthday", "Weight"])

# Streamlit app
st.title("Weight vs. Age Tracker")

# Input fields for user data
name = st.text_input("Enter Your Name:")
birthday = st.date_input("Enter Your Birthday:")
weight = st.number_input("Enter Your Weight (kg):")

if st.button("Submit"):
    # Calculate age based on birthday
    today = datetime.date.today()
    age = today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))

    # Add data to the dataframe
    data = data.append({"Name": name, "Birthday": birthday, "Weight": weight}, ignore_index=True)

    # Display user data
    st.write(f"Name: {name}")
    st.write(f"Age: {age} years")
    st.write(f"Weight: {weight} kg")

    # Create a weight vs. age graph
    fig, ax = plt.subplots()
    ax.plot(data["Birthday"], data["Weight"], marker='o', linestyle='-')
    ax.set_xlabel("Birthday")
    ax.set_ylabel("Weight (kg)")
    ax.set_title("Weight vs. Age")
    st.pyplot(fig)
