import streamlit as st

st.set_page_config(page_title='Homepage', layout='wide')
col1, col2 = st.columns(2)


with col1:
    st.image('images/work in progress.jpg')
with col2:
    st.title('Dee Weinacht')
    about_me = """
    Hello, I'm Dee, and I'm an aspiring Data Scientist. I have a passion for
    working with data to reveal powerful and impactful new insights. I'm driven
    to solve problems and to always be learning new things. 
    I have a B.Sc. in Computer Science and have developed my skills in data
    analysis, data cleaning/wrangling, machine learning, and data visualization.
    I primarily work with Python but I am also a competent Java programmer. 
    """
    st.write(about_me)

site_about = """
This site is to highlight some of my coding and data projects.
Please take some time to look around!
"""
st.write(site_about)