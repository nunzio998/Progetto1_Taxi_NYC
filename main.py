import pandas as pd

from DataAnalyses import *
import time


if __name__ == '__main__':

    start = time.perf_counter()

    # anno e mese selezionato
    years = ['2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021']
    months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
    append_dataFrames = []
    for year in years:
        for month in months:
            print(month, year)
            zoneFilePath = "data/zone/taxi+_zone_lookup.csv"
            tripFilePath = f"data/trip/{year}/yellow_tripdata_{year}-{month}.parquet"

            # Check TripDataframe con partenza e arrivi in Zonefile (Gennaio-2022)
            dataSet_Trip = DataAnalyses(zoneFilePath, tripFilePath, year, month)

            dfTrip = dataSet_Trip.getBoroughAverageDataFrame()

            append_dataFrames.append(dfTrip)

    dfResult = pd.concat(append_dataFrames, ignore_index=True)

    dfResult.to_csv('results/data.csv')

    print(dfResult)

    end = time.perf_counter()
    print(f"Tempo di esecuzione: {round(end - start, 3)}")


