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
        self.numZones = len(self.taxiZone.getDataFrame())
        self.taxiTrip = self.checkedFile(TaxiTripFile(taxiTripFileName), self.numZones)

    @classmethod
    def checkedFile(cls, taxiTripObject, numZones) -> TaxiTripFile:
        """
        Metodo statico invocato nel construttore che controlla se ogni locationId (PU o DO) è
        compreso nel numero di borough presenti nella città di NewYork o di una qualsiasi città.
        :param taxiTripObject:
        :param taxiZoneObject:
        :return:
        """
        objPulito = taxiTripObject
        i = 0
        while i < len(taxiTripObject.getDataFrame()):
            if objPulito.getDataFrame()['PULocationID'].get(i) < 0 or objPulito.getDataFrame()['PULocationID'].get(i) > numZones:
                objPulito.getDataFrame().drop(i)
                #print('ELIMINATO!!!!!!!!', pulito['PULocationID'].get(i))
            if objPulito.getDataFrame()['DOLocationID'].get(i) < 0 or objPulito.getDataFrame()['DOLocationID'].get(i) > numZones:
                objPulito.getDataFrame().drop(i)
                #print('ELIMINATO!!!!!!!!', pulito['PULocationID'].get(i))
            i += 1
        return objPulito

    def getTaxiTripDataFrame(self) -> pd.DataFrame :
        return self.taxiTrip.getDataFrame()

    def getTaxiZoneDataFrame(self) -> pd.DataFrame:
        return self.taxiZone.getDataFrame()
