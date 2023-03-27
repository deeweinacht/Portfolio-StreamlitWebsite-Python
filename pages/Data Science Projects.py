import streamlit as st
import pandas as pd

st.set_page_config(page_title='Portfolio', layout='wide')
# data = pd.read_csv('files/project_data.csv')

st.title('Data Science')
st.write('Check out some of my data projects:')

"""
for index, row in data.iterrows():
    col1, col2 = st.columns(2)
    with col1:
        st.image('images/' + row['image'])
    with col2:
        st.subheader(row['title'])
        st.write(row['description'])
        st.caption(row['url'])
"""