import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Title Page
st.set_page_config(page_title="Air Quality Analysis of Aotizhongxin stations by Marcel Adila Jufai")

# Data Read
Data_path = 'Data CVS/Aoti.csv'
Aoti = pd.read_csv(Data_path)

# Dashboard Tittle
st.title('Air Quality in Aotizhongxiang Stations')

st.write("This Dashboard was created to fullfill the criteria needed to pass Dicoding Course: Belajar Analisis Data dengan Python")

st.markdown("""
### About Me
- **Name**: Marcel Adila Jufai
- **Email**: marceljufai9503@gmail.com
- **Dicoding ID**: marceljufai
            
### Project Overview
This dashboard will gives you the result of my analysis of air quality data Aotizhongxu station. This Dashboard will shown the difference of pollutant concentration [NO2, SO2, O3, CO] while also shown you the percentage of each pollutant the period of a year
""")

# Input Section for User
st.subheader("Input the year and month of the data you want to know")
select_year = st.selectbox('Select The year', list(Aoti['year'].unique()))
select_month = st.selectbox('Select The month', list(Aoti['month'].unique()))

# Filtered the data as the User inputed
data_select = Aoti[(Aoti['year'] == select_year) & (Aoti['month'] == select_month)].copy()

# Displaying data statistics
st.subheader('Data Overview')
st.write(data_select.describe())
st.subheader('Data Overview for Selected Period')
st.write(data_select.head())

# Shown the linechart for pollutant concentration throught out the Year and month
st.subheader('Line chart for pollutant concentration throughtout the year')

# Filtering the data to the year that the user input
pollutant_select = st.selectbox('Select The Pollutant', ['NO2', 'SO2', 'O3', 'CO'])
Aoti_year = Aoti[Aoti['year'] == select_year]
st.write(f'Data Result for {select_year}')
st.write(Aoti_year)

Pollutant_level = Aoti_year.groupby('month')[pollutant_select].mean()
#Pollutant_level = Aoti_year.groupby('month')['O3'].mean()
st.write(f'The Mean Result of the whole month in {select_year}')
st.write(Pollutant_level)

#V Visualize the data to a line chart
st.write('- The graph Result -')
plt.figure(figsize=(10, 6))
Pollutant_level.plot(kind='line', marker='o', color='skyblue', linestyle='-')
plt.title(f'{pollutant_select} Concentration on Aotizhongxu Station in the year {select_year}')
plt.xlabel('Month')
plt.ylabel(f'Mean of {pollutant_select}')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

st.pyplot(plt)

# Using the piechart to show the pollutant concentration
st.subheader('Pollutant Percentage Throughtout The Year')
data_column = ['SO2', 'NO2', 'CO', 'O3']
data_select = Aoti_year[data_column]
st.write(f'Pollutant data recorded from Aoutizhongxin station in {select_year}')
st.write(data_select)

sum_values = data_select.sum()
st.write(f'Mean of the pollutant concentration in {select_year}')
st.write(sum_values)

st.write('- The graph Result -')
plt.figure(figsize=(8, 8))
plt.pie(sum_values, labels=sum_values.index, autopct='%1.1f%%', startangle=140)
plt.title(f'Distribution of Air Pollutants in {select_year}')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

st.pyplot(plt)