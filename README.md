# 📈 Sales Forecasting Using Machine Learning with Python

<div align="center">

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?style=for-the-badge&logo=scikitlearn)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-purple?style=for-the-badge&logo=pandas)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-red?style=for-the-badge&logo=streamlit)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

Machine Learning based Sales Forecasting System developed using Python, Scikit-Learn and Streamlit.

</div>

---

## 📌 Overview

This project predicts furniture sales using historical sales data and Machine Learning algorithms.

The project includes:

- Data Cleaning
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Machine Learning Model Training
- Model Evaluation
- Interactive Streamlit Dashboard
- Real-Time Sales Prediction

The best performing model (Random Forest Regressor) was deployed using Streamlit.

---

## 🎯 Objectives

- Analyze historical furniture sales
- Build predictive ML models
- Compare multiple regression algorithms
- Select the best-performing model
- Deploy an interactive dashboard
- Generate future sales predictions

---

## 🛠 Tech Stack

| Category | Technology |
|-----------|------------|
| Language | Python |
| IDE | VS Code / Jupyter Notebook |
| Libraries | Pandas, NumPy, Scikit-Learn |
| Visualization | Matplotlib, Seaborn, Plotly |
| Deployment | Streamlit |
| Model Saving | Joblib |

---

## 📂 Dataset

The project uses the **Furniture Sales Dataset** containing historical sales transactions.

Features include:

- Order Date
- Ship Date
- Customer Details
- Product Details
- Region
- Quantity
- Discount
- Profit
- Sales (Target Variable)

---

## 📊 Exploratory Data Analysis

EDA includes:

- Dataset Information
- Missing Value Analysis
- Correlation Heatmap
- Monthly Sales Trend
- Sales by Region
- Sales by Segment
- Profit by Sub-Category
- Discount vs Sales
- Sales Distribution

---

## 🤖 Machine Learning Models

The following regression algorithms were implemented:

- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor

---

## 📈 Model Performance

| Model | MAE | RMSE | R² Score |
|--------|-----|------|----------|
| Linear Regression | 304.60 | 506.66 | 0.162 |
| Decision Tree | 242.17 | 517.41 | 0.126 |
| **Random Forest** | **199.03** | **404.93** | **0.465** |

Random Forest achieved the best performance and was selected for deployment.

---

## 💻 Dashboard Features

The Streamlit dashboard provides:

- KPI Cards
- Monthly Sales Trend
- Sales by Region
- Sales by Segment
- Profit by Sub-Category
- Dataset Explorer
- Prediction Module
- Model Performance Summary

---

## 🚀 Installation

Clone the repository

```bash
git clone https://github.com/yourusername/Sales-Forecasting-Using-Machine-Learning.git
```

Navigate into the project

```bash
cd Sales-Forecasting-Using-Machine-Learning
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

## 📁 Project Structure

```text
data/
models/
notebooks/
app.py
README.md
requirements.txt
```

---

## 📷 Screenshots

Add screenshots here after uploading them.

- Dashboard
- Monthly Sales Trend
- Prediction Module
- Dataset Explorer

---

## 🔮 Future Enhancements

- XGBoost Implementation
- LSTM Time-Series Forecasting
- Cloud Deployment
- Real-Time Database Integration
- Power BI Dashboard
- Automated Report Generation

---

## 👨‍💻 Author

**Shreyash Kashyap**

B.E. Computer Science Engineering

Machine Learning Intern

NAVIOTECH SOLUTION Pvt. Ltd.

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub!
