import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from sklearn.linear_model import LinearRegression

# 1. Page Setup (Website ka title)
st.set_page_config(page_title="Tip Predictor App", layout="wide")
st.title("💸 Waiter Tips Prediction System")

# 2. Data Load karna
try:
    data = pd.read_csv("tips.csv")
    
    # 3. Sidebar (Website ke side mein filters/inputs)
    st.sidebar.header("Input Details")
    bill = st.sidebar.number_input("Total Bill ($)", value=20.0)
    sex = st.sidebar.selectbox("Gender", ["Male", "Female"])
    smoker = st.sidebar.selectbox("Smoker", ["No", "Yes"])
    day = st.sidebar.selectbox("Day", ["Thur", "Fri", "Sat", "Sun"])
    time = st.sidebar.selectbox("Time", ["Lunch", "Dinner"])
    size = st.sidebar.slider("Table Size", 1, 6, 2)

    # 4. Model Training (Back-end logic)
    df_ml = data.copy()
    df_ml["sex"] = df_ml["sex"].map({"Female": 0, "Male": 1})
    df_ml["smoker"] = df_ml["smoker"].map({"No": 0, "Yes": 1})
    df_ml["day"] = df_ml["day"].map({"Thur": 0, "Fri": 1, "Sat": 2, "Sun": 3})
    df_ml["time"] = df_ml["time"].map({"Lunch": 0, "Dinner": 1})

    X = df_ml[["total_bill", "sex", "smoker", "day", "time", "size"]]
    y = df_ml["tip"]
    model = LinearRegression().fit(X, y)

    # 5. Prediction (Button dabaate hi result)
    input_features = [[bill, 1 if sex=="Male" else 0, 1 if smoker=="Yes" else 0, 
                       {"Thur":0, "Fri":1, "Sat":2, "Sun":3}[day], 0 if time=="Lunch" else 1, size]]
    
    prediction = model.predict(input_features)
    
    st.sidebar.markdown("---")
    st.sidebar.subheader(f"Predicted Tip: ${prediction[0]:.2f}")

    # 6. Visualizations (Website ke main page par charts)
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Bill vs Tip Analysis")
        fig1 = px.scatter(data, x="total_bill", y="tip", color="day", trendline="ols")
        st.plotly_chart(fig1, use_container_width=True)
    
    with col2:
        st.subheader("Tips by Category")
        cat = st.selectbox("Choose Category", ["day", "sex", "smoker", "time"])
        fig2 = px.pie(data, values='tip', names=cat, hole=0.5)
        st.plotly_chart(fig2, use_container_width=True)

    st.write("### Dataset Preview", data.head())

except FileNotFoundError:
    st.error("Bhai, 'tips.csv' file nahi mili! Make sure file app.py ke sath hi rakhi ho.")