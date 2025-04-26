import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('Weather Report')
fileupload = st.file_uploader('Upload a CSV file: ', type="csv")
if fileupload is not None:
    st.write('File Uploaded!')
    df = pd.read_csv(fileupload)
    st.subheader('Data Preview:')
    st.dataframe(df.head())
    st.subheader('Data Summary:')
    st.dataframe(df.describe())

    st.subheader('Filter Data: ')
    columns = df.columns.tolist()
    selected_column = st.selectbox('Select Column to filter by: ', columns)
    unique_values = df[selected_column].unique()
    selected_value = st.selectbox('Select a Value: ', unique_values)
    filtered_df = df[df[selected_column] == selected_value]
    st.dataframe(filtered_df)
    st.subheader("Plot Data")
    x_column = st.selectbox("Select x-axis column", columns)
    y_column = st.selectbox("Select y-axis column", columns)

    if st.button("Generate Plot"):
        st.line_chart(filtered_df.set_index(x_column)[y_column])
else:
    st.write('Upload a file to get started!')


