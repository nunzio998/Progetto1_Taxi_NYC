from calendar import monthrange

import numpy as np
import pandas as pd

from File.TaxiTripFile import TaxiTripFile
from File.TaxiZoneFile import TaxiZoneFile


class DataAnalyses:
    """
    La classe istanzia le classi relative al file .parquet e al .css e tramite i metodi
    di queste classi recupera i dati di cui necessita per effettuare le analisi necessarie.
    """

    def __init__(self, taxiZoneFileName, taxiTripFileName, year, month):
        """
        il costruttore di questa classe riceve in input i nomi dei file con i quali
        istanzia i due oggetti che userà in seguito per effettuare l'analisi dati.
        :param taxiTripFileName:
        :param taxiZoneFileName:
        """
        self.taxiZone = TaxiZoneFile(taxiZoneFileName)
        self.taxiTrip = self.checkedFile(TaxiTripFile(taxiTripFileName), self.taxiZone)
        self.year = year
        self.month = month

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
            if not (Min_locationID <= PULocation[i] <= Max_locationID) or not (
                    Min_locationID <= DOLocation[i] <= Max_locationID):
                objPulito.getDataFrame().drop(i)
        return objPulito

    def getTaxiTripDataFrame(self) -> pd.DataFrame:
        """
        Metodo che ritorna il dataframe relativo al file parquet delle corse che si vuole analizzare e
        che si è dato in input al costruttore della classe al momento in cui essa è stata instanziata.
        :return:
        """
        return self.taxiTrip.getDataFrame()

    def getTaxiZoneDataFrame(self) -> pd.DataFrame:
        """
        Metodo che ritorna il dataframe relativo al file csv dei borough che si vuole analizzare e
        che si è dato in input al costruttore della classe al momento in cui essa è stata instanziata.
        :return:
        """
        return self.taxiZone.getDataFrame()

    def getBoroughAverageDataFrame(self) -> pd.DataFrame:
        """
        Metodo che calcola la media giornaliera di corse per ogni coppia mese-borough e restiuisce il
        DataFrame relativo.
        :return:
        """
        dataSet_Trip = self.getTaxiTripDataFrame()
        dataSet_Zone = self.getTaxiZoneDataFrame()

        # Estrazione di solo colonne: Data, partenza
        dfTrip = pd.DataFrame(dataSet_Trip, columns=['tpep_pickup_datetime', 'PULocationID'])

        # Dizionario con id_zona: Borough
        ZoneDict = dict(zip(dataSet_Zone.LocationID, dataSet_Zone.Borough))

        # Sostituzione id_zona con Borough
        dfTrip['PULocationID'] = dfTrip['PULocationID'].replace(ZoneDict)

        # groupby giornaliero e somma per borough
        dfTrip = dfTrip.groupby(
            by=[dfTrip['tpep_pickup_datetime'].dt.to_period('M'), 'PULocationID']).size().reset_index(
            name='count')

        # numero di giorni nel mese dell'anno selezionato per normalizzare la somma delle corse
        num_days = monthrange(int(self.year), int(self.month))[1]

        # normalizza su 30 il numero delle corse per borough (non faccio la media prima perchè potrebbe esserci un
        # borough in cui in un giorno non ci sono corse)
        dfTrip['count'] = round(dfTrip['count'].div(num_days)).astype(int)

        # Rimuove tutte le righe che non appartengono a mese e anno selezionato
        # Riassegna l'index da 0 a len(df) dopo aver rimosso non relative al mese in esame
        dfTrip = dfTrip[~(dfTrip['tpep_pickup_datetime'] != f'{self.year}-{self.month}')].reset_index(drop=True)

        # rinomino colonne dataframe
        dfTrip.columns = ['year-month', 'borough', 'average']
        return dfTrip

    def getNewYorkAverageDataFrame(self) -> pd.DataFrame:
        """
        Metodo che calcola la media di corse giornaliere di tutta la città di NewYork e restituisce il
        DataFrame relativo.
        :return:
        """
        dataSet_Trip = self.getTaxiTripDataFrame()
        dataSet_Zone = self.getTaxiZoneDataFrame()

        # Estrazione di solo colonne: Data, partenza
        dfTrip = pd.DataFrame(dataSet_Trip, columns=['tpep_pickup_datetime', 'PULocationID'])

        # groupby mensile
        dfTrip = dfTrip.groupby(by=dfTrip['tpep_pickup_datetime'].dt.to_period('M'))\
            .size().reset_index(name='count')

        # Rimuove tutte le righe che non appartengono a mese e anno selezionato
        # Riassegna l'index da 0 a len(df) dopo aver rimosso le righe non relative al mese in esame
        dfTrip = dfTrip[dfTrip['tpep_pickup_datetime'] == f'{self.year}-{self.month}'].reset_index(drop=True)

        # numero di giorni del mese dell'anno selezionato per normalizzare la somma delle corse
        num_days = monthrange(int(self.year), int(self.month))[1]

        # normalizza il numero delle corse sul numero di giorni del mese
        dfTrip['count'] = round(dfTrip['count'].div(num_days)).astype(int)

        # rinomino colonne dataframe
        dfTrip.columns = ['year-month', 'average']

        # aggiunge la colonna borough per conformità con il resto del DataSet
        dfTrip.insert(1,'borough',['New York'])

        return dfTrip