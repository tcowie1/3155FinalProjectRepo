from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

<<<<<<< HEAD

=======
>>>>>>> 2a10d1b74ada7dcd62d90a79258a784e6be3c615
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
st.sidebar.header("Home")
navChoice = st.sidebar.selectbox('Navigation', ('Home', 'Salaries', 'Loans'))
<<<<<<< HEAD
#Test
=======
>>>>>>> 2a10d1b74ada7dcd62d90a79258a784e6be3c615
