import streamlit as st
import pandas as pd

# 1. Set the page tab title and layout width
st.set_page_config(page_title="Reputation Monitor", layout="wide")

# 2. Display a big main title on the website
st.title("📱 TechNova X1 - Social Media Reputation Monitor")
st.write("Welcome to our Big Data Analytics dashboard! Below is our initial social media dataset.")

# 3. Load and display our dataset
try:
    # Read the CSV file we created earlier
    df = pd.read_csv("social_media_data.csv")
    
    # Show the table on the website
    st.subheader("Raw Dataset Preview")
    st.dataframe(df)
    
except Exception as e:
    st.error("Could not find the dataset file. Please make sure the name is correct!")
