import streamlit as st
import json

st.set_page_config(page_title='Dee Weinacht - Skill Set', layout='wide')
with open('data/competencies.JSON', 'r') as file:
    data = json.load(file)

st.subheader('Here is a more detailed look at my data science skill set than would fit on a resume:')

col1, padding, col2 = st.columns([2, 0.5, 2])

with col1:
    st.subheader('Skills')
    for skill in data['Skills'].keys():
        st.write('**' + skill + "**")
        for details in data['Skills'][skill]:
            st.write('- ' + details)

with col2:
    st.subheader('Proficiencies')
    for proficiency in data['Proficiencies'].keys():
        st.write('**' + proficiency + '**')
        for details in data['Proficiencies'][proficiency]:
            st.write('- ' + details)

