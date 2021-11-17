import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt


st.set_page_config(
    page_title='Grad rates for University of North Carolina at Charlotte')
st.header('Choose a college')

# --- LOAD DATAFRAME
data = pd.read_excel('graduates.csv')
df = pd.DataFrame(
    data, columns=['Year', 'Education.Major', 'Salaries.Median', 'Salaries.Highest', 'Salaries.Lowest'])

# selected_college = st.selectbox('Select a College', df['college'])
# college_data = df[df['college'] == selected_college]

# fig = go.Figure(data=[go.Table(
#     header=dict(values=['Applications', 'Accepted Applications', 'Number Enrolled (from accepted', 'Graduation Rate'],
#                 fill_color='grey',
#                 align='left'),
#     cells=dict(values=[college_data['Apps'], college_data['Accept'], college_data['Enroll'], college_data['Grad.Rate']],
#                fill_color='black',
#                align='center',
#                font=dict(family='sans-serif', size=16))
# )])


st.plotly_chart(fig)
