#Import the required Libraries
import streamlit as st
import pandas as pd

def app3_page():
    '''
    Wraps as a function to import to create multiple pages
    Args:
        none
    Returns:
        none
    '''
     # Load Crime Data
    @st.cache_data
    def read_crime_data():
        '''
       Reads in crime data as a csv file
    Args:
            none
    Returns:
            dafaframe of crime data
        '''
        URL = "https://raw.githubusercontent.com/JulietKuruvilla/CrimeData/main/crime_and_incarceration_by_state_2018.csv"
        
        df = pd.read_csv(URL)
        return df
   
    # Create file object
    crime = read_crime_data()
    if crime not in st.session_state:
        st.session_state['file_1'] = crime
    
     # Load Region Census Data
    @st.cache_data
    def read_region_data():
        '''
       Reads in census region data as a csv file
    Args:
            none
    Returns:
            dafaframe of region data
        '''
        URL = "https://raw.githubusercontent.com/JulietKuruvilla/CrimeData/main/us_regions_states.csv"
        
        df = pd.read_csv(URL)
        return df
    
    region_data = read_region_data()
    if region_data not in st.session_state:
        st.session_state['region_data'] = region_data

    st.markdown("<h1 style='text-align: center; color: grey;'>Data Cleaning: Crime and Incarceration by State<br/><br/</h1>", unsafe_allow_html=True)
    
    st.markdown(
    """
    This step involves cleaning the data. Almost all data need some level of cleaning before it can be used for analysis. This step involves dealing with missing or inconsistent data, removing outliers or transforming variables.
    Data cleaning is a critical step in the data science process, especially when working with datasets related to crime and incarceration by state. It involves identifying and rectifying errors, inconsistencies, and missing values in the dataset to ensure it is accurate, reliable, and suitable for analysis. Here's a detailed explanation of the data cleaning process for the "Crime and Incarceration by State" dataset:
    """
    )
    st.markdown("* **Handling Missing Values:** Missing values are common in datasets and can arise due to data collection errors or incomplete information. The data cleaning process involves identifying missing values in each column and deciding how to handle them. Options include removing rows with missing values, imputing missing values using statistical measures like mean or median, or using advanced imputation methods like regression or machine learning-based imputation.")
    
    st.markdown(" >> First show a list of the number of null values by column names using this code.")
    code_one = '''print("Missing values by Count: ")
crime.isnull().sum()
                '''
    st.code(code_one, language='python')
    st.write(crime.isnull().sum())
    
    st.markdown(" >> Code to imputate missing data by replacing null data with 0.")
    
    code_two = '''
    def fill_na(column_list):
  \'''
    Takes in a list of column names and fills 'NA'
    with 0 in a dataframe based on column names
Args:
    column_list: list of column names in a dataframe
Returns:
    list: dataframe of all changed null values
 \'''
    for column in column_list:
    crime[column] = crime[column].fillna(0)

  return crime
                '''
    st.code(code_two, language='python')
    
    
    def format_column_name(text):
        '''
        Function to convert string to desired format
    Args:
            column name
    Returns:
            formatted column name
        '''
        words = text.split('_')
        return ' '.join(word.capitalize() for word in words)

    # Change column names to desired format
    crime.columns = [format_column_name(col) for col in crime.columns]

    # make the jurisdiction capitalised case
    crime['Jurisdiction'] = crime['Jurisdiction'].str.capitalize()

    
    # merge crime and region data so as to get the regions
    # INNER merge excludes "jurisdiction == FEDERAL" as it doesn't hav enough data.
    crime_df = pd.merge(crime, region_data, left_on = 'Jurisdiction', right_on = "State", how = "inner")
    
    st.markdown("* **Dealing with Outliers:** Outliers are extreme values that deviate significantly from the rest of the data. Outliers can distort statistical analysis and modeling results. Data cleaning involves identifying and handling outliers, which can include removing them if they are data errors or transforming them to reduce their impact.")

    st.markdown("* **Data Type Conversion:** Ensuring the correct data types for each column is essential to avoid misinterpretations or errors during analysis. For example, numerical data should be represented as numbers (integers or floats), dates as date objects, and categorical variables as strings.")
    
    st.markdown(" >> Function to convert column data types in a pandas dataframe to string")
    
    code_four = ('''
    col_list = ['year']
    def convert_dtypes_to_string(df, col_list):
    \'''
  This function converts all dtypes in a pandas dataframe to float for the columns specified in the `column_list` argument.
  Args:
    df: The pandas dataframe.
    column_list: A list of column name to include from the conversion.

  Returns:
    The pandas dataframe with dtype changed to string for the columns specified in the `column_list` argument.
  \'''
      for col in col_list:
        df[col] = df[col].astype(str)
      return df
    ''')
    st.code(code_four, language='python')
                 
    st.markdown("* **Cleaning Text Data:** If the dataset includes textual information, such as crime descriptions or state names, it may require text cleaning. This involves tasks like removing special characters, converting text to lowercase, removing stop words, and applying stemming or lemmatization to standardize the text data.")
    
    st.markdown(" >> Code to capitalize all data in a dataframe column")
    
    code_three = '''
    def format_column_name(text):
    \'''
     Formats column name
Args:
    column name
Returns:
        formatted column name
    \'''
        words = text.split('_')
        return ' '.join(word.capitalize() for word in words)

# Change column names to desired format
crime.columns = [format_column_name(col) for col in crime.columns]

# make the jurisdiction capitalised case
crime['Jurisdiction'] = crime['Jurisdiction'].str.capitalize()
            '''
    st.code(code_three, language='python')
    
    st.markdown("* **Addressing Inconsistencies:** Datasets collected from different sources may contain inconsistencies in naming conventions, abbreviations, or data formats. Data cleaning involves standardizing these inconsistencies to ensure the data is consistent and coherent.")

    st.markdown("* **Data Integration and Merging:** In some cases, data from multiple sources may need to be combined to create a comprehensive dataset for analysis. Data integration and merging require careful handling of common identifiers (e.g., state names or codes) to correctly combine the data without introducing errors.")
    
    # Create a section for the dataframe header
    st.write('>> First 5 Rows of Crime Data')
    st.write(crime.head())

    # Create a section for the dataframe header
    st.write('>> First 5 Rows of Region Census Data')
    st.write(region_data.head())
    
    code_four = '''# merge crime and region data so as to get the regions
# INNER merge excludes "jurisdiction == FEDERAL" as it doesn't have enough data.
crime_df = pd.merge(crime, region_data, left_on = 'Jurisdiction', right_on = "State", how = "inner")
                '''
    st.code(code_four, language='python')
    
    st.write('>> Merged Crime and Region Data')
    st.write(crime_df.head())
    
     
    