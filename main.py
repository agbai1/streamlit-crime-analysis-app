# Import the individual app files
from overview import app1_page
from data_collection import app2_page
from data_cleaning import app3_page
from data_exploration import app4_page
from data_preparation import app5_page
from model_trng_eval_deplmt import app6_page

import streamlit as st

# "Data Cleaning": app3,

pages = {
    "Overview":app1_page,
    "Data Collection":app2_page,
     "Data Cleaning":app3_page,
    "Exploratory Data Analy+s":app4_page,
    "Data Preparation":app5_page,
    "Model Training, Evaluation & Deployment":app6_page, 
}

st.sidebar.title('Data Science Workflow')
selected_page = st.sidebar.selectbox("Navigate the Analysis", list(pages.keys()))

# Display the selected page
pages[selected_page]()
