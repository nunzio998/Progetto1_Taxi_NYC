import pandas as pd
import numpy as np


class TaxiTripFile:
    def __init__(self, file):
        self.file = pd.read_parquet(file)
        pass

    def getDataFrame(self) -> pd.DataFrame:
        """
        Ritorna il dataframe relativo al file passato al costruttore della classe
        :return: DataFrame of the input file
        """
        return self.file

    def getMonthDataFrame(self, month: str) -> pd.DataFrame:
        """
        restituisce il dataframe con i dati relativi al mese specificato.
        Utilizza la funzione di check prima di ritornare il dato
        :param month:
        :return:
        """
        pass

    def checkDataFrame(self, dataFrame) -> bool:
        """
        Effettua il check del data frame in input con conseguente
        gestione di valori e della loro coerenza
        :param dataFrame:
        :return:
        """
        return True
