#webapp package
import streamlit as st
  
def app1_page():
    '''
    Wraps as a function to import to create multiple pages
    Args:
        none
    Returns:
        none
    '''
    st.markdown("<h1 style='text-align: center; color: grey;'>Data Science Process using Python and Streamlit</h1>", unsafe_allow_html=True)

    st.markdown('<div style="text-align: center;"><b>Authors: Eke Agbai, Brianna King, Dorothy Oteng, Juliet Kuruvilla</b>&nbsp&nbsp&nbspAug 5, 2023<br/><br/><br/></div>', unsafe_allow_html=True)

    st.markdown("<h3 style='text-align: center; color: black;'>A Data Science Journey: Analyzing Crime and Incarceration Trends by State from 2001 to 2016<br/><br/></h3>", unsafe_allow_html=True)

    st.write("**EXECUTIVE SUMMARY**")

    st.write('Many studies have been undertaken in the past on the factors affecting a country’s crime and incarceration rate. Incarceration in the United States is one of the primary means of punishment, penal labor and rehabilitation, for the commission of crimes or other offenses. In this article, we will introduce you to a data science process on Crime and Incarceration by State Analysis with Python and Streamlit.')


    st.write('Incarceration refers to the long-term confinement of convicted and sentenced offenders. There are several factors that contributes to crime and incarceration, taking into account state population, prisoner count and different crime types. In the section below, we will take you through a Data Science Process on Crime and Incarceration by State Analysis with Python.')

    st.write("**Objective:** Create a multi-page web application using Python and Streamlit to showcase the data science process for Crime and Incarceration by State.")

    # displays a horizontal rule in your app
    st.divider()

    st.write("**Data Science Process Steps:**")         

    #displays string formatted as Markdown
    st.markdown("""
    - Data Collection
    - Data Cleaning
    - Data Exploration
    - Data Preparation
    - Model Training
    - Model Deployment
    """)
    
    # displays a horizontal rule in your app
    st.divider()

    # Writing details about each process within datascience process
    st.write("**Step 1: Data Collection**")
    
    st.write("This step involves gathering data from different databases, APIs, or other sources. Some examples of sources for the collection of primary data are observations, surveys, experiments, personal interviews, questionnaires, etc. It might also involve combining data from multiple sources.")
    
    st.write("**Step 2:  Data Cleaning**")
    
    st.write("Data cleaning involves fixing bad data in a given dataset. Almost all data need some level of cleaning before it can be used for analysis. This step involves dealing with missing or inconsistent data, removing outliers or transforming variables.")
    
    st.write("**Step 3: Data Exploration**")
    
    st.write("This step involves exploring the data to understand its main characteristics and relationships between variables. We can use data visualization and statistical techniques to describe dataset characteristics, such as size, quantity, and accuracy.")
    
    st.write("**Step 4: Data Preparation**")
    
    st.write("This is when you visualize your data and prepare it for model training.")
    
    st.write("**Step 5: Model Training**")
    
    st.write("Once we have explored our data, we can now build predictive or descriptive models. This might involve machine learning or statistical modeling, depending on the problem.")
    st.write("**Step 6: Model Evaluation**")
    
    st.write("Evaluate the performance of the selected model using various metrics and compare it to other models to determine if it is efficient and bringing the output that we expected. This is when you can perform a demo on a different dataset that was not used in training the model.") 
    st.write("**Step 7: Model Deployment**")
    
    st.write("Finally, if your model performs well, the next step is to deploy the selected model to the production environment with stakeholder’s approval making the model available for others to use for predictions and classifications.")