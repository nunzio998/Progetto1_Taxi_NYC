import pandas as pd
import numpy as pd
import matplotlib as pl

from TaxiTripFile import TaxiTripFile
from TaxiZoneFile import TaxiZoneFile


class DataAnalyses:
    """
    La classe istanzia le classi relative al file .parquet e al .css e tramite i metodi
    di queste classi recupera i dati di cui necessita per effettuare le analisi necessarie.
    """

    def __init__(self, taxiTripFile, taxiZoneFile):
        """
        il costruttore di questa classe riceve in input i nomi dei file con i quali
        istanzia i due oggetti che userà in seguito per effettuare l'analisi dati.
        :param taxiTripFile:
        :param taxiZoneFile:
        """
        self.taxiTrip = TaxiTripFile(taxiTripFile)
        self.taxiZone = TaxiZoneFile(taxiZoneFile)
