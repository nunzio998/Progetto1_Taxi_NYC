import pandas as pd


class TaxiTripFile:
    def __init__(self, file):
        self.dataFrame = pd.read_parquet(file)

    def getDataFrame(self) -> pd.DataFrame:
        """
        Ritorna il dataframe relativo al file passato al costruttore della classe
        :return: DataFrame of the input file
        """
        return self.dataFrame

    def getCheckedDataFrame(self) -> pd.DataFrame:
        """
        Ritorna il dataframe 'pulito' relativo al file passato al costruttore della classe
        :return: DataFrame of the input file
        """
        return self.checkDataFrame(self.dataFrame)

    @classmethod
    def checkDataFrame(cls, dataFrame) -> pd.DataFrame:
        """
        Effettua il check del data frame in input con conseguente
        gestione di valori e della loro coerenza
        :param dataFrame:
        :return:
        """
        return dataFrame
