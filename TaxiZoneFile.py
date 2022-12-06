import pandas as pd
import numpy as np

class TaxiZoneFile:

    def __init__(self, file):
        self.file = pd.read_csv(file)

    def getDataFrame(self) -> pd.DataFrame:
        """
        Ritorna il dataframe relativo al file passato al costruttore della classe
        :return: DataFrame of the input file
        """
        return self.file

    def checkDataFrame(self, dataFrame) -> bool:
        """
        Effettua il check del data frame in input con conseguente
        gestione di valori e della loro coerenza
        :param dataFrame:
        :return:
        """
        return True