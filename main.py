import DataAnalyses
from AverageFileMaker import AverageFileMaker
from TaxiTripFile import *
from DataAnalyses import *
import streamlit as st
import time
from calendar import monthrange

if __name__ == '__main__':
    analisi = AverageFileMaker(["2018"], ["01"])
    analisi.fillDataFrames()
    print(analisi.getYearDataFrame('2018'))
