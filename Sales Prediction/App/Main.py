import streamlit as st

st.set_page_config(
    page_title='Sales Prediction',
    page_icon="👋"
)

st.write("# Welcome to Our Page! 👋")

st.write("""
    This application allows you to predict the sales of items in retail outlets based on various input features.
    
    **Main Features:**
    1. **Sales Prediction**: Predict sales based on item details such as weight, fat content, visibility, and price.
    2. **Data Visualizations**: Explore insightful visualizations that highlight sales performance by outlet type, location, size, and more.
    
    Use the radio buttons above to navigate through the different sections. Start predicting or explore the data through the visualizations!
    
    Enjoy using the app, and feel free to experiment with the custom visualization feature to create your own analysis.
    """)

st.sidebar.success('Select Page.')