from Analisi.DataAnalyses import DataAnalyses
import datetime
import streamlit as st


def checkDatetimeFile(year, month):
    """
    Funzione che gestisce la restituisce un messaggio di errore
    nel caso si richiede la visualizzazione di un anno un mese anomalo
    :param strMonth:
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
    già analizzato ma presente nel daatset lcoale
    :param yearsList:
    :param monthsList:
    :param monthsDict:
    :return:
    """
    months_number = []

    for month in monthsList:
        if month in monthsDict:
            months_number.append(f'{monthsDict[month]:02d}')
    for year in yearsList:
        for month in months_number:
            try:
                DataAnalyses(year, month)
            except FileNotFoundError:

                checkDatetimeFile(year, month)
                return False
    return True
