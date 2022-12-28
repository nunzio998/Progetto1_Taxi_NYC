import datetime
import os

import streamlit as st


def checkDatetimeFile(year, month):
    """
    Funzione che gestisce la restituisce un messaggio di errore
    nel caso si richiede la visualizzazione di un anno un mese anomalo
    :param year:
    :param month:
    :return:
    """
    dt_selected = datetime.datetime.strptime(f'{year}-{month}', '%Y-%m')
    dt_today = datetime.datetime.combine(datetime.date.today(), datetime.time(0, 0))
    if dt_selected > dt_today:
        return st.warning('We are not here to predict the future', icon="🔮")
    else:
        return st.warning(f'Some files related to your request are not in your dataset', icon="⚠️")


def check_dataset(yearsList: list, monthsList: list, monthsDict: dict):
    """
    Funzione che fa l'analisi in caso di richiesta di un anno o un mese non
    già analizzato ma presente nel datset locale
    :param yearsList: lista di anni sui quali si vuole eseguire l'analisi
    :param monthsList: lista di mesi sui quali si vuole eseguire l'analisi
    :param monthsDict: dizionario per la conversione della lista di mesi (Jan, Feb, Mar...) in (01, 02, 03,...)
    :return:
    """
    months_number = []

    for month in monthsList:
        if month in monthsDict:
            months_number.append(f'{monthsDict[month]:02d}')
    for year in yearsList:
        for month in months_number:
            if not os.path.isfile(f"data/trip/{year}/yellow_tripdata_{year}-{month}.parquet"):
                checkDatetimeFile(year, month)
                return False
    return True
