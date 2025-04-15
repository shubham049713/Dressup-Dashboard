
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
uploaded_file = st.file_uploader("Upload your wardrobe Excel file", type=["xlsx"])

if uploaded_file:
    df = pd.read_excel(uploaded_file)

    st.title("👗 Dress Up! Interactive Wardrobe Dashboard")

    # Category Distribution
    st.subheader("Category Distribution")
    category_counts = df['Category'].value_counts()
    st.bar_chart(category_counts)

    # Color Distribution
    st.subheader("Color Distribution")
    color_counts = df['Color'].value_counts()
    st.bar_chart(color_counts)

    # Weather Fit Distribution
    st.subheader("Weather Fit Distribution")
    weather_counts = df['Weather Fit'].value_counts()
    st.bar_chart(weather_counts)

    # Occasion Distribution
    st.subheader("Occasion Distribution")
    occasion_counts = df['Occasion'].value_counts()
    st.bar_chart(occasion_counts)

    # Summary Insights
    st.subheader("📌 Summary Insights")
    insights = {
        "Top Category": category_counts.idxmax(),
        "Least Represented Category": category_counts.idxmin(),
        "Dominant Color": color_counts.idxmax(),
        "Weather Bias": weather_counts.idxmax(),
        "Most Frequent Occasion": occasion_counts.idxmax(),
        "Underrepresented Weather": weather_counts.idxmin(),
        "Underrepresented Occasion": occasion_counts.idxmin()
    }
    st.dataframe(pd.DataFrame.from_dict(insights, orient='index', columns=["Insight"]))
else:
    st.info("Please upload a wardrobe Excel file to begin.")
