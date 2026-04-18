import streamlit as st

st.set_page_config(page_title='Dee Weinacht - Home', layout='wide')
st.header('Dee Weinacht')

moved_message = """
### This portfolio has moved!

[View my current data portfolio](https://dee-weinacht.carrd.co/)

[Visit my GitHub profile](https://github.com/deeweinacht/)

My latest work includes SQL, Python, ETL, dashboards, and analytics engineering projects.
"""

st.write(moved_message)

st.write("")

st.write("")

st.write("### About Me")

about_me = """
    As a recent computer science graduate with a passion for data science I have dedicated myself to learning the tools 
    and techniques of data science and analytics, honing my skills through a combination of coursework, independent 
    learning, and personal projects. In doing so I have developed advanced skills in data preprocessing, 
    data analysis, data visualization, and machine learning. I primarily work in Python but I am also a competent Java 
    programmer. 

    I am a highly conscientious, dedicated individual who is committed to delivering high-quality work that provides 
    valuable and actionable insights. I am a strong team player who enjoys collaborating with others to tackle complex 
    problems. I am excited to bring my skills and enthusiasm for analysis to a challenging and rewarding position in 
    the field.
    """
st.write(about_me)
