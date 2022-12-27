import os
import pandas as pd
from Analisi.DataAnalyses import DataAnalyses


class AverageFileMaker:
    """
    Questa classe viene istanziata durante l'esecuzione passando come parametri le liste di anni e mesi che si vogliono
    analizzare. Per ogni anno-mese questa classe istanzia DataAnalyses con la quale viene creato il dataframe relativo
    a quel mese di quell'anno, che viene poi aggiunto ad una lista dataframes che verrà infine concatenata al fine di
    ottenere un unico dataframe. Con il seguente dataframe verrà infine realizzato e archiviato il file .csv dei dati
    analizzati.
    In caso venisse rieseguito un programma che dia in ingresso una lista di anni e una lista di mesi, questa classe fa
    l'analisi e archivia solamente i dati relativi ai parametri di ingresso che non erano già stati analizzati e
    archiviati in precedenza
    """

    def __init__(self, yearsList, monthsList):
        self.yearsList = yearsList
        self.monthsList = monthsList

    @classmethod
    def isInCsv(cls, year: str, month: str) -> bool:
        """
        Metodo che prende in ingresso due stringhe rappresentanti anno e mese di cui è richiesto il check
        e restituisce un valore booleano che indica se il mese dell'anno ha una corrispondenza nel file average.csv
        con un'analisi già svolta

        :param year: str di 4 caratteri: l'anno di cui è richiesto il check
        :param month: str di 2 caratteri: il mese di cui è richiesto il check
        :return: bool True se il mese dell'anno ha una corrispondenza nel file average.csv, False altrimenti
        """
        average = pd.read_csv("./output/average.csv")
        return f"{year}-{month}" in set(average["year-month"])

    def generateListDataframe(self) -> list:
        """
        Metodo che genera una lista di dataframes relativi al parametri di ingresso integrando, se già calcolati in
        precedenza, i dati già archiviati.
        :return: lista di dataframe analizzati
        """
        exists_path = os.path.exists("output/average.csv")
        listDataFrame = []
        for year in self.yearsList:
            for month in self.monthsList:
                # se l'analisi mese-anno correnti è già presente nel file csv nel caso salta all'iterazione successiva
                if exists_path and self.isInCsv(year, month):
                    continue
                dtToAdd = DataAnalyses(year, month).getBoroughAverageDataFrame()
                listDataFrame.append(dtToAdd)
        return listDataFrame

    def writeFiles(self):
        """
        Metodo che si occupa di:
         - verificare se esiste una directory ./output e in caso se esiste un file average.csv, in caso contrario
           le crea
         - scrivere un unico file csv relativo alle medie (average.csv) che contenga tutti i
           dataframe memorizzati nella lista di dataframes.
        :return:
        """
        listToConcat = self.generateListDataframe()
        # se ci sono righe da scrivere nel file average.csv, le scrive in coda

        if listToConcat:
            dtTmp = pd.concat(listToConcat, ignore_index=True)
            if os.path.exists("output/"):
                if os.path.exists("output/average.csv"):
                    dtEx = pd.read_csv("output/average.csv", index_col=0)
                    dtEx["year-month"] = pd.to_datetime(dtEx["year-month"]).dt.to_period("M")
                    dtTmp = pd.concat([dtEx, dtTmp], ignore_index=True)
            else:
                os.mkdir("output/")
            dtTmp = dtTmp.sort_values(by="year-month").reset_index(drop=True)
            dtTmp.to_csv("output/average.csv")
