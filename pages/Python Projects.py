import streamlit as st
import json

st.set_page_config(page_title='portfolio', layout='wide')
with open('data/python_projects.JSON', 'r') as file:
    data = json.load(file)


st.title('Python projects')
st.markdown('**Check out some of my coding projects written in Python:**')

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

