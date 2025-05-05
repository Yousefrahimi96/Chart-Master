import streamlit as st
import pandas as pd
import plost

st.title('Chart Master')

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:

    # Can be used wherever a "file-like" object is accepted:
    dataframe = pd.read_csv(uploaded_file)
    st.write(dataframe)
    
    plost.line_chart(
    dataframe,
    x='Age',  # The name of the column to use for the x axis.
    y='Pclass',  # The name of the column to use for the data itself.
    color='Sex', # The name of the column to use for the line colors.
    )