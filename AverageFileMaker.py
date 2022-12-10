import pandas as pd

from DataAnalyses import DataAnalyses


class AverageFileMaker:
    """
    Questa classe viene istanziata durante l'esecuzione passando come parametri le liste di anni e mesi che voglio
    analizzare. Per ogni anno-mese questa classe istanzia DataAnalyses con la quale viene creato il dataframe relativo
    a quel mese di quell'anno, che viene poi aggiunto ad un dizionario di dataframes che conterrà coppie
    anno-dataframes. Con il seguente dizionario verranno poi generati i file csv relativi ad ogni anno selezionato.
    """

    def __init__(self, yearsList, monthsList):
        self.yearsList = yearsList
        self.monthsList = monthsList
        self.dataFrames = {}
        for anno in self.yearsList:
            self.dataFrames[anno] = pd.DataFrame.empty  # dataframe sul quale aggiungo i risultati delle varie analisi
        self.zoneFilePath = "data/zone/taxi+_zone_lookup.csv"

    def fillDataFrames(self):
        for anno in self.yearsList:
            self.dataFrames[anno] = self.generateYearDataframe(anno)

    def generateYearDataframe(self, year) -> pd.DataFrame:
        yearDataFrame = pd.DataFrame({"year-month": [],
                                      "borough": [],
                                      "average": []
                                      })
        for month in self.monthsList:
            dtToAdd = DataAnalyses(self.zoneFilePath,
                                   f"data/trip/{year}/yellow_tripdata_{year}-{month}.parquet",
                                   year, month).getBoroughAverageDataFrame()
            yearDataFrame = self.mergeDataFrames(yearDataFrame, dtToAdd)
        return yearDataFrame

    def makeFiles(self):  # TODO metodo da implementare
        # richiama fillDataFrames()
        pass

    def getDataFrames(self):
        return self.dataFrames

    def getYearDataFrame(self, year):
        return self.dataFrames[year]

    def mergeDataFrames(self, dt1, dt2):  # FIXME il metodo non funziona correttamente
        """
        Metodo che aggiunge gli elementi del secondo dataframe al primo e lo restituisce
        :param dt1:
        :param dt2:
        :return:
        """
        for i in range(len(dt2)):
            dt1.append(dt2.loc[i])
        return dt1
