# 📈 Sales Forecasting & Demand Analysis Dashboard

An end-to-end Data Science and Machine Learning project that analyzes retail sales data, forecasts future demand, detects anomalies, segments products based on demand patterns, and presents insights through an interactive Streamlit dashboard.

## Project Overview

Efficient inventory management is one of the biggest challenges for retail businesses. Overstocking increases storage costs, while understocking results in lost sales and dissatisfied customers.

This project uses historical Superstore sales data to:

- Analyze sales trends and seasonality
- Forecast future sales using multiple forecasting models
- Detect unusual sales spikes and drops
- Segment products based on demand characteristics
- Build an interactive Streamlit dashboard for business users

The project combines **Exploratory Data Analysis (EDA)**, **Time Series Forecasting**, **Machine Learning**, **Anomaly Detection**, **Clustering**, and **Dashboard Deployment** into a single business solution.

# Objectives

- Analyze historical sales data
- Understand customer demand patterns
- Compare multiple forecasting models
- Predict future sales
- Detect abnormal sales behavior
- Segment products into demand groups
- Support inventory and supply chain decisions
- Deploy an interactive dashboard using Streamlit


# Dataset

**Dataset:** Superstore Sales Dataset

Contents include:

- Order Date
- Ship Date
- Region
- Category
- Sub-Category
- Product Name
- Sales
- Quantity
- Discount
- Profit

The dataset contains approximately **4 years of retail sales transactions** across multiple regions and product categories.

# Technologies Used

### Programming Language

- Python

### Libraries

- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Statsmodels
- Prophet
- XGBoost
- Streamlit

# Project Workflow

## Task 1 — Data Loading & Exploratory Data Analysis

- Data Cleaning
- Missing Value Analysis
- Duplicate Detection
- Feature Engineering
- Monthly & Weekly Aggregation
- Product Category Analysis
- Region-wise Sales Analysis
- Shipping Time Analysis

## Task 2 — Time Series Analysis

Performed:

- Monthly Sales Trend Analysis
- Seasonal Decomposition
- Trend Analysis
- Residual Analysis
- Stationarity Testing (ADF Test)
- Differencing

## Task 3 — Sales Forecasting

Implemented three forecasting models:

### 1. SARIMA

Statistical time-series forecasting model.

### 2. Facebook Prophet

Business-oriented forecasting model with trend and seasonality analysis.

### 3. XGBoost

Machine Learning based forecasting using lag features and rolling statistics.

### Model Performance

| Model | MAE | RMSE | MAPE |
|------|------:|------:|------:|
| SARIMA | 11532.90 | 13843.49 | 17.65% |
| Prophet | 10128.56 | 14561.39 | 14.33% |
| **XGBoost** | **8017.25** | **13156.85** | **10.60%** |

**Best Model:** XGBoost

## Task 4 — Category & Region Level Forecasting

Generated demand forecasts for:

- Furniture
- Technology
- Office Supplies
- West Region
- East Region

Compared forecast trends across different business segments.

## Task 5 — Anomaly Detection

Implemented:

### Isolation Forest

Detected unusual sales spikes and drops.

Results:

- Normal Weeks: **198**
- Anomalies Detected: **11**

Also compared results with Z-Score based anomaly detection.

## Task 6 — Product Demand Segmentation

Used **K-Means Clustering** to group products based on:

- Total Sales
- Average Order Value
- Sales Volatility
- Growth Rate

Applied:

- StandardScaler
- Elbow Method
- PCA for visualization

Demand segments identified:

- High Volume, Stable Demand
- High Volume, Premium Products
- Growing Demand
- Low Volume, Stable Demand

## Task 7 — Streamlit Dashboard

Built a multi-page interactive dashboard.

### Dashboard Pages

### Page 1

Sales Overview Dashboard

Features:

- Total Sales by Year
- Monthly Sales Trend
- Category Filter
- Region Filter
- Summary Metrics

### Page 2

Forecast Explorer

Features:

- Category/Region Selection
- Forecast Horizon Selection
- Forecast Chart
- Forecast Table
- Model Performance Metrics

### Page 3

Anomaly Report

Features:

- Weekly Sales Chart
- Detected Anomalies
- Anomaly Table

### Page 4

Product Demand Segments

Features:

- PCA Cluster Visualization
- Demand Segment Table
- Product Grouping

## Task 8 — Executive Business Report

Prepared a business-oriented report including:

- Executive Summary
- Key Findings
- Forecast Summary
- Anomaly Insights
- Demand Segmentation
- Inventory Recommendations
- Business Recommendations
- Project Limitations


# Key Business Insights

- Technology generated the highest overall sales revenue.
- West region demonstrated the strongest long-term sales growth.
- Seasonal demand increases were observed during year-end months.
- XGBoost delivered the most accurate forecasts.
- Eleven unusual sales periods were detected through anomaly detection.
- Product clustering supports optimized inventory planning.


# 📂 Project Structure

```
SalesForecasting_Likitha/

│── analysis.ipynb
│── app.py
│── requirements.txt
│── summary.docx
│── README.md

│── data/
│     └── train.csv

│── charts/
│     ├── category_sales.png
│     ├── yearly_sales_region.png
│     ├── monthly_sales_trend.png
│     ├── time_series_decomposition.png
│     ├── sarima_actual_vs_forecast.png
│     ├── prophet_forecast.png
│     ├── xgboost_actual_vs_forecast.png
│     ├── anomaly_detection.png
│     ├── elbow_method.png
│     └── product_clusters.png
```

# 🚀 Running the Project

Clone the repository

```bash
git clone https://github.com/<YOUR_USERNAME>/SalesForecasting_Likitha.git
```

Go into the project directory

```bash
cd SalesForecasting_Likitha
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the Streamlit application

```bash
streamlit run app.py
```
Streamlit Dashboard link
```bash
https://salesforecasting-jkqwji53mkrxudbruguedj.streamlit.app/
```

# Project Outputs

The project produces:

- Data Cleaning Report
- Sales Trend Analysis
- Forecast Comparisons
- Anomaly Detection Results
- Product Demand Clusters
- Interactive Dashboard
- Executive Business Report


# Business Impact

This project demonstrates how data-driven forecasting can improve retail inventory management by:

- Reducing stock shortages
- Preventing overstocking
- Improving demand forecasting
- Supporting procurement planning
- Enhancing supply chain decision-making


# Future Improvements

- Real-time sales forecasting
- Cloud database integration
- Automated model retraining
- Holiday and promotion-aware forecasting
- Interactive Power BI dashboard
- REST API deployment

# Author

**Likitha R**

B.Tech – Computer Science & Engineering

University Visvesvaraya College of Engineering, Bangalore

Skills:
- Data Analysis
- Machine Learning
- Time Series Forecasting
- Python
- Streamlit
- SQL
- Data Visualization

---

