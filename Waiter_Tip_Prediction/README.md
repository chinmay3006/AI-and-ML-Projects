# 💸 Waiter Tip Prediction System

This project is a **Machine Learning based Web Application** built using Python and Streamlit. It predicts the tip amount a waiter might receive based on various factors like total bill, gender, smoking preference, day of the week, and time of the meal.

## 🚀 Features
* **Interactive UI:** Built with Streamlit for a smooth user experience.
* **Data Visualization:** Uses Plotly for interactive scatter plots and pie charts to analyze tipping patterns.
* **Machine Learning:** Implements **Linear Regression** from Scikit-Learn to make real-time predictions.
* **Responsive Sidebar:** Users can adjust inputs and see the predicted tip instantly.

## 🛠️ Tech Stack
* **Language:** Python
* **Libraries:** Pandas, NumPy, Scikit-Learn
* **Visualization:** Plotly
* **Framework:** Streamlit

## 📊 Dataset Information
The model is trained on the `tips.csv` dataset, which includes:
- `total_bill`: Total bill amount in USD
- `sex`: Gender of the person paying (Male/Female)
- `smoker`: Whether the person is a smoker (Yes/No)
- `day`: Day of the week (Thur, Fri, Sat, Sun)
- `time`: Time of the meal (Lunch/Dinner)
- `size`: Number of people at the table

## ⚙️ How to Run
1. Navigate to this folder.
2. Install dependencies: 
   ```bash
   pip install -r requirements.txt
