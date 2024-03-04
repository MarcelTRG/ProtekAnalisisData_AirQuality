# Air Quality Analysis Dicoding Project: Aotizhongzin Station

## Project Overview
This project was created to fullfill the criteria to pass the course "Belajar Data Analysis dengan Python" from Dicoding. It focuses on analyzing air quality data in that Aotizhongxing staion and gives me a general view of the pollutan in the course of 2013 to 2017 

## Live Dashboard
https://pwubwr8hbqqebq7jldw6ef.streamlit.app/

## Data Source
The dataset used in this project was provided by Dicoding. I use the Aotizhongxing air quality data

## Libraries Used
- Streamlit
- Pandas
- Matplotlib
- Seaborn
- NumPy

## How to Run the Dashboard

To run the Air Quality Analysis Dashboard, follow these steps:

### Setup Environment

1. **Create and Activate a Python Environment**:
   - You could use venv which is standard Python environment tool directly on VS Code:
     ```
     python -m venv [environment_name]
     source [environment_name]/bin/activate  # On Windows use `[environment_name]\Scripts\activate`
     ```

2. **Install Required Packages**:
   - The following packages are necessary for running the analysis and the dashboard:
     ```
     pip install pandas numpy matplotlib seaborn streamlit
     ```

     or you can do
     ```
     pip install -r requirements.txt
     ```
### Run the Streamlit App

1. **Navigate to the Project Directory** where `dashboard.py` is located.

2. **Run the Streamlit App**:
    ```
    cd Board
    streamlit run dashboard.py
    ```

### Additional Files

- The dataset used for this analysis is included in the Dashboard FOlder while the one that has been processed cpuld be found om Data CVS Folder.
- A detailed Python notebook (`Proyek_Analisis_Data.ipynb`) containing the data analysis and visualizations is also provided.
---
### Side Note.
Make sure to change [environment_name] when you create the virtual environment to whatever you want. In this project, i did create Virtual Environment named ProyekAoti. You could delete it and create your own named for the environment.

Since the 'dashnoard.py' and 'requirement.txt need' to be in the same folder so it's easier to run the "pip install" command' i have moved the requirement.txt file to the Board folder 

For the IPYNB File that was provided in this submission, i suggest that the teacher or the one that grade this submission to run it in Goofle Collabs, because it much easier there

In the python file "dashboard.py", make sure to change the path for the data read [Line 10] to whereever you save this project in your computer
---

## About Me
- **Name**: Marcel Adila Jufai
- **Email Address**: marceljufai9503@gmail.com
- **Dicoding ID**: marceljufai
