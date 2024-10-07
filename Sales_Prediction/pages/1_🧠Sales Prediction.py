import streamlit as st
import pickle
import pandas as pd
import numpy as np

st.set_page_config(
    page_title='Sales Model',
    page_icon="🧠"
)

# Load model and data
try:
    reg = pickle.load(open('App\model.pkl', 'rb'))
    clean_df = pd.read_csv('App\cleaned_data.csv')
except FileNotFoundError as e:
    st.error(f"Error loading files: {e}")
    st.stop()

# App Title and Description
st.title('Sales Prediction App')
st.write("This app predicts the sales of items in retail outlets based on various input features. Fill out the details below and click 'Predict Sales' to see the predicted value.")

# Input fields
st.header("Item Details")
item_id = st.selectbox('Item ID', clean_df['Item_Identifier'].unique(), help="Select the unique identifier for the item.")
weight = st.number_input('Weight (in kg)',
                         min_value=float(clean_df['Item_Weight'].min()),
                         max_value=float(clean_df['Item_Weight'].max()),
                         help="Enter the weight of the item.")
fat_content = st.selectbox('Fat Content', clean_df['Item_Fat_Content'].unique(), help="Select the fat content of the item.")
visibility = st.number_input('Visibility (percentage)',
                             min_value=float(clean_df['Item_Visibility'].min()),
                             max_value=float(clean_df['Item_Visibility'].max()),
                             help="Enter the visibility percentage of the item in stores.")
item_type = st.selectbox('Item Type', clean_df['Item_Type'].unique(), help="Select the type of the item.")
item_price = st.number_input('Item Price',
                             min_value=float(clean_df['Item_MRP'].min()),
                             max_value=float(clean_df['Item_MRP'].max()),
                             help="Enter the maximum retail price of the item.")

st.header("Outlet Details")
outlet_id = st.selectbox('Outlet ID', clean_df['Outlet_Identifier'].unique(), help="Select the outlet identifier.")
year = st.number_input('Year of Establishment',
                       min_value=int(clean_df['Outlet_Establishment_Year'].min()),
                       max_value=int(clean_df['Outlet_Establishment_Year'].max()),
                       help="Enter the year the outlet was established.")
size = st.selectbox('Outlet Size', clean_df['Outlet_Size'].unique(), help="Select the size of the outlet.")
location = st.selectbox('Outlet Location Type', clean_df['Outlet_Location_Type'].unique(), help="Select the location type of the outlet.")
outlet_type = st.selectbox('Outlet Type', clean_df['Outlet_Type'].unique(), help="Select the type of the outlet.")

# Prediction button
if st.button('Predict Sales'):
    # Create new data for prediction
    new_data = pd.DataFrame({
        'Item_Identifier': [item_id],
        'Item_Weight': [weight],
        'Item_Fat_Content': [fat_content],
        'Item_Visibility': [visibility],
        'Item_Type': [item_type],
        'Item_MRP': [item_price],
        'Outlet_Identifier': [outlet_id],
        'Outlet_Establishment_Year': [year],
        'Outlet_Size': [size],
        'Outlet_Location_Type': [location],
        'Outlet_Type': [outlet_type]
    })

    # Prediction and output
    try:
        pred = reg.predict(new_data)
        price = np.exp(pred)
        st.success(f"The predicted sales for Item ID {item_id} is ₹{price[0].round(2)}")
    except Exception as e:
        st.error(f"An error occurred during prediction: {e}")