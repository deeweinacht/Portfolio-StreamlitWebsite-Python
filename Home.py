import streamlit as st

st.set_page_config(page_title='Dee Weinacht - Home', layout='wide')
st.header('Dee Weinacht')

col1, col2 = st.columns(2)
with col1:
    st.image('images/profile.jpg')
with col2:
    st.write("##### Hi, I'm Dee, and I'm an aspiring Data Scientist. I'm driven "
                 "to learn new things and to solve challenging problems.")
    about_me = """
    As a recent computer science graduate with a passion for data science I have dedicated myself to learning the 
    latest technologies and techniques in the field, honing my skills through a combination of coursework, 
    independent learning, and personal projects. In doing so I have developed advanced skills in data preprocessing, 
    data analysis, data visualization, and machine learning. I primarily work in Python but I am also a competent Java 
    programmer. 

    I am a highly conscientious, dedicated individual who is committed to delivering high-quality work that provides 
    valuable and actionable insights. I am a strong team player who enjoys collaborating with others to tackle complex 
    problems. I am excited to bring my skills and enthusiasm for data science to a challenging and rewarding position in 
    the field.
    """
    st.write(about_me)

st.write("")

site_about = """
This portfolio site includes several projects that demonstrate my skills and knowledge
 in python and data science. Please take some time to take a look!
"""
st.write(site_about)
