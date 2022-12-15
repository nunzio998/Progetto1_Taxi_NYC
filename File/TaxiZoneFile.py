import pandas as pd


class TaxiZoneFile:
    """
    La classe TaxiZoneFile ha il compito di leggere il file csv relativo ai borough di NewYork
    e fornire il medoto per recuperare tale dato.
    """

    def __init__(self, file):
        self.dataFrame = pd.read_csv(file)

    def getDataFrame(self) -> pd.DataFrame:
        """
        Ritorna il dataframe relativo al file passato al costruttore della classe
        :return: DataFrame of the input file
        """
        return self.dataFrame
