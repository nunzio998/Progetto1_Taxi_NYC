import datetime

import altair as alt
import pandas as pd
import streamlit as st
from util_app import util_chart, util_filter
import getData


source_path = 'C:/Users/matte/Desktop/Magistrale/Programmazione/Guarrasi/Progetto1_Taxi_NYC/results/data.csv'
source = pd.read_csv(source_path, index_col=0)

st.set_page_config(layout='wide')

st.title('Taxi NYC')

year = datetime.date.today().year
years = list(range(2018, year+1))
years_selected = st.sidebar.multiselect(
    'Select years', years, years[:3], help='Years to analyze'
)

# st.write('You selected:', years_selected)

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December']

monthsDict = dict(zip(months, range(1, 13)))

months_selected = st.sidebar.multiselect(
    'Select months', months, months[:5], help='Months to analyze'
)

# st.write('You selected:', month_selected)

st.sidebar.subheader('Select Borough')

Bronx_check = st.sidebar.checkbox('Bronx', value=True)
Brooklyn_check = st.sidebar.checkbox('Brooklyn', value=True)
EWR_check = st.sidebar.checkbox('EWR', value=True)
Manhattan_check = st.sidebar.checkbox('Manhattan', value=True)
Queens_check = st.sidebar.checkbox('Queens', value=True)
Staten_Island_check = st.sidebar.checkbox('Staten Island', value=True)
Unknown_check = st.sidebar.checkbox('Unknown', value=True)


source_filtered = util_filter.filter_data(source, years_selected, months_selected, monthsDict, Bronx_check, Brooklyn_check,
                                          EWR_check, Manhattan_check, Queens_check, Staten_Island_check, Unknown_check)

if Bronx_check or Brooklyn_check or EWR_check or Manhattan_check or Queens_check or Staten_Island_check or Unknown_check:
    util_chart.line_chart(source_filtered)
