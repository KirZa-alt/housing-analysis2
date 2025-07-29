import pandas as pd
import streamlit as st
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

import os
st.title("Housing Data")
file_path = r"C:\Users\acer\Documents\kiran-python\ass\Housing.csv"
data = pd.read_csv(file_path)
st.write(data)

st.title("Explore and Clean Data:")
st.write("First 5 Rows and Columns:",data.head())
st.write("Description of data",data.describe())

st.title("Check and handle missing value")
st.write("checking of null values:",data.isnull().sum())
st.write("There is no null value in data")

st.title("Compute Statistics")
st.header("Price:")
opt=st.selectbox("Select the column which u want to Explore:",
             ["Price","Area","Bedrooms"])

if st.button("Apply"):
    if opt=="Price":
# Mean
        st.write("Average(Mean) of price:",data["price"].mean())
        st.write("Middle Value(Median) of price:",data["price"].median())
        st.write("Most Frequent Value(Mode) of price:",data["price"].mode())
        st.write("Maximum value in price is:",np.max(data["price"]))
        st.write("Minimum value in price is:",np.min(data["price"]))
        st.write("Standard deviation of price is:", data["price"].std())
        st.write("Skewness of price is:", data["price"].skew())
        st.write("Variance of price is:", data["price"].var())

        st.subheader("Histogram of Price")
        fig1, ax1 = plt.subplots()
        sns.histplot(data["price"], bins=30, kde=True, color='skyblue', ax=ax1)
        st.pyplot(fig1)

        # Boxplot
        st.subheader("Box Plot of Price")
        fig2, ax2 = plt.subplots()
        sns.boxplot(x=data["price"], color='orange', ax=ax2)
        st.pyplot(fig2)
    elif opt=="Area":
        st.write("Average(Mean) of area:",data["area"].mean())
        st.write("Middle Value(Median) of area:",data["area"].median())
        st.write("Most Frequent Value(Mode) of area:",data["area"].mode())
        st.write("Maximum value in area is:",np.max(data["area"]))
        st.write("Minimum value in area is:",np.min(data["area"]))
        st.write("Standard deviation of area is:", data["area"].std())
        st.write("Skewness of area is:", data["area"].skew())
        st.write("Variance of area is:", data["area"].var())

        st.subheader("Histogram of Area")
        fig1, ax1 = plt.subplots()
        sns.histplot(data["price"], bins=30, kde=True, color='skyblue', ax=ax1)
        st.pyplot(fig1)

        # Boxplot
        st.subheader("Box Plot of Area")
        fig2, ax2 = plt.subplots()
        sns.boxplot(x=data["price"], color='orange', ax=ax2)
        st.pyplot(fig2)

    elif opt=="Bedrooms":
        st.write("Average(Mean) of bedrooms:",data["bedrooms"].mean())
        st.write("Middle Value(Median) of bedrooms:",data["bedrooms"].median())
        st.write("Most Frequent Value(Mode) of bedrooms:",data["bedrooms"].mode())
        st.write("Maximum value in bedrooms is:",np.max(data["bedrooms"]))
        st.write("Minimum value in bedrooms is:",np.min(data["bedrooms"]))
        st.write("Standard deviation of bedrooms is:", data["bedrooms"].std())
        st.write("Skewness of bedrooms is:", data["bedrooms"].skew())
        st.write("Variance of bedrooms is:", data["bedrooms"].var())

        st.subheader("Histogram of Bedrooms")
        fig1, ax1 = plt.subplots()
        sns.histplot(data["price"], bins=30, kde=True, color='skyblue', ax=ax1)
        st.pyplot(fig1)

        # Boxplot
        st.subheader("Box Plot of Bedrooms")
        fig2, ax2 = plt.subplots()
        sns.boxplot(x=data["price"], color='orange', ax=ax2)
        st.pyplot(fig2)
if st.button("Get Summary"):
        st.title("Insights Summary")
        st.markdown("""
            I analyzed a housing dataset that included price, area, and number of bedrooms.
             The average home price was moderate, but the wide spread
             and high standard deviation showed major variability, 
            suggesting a mix of affordable and premium properties.
             The distribution of prices was right-skewed, meaning a 
            few very expensive homes pulled the average upward. Similarly,
             area values varied significantly, with some compact homes and
             some spacious ones, and several outliers suggesting either 
            luxury homes or unusually small properties. Most houses had 
            between 2 and 4 bedrooms, indicating a family-oriented market. 
            Some surprises were found in the form of large-area homes priced
             relatively low, possibly due to location disadvantages or
             condition issues. The data shows a market with considerable
             diversity — not just in size and price, but likely in quality
             and location too. This variability suggests buyers need to look
             closely at individual property features rather than just 
            comparing by price or size alone.
""")


