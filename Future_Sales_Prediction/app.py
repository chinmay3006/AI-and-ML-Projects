import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# 1. Page Configuration
st.set_page_config(page_title="Future Sales Predictor", layout="wide")
st.title("📈 Future Sales Prediction App")
st.markdown("Predict how much sales you'll generate based on your advertising budget.")

# 2. Data Loading
@st.cache_data
def load_data():
    return pd.read_csv("advertising.csv")

try:
    data = load_data()

    # 3. Sidebar for User Inputs
    st.sidebar.header("Advertising Budget ($)")
    tv = st.sidebar.number_input("TV Advertising", min_value=0.0, value=230.1)
    radio = st.sidebar.number_input("Radio Advertising", min_value=0.0, value=37.8)
    news = st.sidebar.number_input("Newspaper Advertising", min_value=0.0, value=69.2)

    # 4. Model Training Logic
    # Hum features (x) aur target (y) select kar rahe hain
    x = np.array(data.drop(["Sales"], axis=1))
    y = np.array(data["Sales"])
    
    xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.2, random_state=42)
    model = LinearRegression()
    model.fit(xtrain, ytrain)

    # 5. Prediction Result
    user_features = np.array([[tv, radio, news]])
    prediction = model.predict(user_features)

    st.sidebar.markdown("---")
    st.sidebar.success(f"### Predicted Sales: {prediction[0]:.2f} units")

    # 6. Dashboard Visualizations
    st.subheader("Sales vs. Advertising Channels")
    col1, col2, col3 = st.columns(3)

    with col1:
        fig_tv = px.scatter(data, x="Sales", y="TV", size="TV", trendline="ols", title="TV vs Sales")
        st.plotly_chart(fig_tv, use_container_width=True)

    with col2:
        fig_radio = px.scatter(data, x="Sales", y="Radio", size="Radio", trendline="ols", title="Radio vs Sales")
        st.plotly_chart(fig_radio, use_container_width=True)

    with col3:
        fig_news = px.scatter(data, x="Sales", y="Newspaper", size="Newspaper", trendline="ols", title="Newspaper vs Sales")
        st.plotly_chart(fig_news, use_container_width=True)

    # Show Raw Data
    if st.checkbox("Show Raw Dataset"):
        st.dataframe(data)

except FileNotFoundError:
    st.error("Bhai, 'advertising.csv' file nahi mili! Make sure file app.py ke sath hi rakhi ho.")