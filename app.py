import altair as alt
import pandas as pd
import streamlit as st

st.set_page_config(layout='wide')

st.title('Taxi NYC')

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December']
month_selected = st.sidebar.multiselect(
    'Select months', months, months[0], help='Months to analyze'
)

# st.write('You selected:', month_selected)

years = list(range(2009, 2023))
years_selected = st.sidebar.multiselect(
    'Select years', years, years[len(years) - 1], help='Years to analyze'
)

# st.write('You selected:', years_selected)

st.sidebar.subheader('Select Borough')

Bronx_check = st.sidebar.checkbox('Bronx')
Brooklyn_check = st.sidebar.checkbox('Brooklyn')
EWR_check = st.sidebar.checkbox('EWR')
Manhattan_check = st.sidebar.checkbox('Manhattan')
Queens_check = st.sidebar.checkbox('Queens')
Staten_Island_check = st.sidebar.checkbox('Staten Island')
Unknown_check = st.sidebar.checkbox('Unknown')

source = pd.read_csv('./results/data.csv')



