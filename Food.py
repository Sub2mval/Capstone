import streamlit as st
import pandas as pd
import requests

# Streamlit app
st.title("Food Diary")

# Create a button to add a food item
if st.button("Add Food Item"):
    food_name = st.text_input("Enter the Food Name:")
    food_quantity = st.number_input("Enter the Quantity (grams):")
    
    if food_name and food_quantity:
        st.write(f"Added: {food_quantity}g of {food_name}")
        
        # TODO: Call the OpenFoodFacts API to get nutritional data for the entered food item
        # You'll need to parse the API response to retrieve calorie and macronutrient information.
        # For this example, we'll use placeholder values.

# Create a button to calculate totals
if st.button("Calculate Totals"):
    # TODO: Calculate calorie and macronutrient totals based on the added food items.
    # You'll need to loop through the added items and aggregate the nutritional values.
    # For this example, we'll use placeholder values.

    total_calories = 0  # Placeholder for total calories
    total_protein = 0   # Placeholder for total protein (in grams)
    total_carbs = 0     # Placeholder for total carbohydrates (in grams)
    total_fat = 0       # Placeholder for total fat (in grams)

    st.write(f"Total Calories: {total_calories} kcal")
    st.write(f"Total Protein: {total_protein} g")
    st.write(f"Total Carbohydrates: {total_carbs} g")
    st.write(f"Total Fat: {total_fat} g")

    # TODO: Check if any of the added foods contain sugar or vegetable oil
    # If found, display an inflammation risk message.
    # For this example, we'll use placeholder values.

    inflammation_risk = False  # Placeholder for inflammation risk message

    if inflammation_risk:
        st.error("Warning: Some foods contain ingredients that may increase inflammation.")

# Reset button to clear the diary
if st.button("Clear Diary"):
    # TODO: Clear the added food items and reset the totals
    pass
