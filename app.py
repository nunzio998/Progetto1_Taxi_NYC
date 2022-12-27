import datetime
import pandas as pd
import streamlit as st
from utils_app import util_chart, util_filter, util_mean, util_barChart, util_analyses, util_dataset

# main page settings: title, favicon, layout
st.set_page_config(page_title="Taxi NYC", page_icon=":oncoming_taxi:", layout='wide')

# data source path
source_path = 'output/average.csv'

st.title('Taxi NYC')

year = datetime.date.today().year
years = list(range(2009, year + 1))
years_selected = st.sidebar.multiselect(
    'Select years', years[::-1], years[-3:-1], help='Years to analyze'
)

# month sidebar select-box
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December']

monthsDict = dict(zip(months, range(1, 13)))

months_selected = st.sidebar.multiselect(
    'Select months', months, months[:4], help='Months to analyze'
)

# borough sidebar check-box
st.sidebar.subheader('Select Borough')
Bronx_check = st.sidebar.checkbox('Bronx', value=True)
Brooklyn_check = st.sidebar.checkbox('Brooklyn', value=True)
EWR_check = st.sidebar.checkbox('EWR', value=True)
Manhattan_check = st.sidebar.checkbox('Manhattan', value=True)
Queens_check = st.sidebar.checkbox('Queens', value=True)
Staten_Island_check = st.sidebar.checkbox('Staten Island', value=True)
Unknown_check = st.sidebar.checkbox('Unknown', value=True)

# main dynamic page body
if util_dataset.check_dataset(years_selected, months_selected, monthsDict):
    util_analyses.check_analyses(years_selected, months_selected, monthsDict)

    if years_selected == [] or months_selected == []:

        st.warning('Select at least one month and one year', icon="⚠️")
    else:
        if Bronx_check or Brooklyn_check or EWR_check or Manhattan_check or Queens_check or Staten_Island_check or Unknown_check:
            source = pd.read_csv(source_path, index_col=0)
            source_filtered = util_filter.filter_data(source, years_selected, months_selected, monthsDict,
                                                      Bronx_check,
                                                      Brooklyn_check,
                                                      EWR_check, Manhattan_check, Queens_check,
                                                      Staten_Island_check,
                                                      Unknown_check)
            util_chart.line_chart(source_filtered)
            st.subheader(util_mean.meanPeriodBoroughSelected(source_filtered))
            util_barChart.bar_chart(source_filtered, monthsDict)
        else:
            st.warning('Select at least one borough', icon="⚠️")

else:
    pass
