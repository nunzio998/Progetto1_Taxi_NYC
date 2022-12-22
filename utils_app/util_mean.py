from calendar import monthrange

import pandas as pd


def meanPeriodBoroughSelected(dataFrame: pd.DataFrame):
    """
    Riceve il Dataframe dei dati graficati e restituisce il valore medio sul periodo e sui borough selezionati:
    :param dataFrame: input dataframe
    :return:
    """
    dfFiltered = dataFrame[~(dataFrame['borough'] != f'Boroughs Average')].reset_index(drop=True)
    numDays = []
    numTrip = list(dfFiltered['average'])
    for date in dfFiltered['year-month']:
        numDays.append(monthrange(int(date.year), int(date.month))[1])

    # calcolo media pesata
    weightedAverage = sum(numDays[g] * numTrip[g] for g in range(len(numDays))) / sum(numDays)

    return f"Average number of daily trips based on the selected parameters: {round(weightedAverage)}"
