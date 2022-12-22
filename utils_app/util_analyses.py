from FileMaker.AverageFileMaker import AverageFileMaker
import streamlit as st


def check_analyses(yearsList: list, monthsList: list, monthsDict: dict ):
    months_number = []

    for month in monthsList:
        if month in monthsDict:
            months_number.append(f'{monthsDict[month]:02d}')
    analisi = AverageFileMaker(yearsList, months_number)
    analisi.writeFiles()


