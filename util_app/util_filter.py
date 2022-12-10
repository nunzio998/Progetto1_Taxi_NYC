import streamlit as st
import pandas as pd


def filter_data(source, years_selected, month_selected, monthsDict, Bronx_check, Brooklyn_check, EWR_check,
                Manhattan_check, Queens_check, Staten_Island_check, Unknown_check):
    months_number = []

    for month in month_selected:
        if month in monthsDict:
            months_number.append(monthsDict[month])

    sourceFiltered = []
    # Filter on years, month
    for year in years_selected:
        for month in months_number:
            sourceFiltered.append(source[~(source['year-month'] != f'{year}-{month:02d}')].reset_index(drop=True))

    sourceFiltered = pd.concat(sourceFiltered, ignore_index=True)

    # Filter on Borough
    if not Bronx_check:
        sourceFiltered.drop(sourceFiltered[sourceFiltered['borough'] == 'Bronx'].index, inplace=True)
    if not Brooklyn_check:
        sourceFiltered.drop(sourceFiltered[sourceFiltered['borough'] == 'Brooklyn'].index, inplace=True)
    if not EWR_check:
        sourceFiltered.drop(sourceFiltered[sourceFiltered['borough'] == 'EWR'].index, inplace=True)
    if not Manhattan_check:
        sourceFiltered.drop(sourceFiltered[sourceFiltered['borough'] == 'Manhattan'].index, inplace=True)
    if not Queens_check:
        sourceFiltered.drop(sourceFiltered[sourceFiltered['borough'] == 'Queens'].index, inplace=True)
    if not Staten_Island_check:
        sourceFiltered.drop(sourceFiltered[sourceFiltered['borough'] == 'Staten Island'].index, inplace=True)
    if not Unknown_check:
        sourceFiltered.drop(sourceFiltered[sourceFiltered['borough'] == 'Unknown'].index, inplace=True)


    return sourceFiltered
