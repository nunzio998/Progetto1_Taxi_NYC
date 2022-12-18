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
        self.zoneFilePath = "data/zone/taxi+_zone_lookup.csv"

    def generateListDataframe(self) -> list:
        """
        Metodo che genera il dataframe relativo all'anno dato in input al metodo.
        :param year:
        :return:
        """
        listDataFrame = []
        for year in self.yearsList:
            for month in self.monthsList:
                print(year, month)
                dtToAdd = DataAnalyses(self.zoneFilePath,
                                       f"data/trip/{year}/yellow_tripdata_{year}-{month}.parquet",
                                       year, month).getBoroughAverageDataFrame()
                listDataFrame.append(dtToAdd)
        return listDataFrame

    def writeFiles(self):
        """
        Metodo che si occupa di scrivere un unico file csv relativo alle medie (average.csv) che contenga tutti i
        dataframe memorizzati nel dizionario di dataframe.
        :return:
        """
        listToConcat = self.generateListDataframe()
        dtTmp = pd.concat(listToConcat, ignore_index=True)
        dtTmp.to_csv(f"output/average.csv")
