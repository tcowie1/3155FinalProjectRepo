from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
from multiapp import MultiApp

#Home and Navigation Setup
st.set_page_config(page_title='UniSight', page_icon=":goat:")
"""
# UniSight

At UniSight, we want to provide accessible, easy-to-read data and 
visuals to help potential and current students make informed decisions 
on college degrees and the careers they lead to. Guiding individuals through 
major college and career decisions, with up-to-date information, is our 
objective.

"""
#Sidebar Navigation
navChoice = st.sidebar.selectbox('Navigation', ('Home', 'Salaries', 'Loans'))
