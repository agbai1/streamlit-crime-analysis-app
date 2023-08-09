#Import the required Libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

def app5_page():
    '''
    Wraps as a function to import to create multiple pages
    Args:
        none
    Returns:
        none
    '''
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

    # Load Region Data
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

    # make the jurisdiction capitalised case
    crime['jurisdiction'] = crime['jurisdiction'].str.capitalize()


    # merge crime and region data so as to get the regions
    # INNER merge excludes "jurisdiction == FEDERAL" as it doesn't hav enough data.
    crime_df = pd.merge(crime, region_data, left_on = 'jurisdiction', right_on = "State", how = "inner")
    
     #calculating incarceration rate and adding as a new column
    crime_df['incarceration_rate'] = (crime_df['prisoner_count'] / crime_df['state_population']) * 100000
    #crime_df.head()

    # Rounding "incarceration rate" to 2 decimal places
    crime_df['incarceration_rate'] = round(crime_df['incarceration_rate'],2)
    #crime_df.head()

    # First, sort the data by state and year
    crime_sorted = crime_df.sort_values(['jurisdiction', 'year'])

    # Calculating rates per 100,000 population
    crime_sorted['incarceration_rate'] = crime_sorted['prisoner_count'] / crime_sorted['state_population'] * 100000
    crime_sorted['violent_crime_rate'] = crime_sorted['violent_crime_total'] / crime_sorted['state_population'] * 100000
    crime_sorted['property_crime_rate'] = crime_sorted['property_crime_total'] / crime_sorted['state_population'] * 100000
    
    # Groupby state and calculate the percent change for violent crime, property crime, and incarceration
    crime_sorted['violent_crime_pct_change'] = crime_sorted.groupby('jurisdiction')['violent_crime_total'].pct_change() * 100
    crime_sorted['property_crime_pct_change'] = crime_sorted.groupby('jurisdiction')['property_crime_total'].pct_change() * 100
    crime_sorted['incarceration_pct_change'] = crime_sorted.groupby('jurisdiction')['prisoner_count'].pct_change() * 100
    
    
    # First, sort the data by state and year
    #crime_sorted = crime_df.sort_values(['jurisdiction', 'year'])
    
    fig_combined = px.line(crime_sorted, x='year', y=['violent_crime_pct_change', 'property_crime_pct_change', 'incarceration_pct_change'],
                           labels={'value': 'Percent Change', 'variable': 'Metric'},
                           title='Percent Change in Violent Crime, Property Crime, and Incarceration by Year',
                           line_dash_sequence=['solid', 'dash', 'dot'],
                           line_shape='linear')
    fig_combined.update_traces(mode='lines+markers')
    
   

  # Selecting California data
    california_data = crime_sorted[crime_sorted['jurisdiction'] == 'California']
    
    # Defining distinct colors for each category
    colors = {'incarceration': 'blue', 'violent_crime': 'red', 'property_crime': 'green'}
    
    # Calculating percent change for each crime rate
    california_data['incarceration_rate_change'] = california_data['incarceration_rate'].pct_change() * 100
    california_data['violent_crime_rate_change'] = california_data['violent_crime_rate'].pct_change() * 100
    california_data['property_crime_rate_change'] = california_data['property_crime_rate'].pct_change() * 100

    # Creating a new dataframe that includes only every second year starting from 2001
    california_data_even_years = california_data[california_data['year'] % 2 == 1]

    plt.figure(figsize=(10,6))

    
    
    # Plotting California's percent change in rates over the even years
    plt.plot(california_data_even_years['year'], california_data_even_years['incarceration_rate_change'], label='Incarceration', color=colors['incarceration'])
    plt.plot(california_data_even_years['year'], california_data_even_years['violent_crime_rate_change'], label='Violent Crime', color=colors['violent_crime'])
    plt.plot(california_data_even_years['year'], california_data_even_years['property_crime_rate_change'], label='Property Crime', color=colors['property_crime'])

    plt.xlabel('Year')
    plt.ylabel('Percent Change (%)')
    plt.title('Percent Change in Incarceration, Violent Crime, and Property Crime Rates for California Over Every Two Years')
    plt.legend()
    plt.grid(True)
    
    
    # Violent Crime Percent Change
    fig1 = px.line(crime_sorted, x="year", y="violent_crime_pct_change", color="Region", title="Percent Change in Violent Crimes by Region over Time")
   
    
    # Add a title and intro text
    st.markdown("<h1 style='text-align: center; color: grey;'>Data Preparation: Crime and Incarceration by State<br/><br/></h1>", unsafe_allow_html=True)
    st.write('This page explains the data preparation process, using the crime data as an example of how we are able to create meaningful visualizations.')

    st.write("The fourth step in the data science process steps is data preparation. The process of data preparation is to alter the original dataset in a way where it can now be analyzed for decisions to be made. Data preparation can be accomplished using multiple forms of visualizations including regression models, bar graphs, scatterplots, heatmaps, etc.")
    
    st.write("**Observation**")
    st.write("This line plot visualizes the percent changes in three key metrics over time: violent crime, property crime, and incarceration rates. It provides a comparative analysis of how violent crime, property crime, and incarceration rates have evolved. Based on our plot, you can see that the percent change in violent crime and incarceration rate was significant between 2004 and 2006 but then started decreasing afterward. Visualizing these trends on the same graph allows one to understand how changes in one metric may correlate with changes in others. This visualization may be valuable to policymakers, law enforcement agencies, and even researchers in assessing the effectiveness of crime prevention measures.")
    
    # Percent Change in Incarceration, Violent Crime, and Property Crime Rates for California Over Every Two Years
    st.plotly_chart(fig_combined)

    st.write('The plot below shows how violent crime, property crime, and incarceration rates have evolved across four regions. We can see the differences that exist between various regions. According to our graph, the West Coast had very high crime rates around 2006 but decreased over time. Law enforcement agencies will also find this visualization very resourceful since it allows us to understand the dynamics of violent crime and the decisions in crime prevention.')
    
    # Percent Change in Violent Crimes by Region over Time
    st.plotly_chart(fig1)
    
    st.write('The plot visualizes the percent change in incarceration, violent crime, and property crime rates for California every two years, starting from 2001. The incarceration rate fluctuates slightly, with some years showing a slight increase and others a decrease. The decreasing trends in crime rates (violent and property crime) may reflect successful policies contributing to a safer environment, but around 2013, crime rates started to increase significantly.')
    
    #The plot visualizes the percent change
    st.pyplot(plt.gcf())
   