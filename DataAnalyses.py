import pandas as pd
import numpy as np
import matplotlib as pl

from TaxiTripFile import TaxiTripFile
from TaxiZoneFile import TaxiZoneFile


class DataAnalyses:
    """
    La classe istanzia le classi relative al file .parquet e al .css e tramite i metodi
    di queste classi recupera i dati di cui necessita per effettuare le analisi necessarie.
    """

    def __init__(self, taxiZoneFileName, taxiTripFileName):
        """
        il costruttore di questa classe riceve in input i nomi dei file con i quali
        istanzia i due oggetti che userà in seguito per effettuare l'analisi dati.
        :param taxiTripFileName:
        :param taxiZoneFileName:
        """
        self.taxiZone = TaxiZoneFile(taxiZoneFileName)
        self.taxiTrip = self.checkedFile(TaxiTripFile(taxiTripFileName), self.taxiZone)

    @classmethod
    def checkedFile(cls, taxiTripObject, taxiZoneObject) -> TaxiTripFile:
        """
        Metodo statico invocato nel construttore che controlla se ogni locationId (PU o DO) è
        compreso nel numero di borough presenti nella città di NewYork o di una qualsiasi città.
        :param taxiTripObject:
        :param taxiZoneObject:
        :return:
        """

        objPulito = taxiTripObject
        Min_locationID, Max_locationID = np.min(np.array(taxiZoneObject.getDataFrame()['LocationID'])), \
                                         np.max(np.array(taxiZoneObject.getDataFrame()['LocationID']))
        PULocation = np.array(objPulito.getDataFrame()['PULocationID'])
        DOLocation = np.array(objPulito.getDataFrame()['DOLocationID'])

        for i in range(len(objPulito.getDataFrame())):
            if not (Min_locationID <= PULocation[i] <= Max_locationID) or not (Min_locationID <= DOLocation[i] <= Max_locationID):
                objPulito.getDataFrame().drop(i)
        return objPulito

    def getTaxiTripDataFrame(self) -> pd.DataFrame:
        return self.taxiTrip.getDataFrame()

    def getTaxiZoneDataFrame(self) -> pd.DataFrame:
        return self.taxiZone.getDataFrame()
