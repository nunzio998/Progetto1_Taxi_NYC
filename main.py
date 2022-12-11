import DataAnalyses
from TaxiTripFile import *
from DataAnalyses import *
import streamlit as st
import time
from calendar import monthrange

if __name__ == '__main__':
    start = time.perf_counter()

    # anno e mese selezionato
    year = '2022'
    month = '02'

    zoneFilePath = "data/taxi+_zone_lookup.csv"
    tripFilePath = f"data/yellow_tripdata_{year}-{month}.parquet"

    # Check TripDataframe con partenza e arrivi in Zonefile (Gennaio-2022)
    dataSet_Trip = DataAnalyses(zoneFilePath, tripFilePath, year, month)

    print(dataSet_Trip.getBoroughAverageDataFrame(),"\n","-----------------------------")
    print(dataSet_Trip.getNewYorkAverageDataFrame(), "\n", "-----------------------------")

    end = time.perf_counter()
    print(f"Tempo di esecuzione: {round(end - start, 3)}")
