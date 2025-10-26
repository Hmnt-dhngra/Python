import streamlit as st
import pandas as pd
import numpy as np

## Title
st.title("Dummy app") ## run the app by going into that directory and then on cmd type streamlit run app.py

##  Display a simple text
st.write('This is a simple text')

## create a simple dataframe 

df = pd.DataFrame({
    'first_col' : [1, 2, 3, 4],
    'second_col' : [5, 6, 7, 8],
})

## Display the dataframe
st.write('This is the dataframe')
st.write(df)

## create a line chart
chart_data = pd.DataFrame(np.random.randn(20,3), columns =['a', 'b', 'c'])
st.line_chart(chart_data)