#Import the required Libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def app4_page():
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
    
    # Add a title and intro text
    st.markdown("<h1 style='text-align: center; color: grey;'>Data Exploration: Crime and Incarceration by State<br/><br/></h1>", unsafe_allow_html=True)
    st.write('This page explains the data exploration process, using the crime data as an example of different ways someone can go about exploring a dataset.')

    st.write("The third step in the data science process is data exploration. Data exploration takes place after the dataset has been cleaned and is now ready to be looked at. This allows the data scientist to gain a better understanding on the data to know what questions to ask and to identify any patterns.")

    st.write("When you're first exploring the dataset, it's important to know what the information used in any given dataset is (string or int). This will ensure that the columns that are supposed to be numbers are showing up as ints and can be manipulated.")
    st.markdown("<h6>Observation</h6>", unsafe_allow_html=True)

    st.write("You can tell that there is a significant difference between the 75th percentile(75%) and the Max values. This could mean there might be outliers in those columns (prisoner_count, violent_crime_total, robbery, agg_assault, burglary, larceny, and vehicle_theft). These outliers could either be errors in data collection and if so, should be removed. They could also be correct and meaningful data points. They could represent States that have unusually high crime rates, high prisoner count etc. that could be important to consider in our analysis.")

    codeOne = ''' crime_df.describe() '''
    st.code(codeOne, language='python')
        # Give the statistical summary of the dataset
    st.write(crime_df.describe())
    st.text("")

    st.write("In data exploration, you can also find the sum of a column, as long as the column's data type is an int or float64. In this example, we wanted to find the sum of violent crime based on the jurisdiction (or state). We can achieve this by using the .groupby function.") 

    codeTwo = ''' violent_crime_total_df = crime_df.groupby()'''
    st.code(codeTwo, language='python')

    st.write("Next, in order to find the total number of violent crimes per state, you add the name of the column you wish to group by first in parenthsis and then add the column you're finding the sum of in brackets, putting .sum at the end to ensure it finds the total number.")

    codeThree = '''('jurisdiction')['violent_crime_total'].sum(numeric_only = True)'''
    st.code(codeThree, language='python')

    st.write("Your code would look like this:") 

    codeFour = '''violent_crime_total_df = crime_df.groupby('jurisdiction')['violent_crime_total'].sum(numeric_only = True)'''
    st.code(codeFour, language='python')

    st.write("In order to print your new data frame created (showing only the first five rows with .head()), you'd use the following code to get this output:")

    codeFive = '''violent_crime_total_df.head()'''
    st.code(codeFive, language='python')

    st.write("Data exploration is also the perfect step to add an additional column for further analysis. This may be helpful if a scientist is tasked with finding the average between two columns. In this example, we wanted to create three additional columns showing the rates for every 100,000 citizen.")

    st.text("")

    st.write("In order to add this column, you first create a new data frame calling the original data frame with the name of the new column in open brackets. In this example, we want to create an 'incarceration_rate' column.")

    codeSix = '''crime_df['incarceration_rate']'''
    st.code(codeSix, language='python')

    st.write("Once you have this, you want to create the equation used in the new column being created. Since we want to find the incarceration rate per 100,000 citizen, we are going to divide the prisoner_count and state_population column and multiply the answer by 100,000. The complete new code should look like the following:")
    codeEight = '''crime_df['incarceration_rate'] = (crime_df['prisoner_count'] / crime_df['state_population']) * 100000
    '''
    st.code(codeEight, language='python')

    st.write("This will now insert a new column as shown below.") 
    
    #calculating incarceration rate and adding as a new column
    crime_df['incarceration_rate'] = (crime_df['prisoner_count'] / crime_df['state_population']) * 100000
    crime_df.head()

    # Rounding "incarceration rate" to 2 decimal places
    crime_df['incarceration_rate'] = round(crime_df['incarceration_rate'],2)
    crime_df.head()

    # First, sort the data by state and year
    crime_sorted = crime_df.sort_values(['jurisdiction', 'year'])

    # Calculating rates per 100,000 population
    crime_sorted['incarceration_rate'] = crime_sorted['prisoner_count'] / crime_sorted['state_population'] * 100000
    crime_sorted['violent_crime_rate'] = crime_sorted['violent_crime_total'] / crime_sorted['state_population'] * 100000
    crime_sorted['property_crime_rate'] = crime_sorted['property_crime_total'] / crime_sorted['state_population'] * 100000
    
    # Display the DataFrame in the Streamlit app
    st.dataframe(crime_sorted)

    # Defining distinct colors for each category
    colors = {'incarceration': 'blue', 'violent_crime': 'red', 'property_crime': 'green'}

    # Selecting few states for visual clarity, you can choose any states you want.
    selected_states = ['California', 'Texas', 'New York', 'Florida']

    plt.figure(figsize=(10,6))
    
    st.write('Incarceration Rate (Blue Lines) shows the number of people in prison for every 100,000 residents in each state. Violent Crime Rate (Red Lines) represents the number of reported violent crimes (such as assault, robbery, or murder) for every 100,000 residents. Property Crime Rate (Green Lines) shows the number of property crimes (like burglary, theft, or vandalism) per 100,000 residents. An upward trend in the green line signifies an increase in property crime, while a downward trend indicates a decrease. We can observe that for these four states, property crimes have decreased over the years between 2001 and 2016, while violent crimes and incarceration rates have remained the same.') 

    # Plotting each state's rates over the years
    for state in selected_states:
        state_data = crime_sorted[crime_sorted['jurisdiction'] == state]
        plt.plot(state_data['year'], state_data['incarceration_rate'], label=f'{state} Incarceration', color=colors['incarceration'])
        plt.plot(state_data['year'], state_data['violent_crime_total'], label=f'{state} Violent Crime', color=colors['violent_crime'])
        plt.plot(state_data['year'], state_data['property_crime_total'], label=f'{state} Property Crime', color=colors['property_crime'])

    plt.xlabel('Year')
    plt.ylabel('Rate per 100,000 population')
    plt.title('Incarceration, Violent Crime, and Property Crime Rates Over the Years')
    plt.legend()
    # Show the plot in the Streamlit app
    st.pyplot(plt.gcf())

    st.write('These are bar plots showcasing the top 5 states by average incarceration rate, violent crime rate, and property crime rate from 2001 to 2016. The states with the highest average incarceration rates may indicate regions with stricter law enforcement, higher crime rates, or policies that lead to more imprisonments. The States leading in violent crime rates may highlight areas with safety concerns. The top states in property crime rates could mean regions with particular challenges related to theft, burglary, or vandalism. These plots give insights into regional differences in crime and incarceration, which may require targeted interventions. Bear in mind that these analyses are based on the Top 5 States.')

    average_rates = crime_sorted.groupby('jurisdiction')[['incarceration_rate', 'violent_crime_rate', 'property_crime_rate']].mean()
    
    # Creating bar plots for average rates
    fig, axs = plt.subplots(3, 1, figsize=(10, 10))

    # Incarceration rate
    top_incarceration_states = average_rates['incarceration_rate'].sort_values(ascending=False)[:5]
    axs[0].barh(top_incarceration_states.index, top_incarceration_states.values, color='blue')
    axs[0].set_xlabel('Average Incarceration Rate per 100,000 population (2001-2016)')
    axs[0].set_title('Top 5 States by Average Incarceration Rate')

    # Violent crime rate
    top_violent_crime_states = average_rates['violent_crime_rate'].sort_values(ascending=False)[:5]
    axs[1].barh(top_violent_crime_states.index, top_violent_crime_states.values, color='red')
    axs[1].set_xlabel('Average Violent Crime Rate per 100,000 population (2001-2016)')
    axs[1].set_title('Top 5 States by Average Violent Crime Rate')

    # Property crime rate
    top_property_crime_states = average_rates['property_crime_rate'].sort_values(ascending=False)[:5]
    axs[2].barh(top_property_crime_states.index, top_property_crime_states.values, color='green')
    axs[2].set_xlabel('Average Property Crime Rate per 100,000 population (2001-2016)')
    axs[2].set_title('Top 5 States by Average Property Crime Rate')

    plt.tight_layout()
    st.pyplot(fig)

    #3 Heatmap Viz and Explanation
    st.write('This correlation heatmap shows the relationships between prisoner count, incarceration rate, violent crime rate, and property crime rate. A moderate positive correlation (0.32) exists between the prisoner count and the incarceration rate. This means states with higher prisoner counts tend to have higher incarceration rates, and vice versa. The violent and property crime rates have a strong positive correlation (0.56), meaning states with higher violent crime rates also tend to have higher property crime rates. From this visualization, we can deduce that since there is a moderate positive correlation between incarceration and crime rates, it may suggest that regions with higher crime rates have more incarcerations. The correlations between violent and property crime rates help us understand how these different types of crimes interact. Since there is a strong positive correlation, it might suggest that regions with higher violent crime rates also tend to have higher property crime rates. These insights can guide further investigation, policy decisions, or crime prevention strategies.')

    # Calculating the correlation matrix
    correlation_matrix = crime_sorted[['prisoner_count', 'incarceration_rate', 'violent_crime_rate', 'property_crime_rate']].corr()

    # Create a heatmap
    plt.figure(figsize=(8, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
    plt.title('Heatmap of Crime Metrics Correlations')
    st.pyplot(plt.gcf())





