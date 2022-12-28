import pandas as pd


class TaxiTripFile:
    """
    La classe TaxiTripFile ha il compito di leggere il file parquet relativo ai borough di NewYork
    e fornire il metodo per recuperare tale dato.
    """
    def __init__(self, file):
        self.dataFrame = pd.read_parquet(file)

    def getDataFrame(self) -> pd.DataFrame:
        """
        Ritorna il dataframe relativo al file passato al costruttore della classe
        :return: DataFrame of the input file
        """
        return self.dataFrame
