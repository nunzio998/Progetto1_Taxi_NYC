import os

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
        Metodo che genera il dataframe relativo all'anno dato in input al metodo.
        :return:
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
        Metodo che si occupa di scrivere un unico file csv relativo alle medie (average.csv) che contenga tutti i
        dataframe memorizzati nel dizionario di dataframe.
        :return:
        """
        listToConcat = self.generateListDataframe()
        # se ci sono righe da scrivere nel file average.csv, le scrive in coda
        dtTmp = pd.concat(listToConcat, ignore_index=True)
        if listToConcat and os.path.exists("output/average.csv"):
            dtEx = pd.read_csv("output/average.csv", index_col=0)
            dtTmp = pd.concat([dtEx, dtTmp], ignore_index=True)
        if not os.path.exists("output/"):
            os.mkdir("output/")
        dtTmp.to_csv("output/average.csv")
