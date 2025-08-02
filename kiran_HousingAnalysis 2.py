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

        
st.title("Correlation of data")        
numeric_data = data.select_dtypes(include='number')
st.write(numeric_data.corr())

sns.heatmap(numeric_data.corr()  ,annot=True, cmap="coolwarm")
st.pyplot()

st.title("Groupby Function")
st.write(data.groupby("bedrooms")["bathrooms"].mean())
st.write(data.groupby("bedrooms")["bathrooms"].mean().head(2))
st.write(data.groupby("bedrooms").mean(numeric_only=True).head())
st.write(data.groupby("bedrooms")[["bathrooms","stories","parking"]].max().head())

st.title("Aggregation")

st.write(data.groupby("bedrooms")["bathrooms"].agg(["mean","median","max"]))
st.write(data.aggregate({"stories":["mean","max"],"bathrooms":["count","max"]}))

st.title("Describe Categorical Data")

st.write(data.describe(),include="all")
st.write(data.describe(),include="object")
st.write(data.value_counts())
st.write(data["furnishingstatus"].unique())
st.write(data["furnishingstatus"].nunique())

if st.button("Get final Summary"):
    st.title("Insights Summary")
    st.markdown("""
    After analyzing the housing dataset, several key insights were uncovered:

    #### 📊 Overall Data Patterns
    The average home price and size showed moderate central tendencies, but both had wide ranges and high standard deviations, indicating a highly diverse housing market. Some properties stood out as outliers — either very luxurious or surprisingly small or low-priced, suggesting uneven distribution in features and quality.

    #### 📈 Correlation Insights
    Correlation analysis showed strong relationships between certain features:
    - `bathrooms` and `bedrooms` had a moderately positive correlation.
    - `stories` and `price` showed a noticeable link, possibly indicating that multi-storey homes tend to be more expensive.
    - Most other variables had low correlations, meaning price and size alone don't fully predict a property's features.

    #### 📚 Grouped Trends (Bedrooms-wise)
    Grouping by `bedrooms` showed:
    - Most common configurations were 2 to 4 bedrooms.
    - As the number of bedrooms increased, the average number of `bathrooms` and `stories` also increased.
    - Interestingly, the `parking` availability also scaled with more bedrooms.

    #### 📦 Aggregated Summary
    - `Stories` showed an average of around 1.6 with a max of 4, indicating a majority of single or double-storey homes.
    - `Bathrooms` count had both mean and max values increase steadily across more bedrooms, confirming an upscale trend.

    #### 🏠 Categorical Insights
    - The `furnishingstatus` column revealed three unique statuses: furnished, semi-furnished, and unfurnished — with semi-furnished being most frequent.
    - `value_counts()` showed the most common complete records, indicating dominant property types in the dataset.

    #### 🧭 Final Thought
    This dataset reflects a diverse market — with properties differing not just in size and price but also in style, amenities, and furnishing status. Buyers should consider multiple factors beyond price, such as number of stories, parking, and furnishing, to find homes that truly match their needs.
    """)
