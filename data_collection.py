#webapp package
import streamlit as st
#data manipulation package
import pandas as pd

def app2_page():
    '''
    Wraps as a function to import to create multiple pages
    Args:
        none
    Returns:
        none
    '''
    
    st.markdown("<h1 style='text-align: center; color: grey;'>Data Collection: Crime and Incarceration by State<br/><br/></h1>", unsafe_allow_html=True)
    st.write('Now let’s get started with the task of Crime and Incarceration by State Analysis with Python and Streamlit. We will start this task by importing the necessary Python libraries and the dataset:')

    st.write("[Dataset](https://raw.githubusercontent.com/JulietKuruvilla/CrimeData/main/crime_and_incarceration_by_state_2018.csv)")

    #import libraries needed
    st.divider()
    st.write("**Libraries Used:**")
    st.write("import streamlit as st")
    st.write("import pandas as pd")
    st.write("import matplotlib.pyplot as plt")
    st.write("import numpy as np")
    st.write("import seaborn as sns")
    st.write("import plotly.express as px")

    st.divider()

    @st.cache_data
    def get_data():
        url = "https://raw.githubusercontent.com/JulietKuruvilla/CrimeData/main/crime_and_incarceration_by_state_2018.csv"
        return pd.read_csv(url)
    df = get_data()

    st.write("**Display top 5 rows of the dataset**")
    st.dataframe(df.head())

    st.write("**Display last 5 rows of the dataset**")
    st.dataframe(df.tail())

    st.write("Now let’s have a look at some statistics from the dataset by using the **describe** function of Pandas:")
    st.dataframe(df.describe())

    st.write("Get the columns of the dataset using **columns** method.")
    st.dataframe(df.columns)

    st.write("Based on the data, we can see there are only two categorical variables : **jurisdiction** and **year**.")