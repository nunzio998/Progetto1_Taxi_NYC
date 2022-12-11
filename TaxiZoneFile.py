import pandas as pd


class TaxiZoneFile:

    def __init__(self, file):
        self.dataFrame = pd.read_csv(file)

    def getDataFrame(self) -> pd.DataFrame:
        """
        Ritorna il dataframe relativo al file passato al costruttore della classe
        :return: DataFrame of the input file
        """
        return self.checkDataFrame(self.dataFrame)

    @classmethod
    def checkDataFrame(cls, inputDataFrame) -> bool:
        """
        Effettua il check del data frame in input con conseguente
        gestione di valori e della loro coerenza.
        Si decide di eliminare eventuali valori NaN o Unknown.
        :param cls:
        :param inputDataFrame:
        :return:
        """
        return inputDataFrame
