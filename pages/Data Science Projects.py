import streamlit as st
import json

st.set_page_config(page_title='Dee Weinacht - Data Science', layout='wide')
with open('data/jupyter_projects.JSON', 'r') as file:
    data = json.load(file)

st.header('Data Science Projects')
st.markdown('**Check out some of my data science projects created in JupyterLab:**')

for project in data:
    st.write("---")
    st.subheader(project['name'])
    col1, col2 = st.columns(2)
    with col1:
        st.image('images/' + project['image'])
        st.markdown(f"[GitHub repository]({project['url']})")
    with col2:

        st.markdown('**' + project['description'] + '**')
        for skill in project['skills']:
            st.markdown('- ' + skill)
