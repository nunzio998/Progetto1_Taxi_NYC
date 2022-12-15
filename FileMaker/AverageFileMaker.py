import pandas as pd

from Analisi.DataAnalyses import DataAnalyses


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
        """
        metodo che scorre tutti gli anni selezionati e per ognuno di essi richiama il metodo generateYearDataFrame
        e 'riempie' l'elemento con chiave 'anno' nel dizionario di dataframe col relativo dataframe.
        :return:
        """
        for anno in self.yearsList:
            self.dataFrames[anno] = self.generateYearDataframe(anno)

    def generateYearDataframe(self, year) -> pd.DataFrame:
        '''
        Metodo che genera il dataframe relativo all'anno dato in input al metodo.
        :param year:
        :return:
        '''
        yearDataFrame = []
        for month in self.monthsList:
            print(year,month)
            dtToAdd = DataAnalyses(self.zoneFilePath,
                                   f"data/trip/{year}/yellow_tripdata_{year}-{month}.parquet",
                                   year, month).getBoroughAverageDataFrame()
            dtToAdd2 = DataAnalyses(self.zoneFilePath,f"data/trip/{year}/yellow_tripdata_{year}-{month}.parquet",
                                    year, month).getNewYorkAverageDataFrame()
            dtToAdd = pd.concat([dtToAdd, dtToAdd2], axis=0, ignore_index=True)
            yearDataFrame.append(dtToAdd)
        yearDataFrame = self.mergeDataFrames(yearDataFrame)
        return yearDataFrame

    def getDataFrames(self):
        """
        Metodo che ritorna il dizionario contenente i dataframe di tutti gli anni selezionati
        dall'utente.
        :return:
        """
        return self.dataFrames

    def getYearDataFrame(self, year):
        """
        Metodo che ritorna il dataframe relativo all'anno selezionato in input
        :param year:
        :return:
        """
        return self.dataFrames[year]

    def mergeDataFrames(self, dt):
        """
        Metodo che aggiunge gli elementi del secondo dataframe al primo e lo restituisce
        :param dt:
        :return:
        """
        dt = pd.concat(dt, ignore_index=True)
        return dt

    def writeFiles(self):
        """
        Metodo che si occupa di scrivere un unico file csv relativo alle medie (average.csv) che contenga tutti i
        dataframe memorizzati nel dizionario di dataframe.
        :return:
        """
        dtTmp = []
        for anno in self.dataFrames.keys():
            dtTmp.append(self.dataFrames[anno])
            # self.dataFrames[anno].to_csv(f"output/average_{anno}.csv")
            # istruzione per scrivere file diversi per ogni anno
        dtTmp = self.mergeDataFrames(dtTmp)
        dtTmp.to_csv(f"output/average.csv")
