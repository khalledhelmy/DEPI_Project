# Sales Data Analysis and Prediction
 
This repository contains a Jupyter Notebook and a Streamlit app that perform data analysis and sales prediction for a retail sales dataset. The goal is to use machine learning models to predict item sales by analyzing both item and outlet-specific characteristics.

## Table of Contents
- [Objective](#objective)
- [Dataset](#dataset)
- [Project Structure](#project-structure)
- [Dependencies](#dependencies)
- [Streamlit App](#streamlit-app)

## Objective
The main objectives of this project are:
- **Data Cleaning**: Handling missing values and preparing the dataset for modeling.
- **Exploratory Data Analysis (EDA)**: Understanding patterns and relationships in the dataset using visualization techniques.
- **Sales Prediction**: Using machine learning models to predict the `Item_Outlet_Sales` based on various item and outlet features.
- **Model Evaluation**: Comparing the performance of different regression models, including:
  - Linear Regression
  - Decision Tree Regressor
  - Random Forest Regressor
  - XGBoost Regressor
  - Ridge

## Dataset
The dataset used in this project can be found on Kaggle: [Big Mart Sales Prediction Dataset](https://www.kaggle.com/datasets/shivan118/big-mart-sales-prediction-datasets)

The dataset used in this project has the following columns:
- **Item_Identifier**: Unique identifier for each item.
- **Item_Weight**: Weight of the item (some missing values).
- **Item_Fat_Content**: Indicates whether the item is low fat or regular.
- **Item_Visibility**: Percentage visibility of the item in the store.
- **Item_Type**: Category/type of the item (e.g., Dairy, Meat).
- **Item_MRP**: Maximum retail price of the item.
- **Outlet_Identifier**: Unique identifier for each outlet.
- **Outlet_Establishment_Year**: Year when the outlet was established.
- **Outlet_Size**: Size of the outlet (some missing values).
- **Outlet_Location_Type**: Tiered categorization of the outlet's location.
- **Outlet_Type**: Type of outlet (e.g., Grocery Store, Supermarket).
- **Item_Outlet_Sales**: Sales of the item at the respective outlet (target variable).

## Project Structure
- **Sales_Prediction.ipynb**: Main notebook containing the code for data analysis, feature engineering, model training, and evaluation.
- **Train.csv**: Dataset used for training the models.
- **sales_prediction_app.py**: Streamlit app for predicting sales based on user inputs.

## Dependencies
The project requires the following Python libraries:
- **Pandas**: Data manipulation and analysis.
- **Numpy**: Numerical operations.
- **Matplotlib & Seaborn**: Data visualization.
- **Scikit-Learn**: Machine learning models and tools.
- **XGBoost**: Implementation of the XGBoost Regressor.
- **Streamlit**: For the web application.

## Streamlit App
- Ensure the trained model (model.pkl) and cleaned data (cleaned_data.csv) are available in the same directory.
- To launch the prediction app, run the following command in your terminal:

```sh
streamlit run sales_prediction_app.py
