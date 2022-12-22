import pandas as pd
import streamlit as st


class TaxiTripFile:
    """
    La classe TaxiTripFile ha il compito di leggere il file parquet relativo ai borough di NewYork
    e fornire il medoto per recuperare tale dato.
    """
    def __init__(self, file):
        try:
            self.dataFrame = pd.read_parquet(file)
        except FileNotFoundError:
            st.warning("Invalid selected parameters.")

    def getDataFrame(self) -> pd.DataFrame:
        """
        Ritorna il dataframe relativo al file passato al costruttore della classe
        :return: DataFrame of the input file
        """
        return self.dataFrame
