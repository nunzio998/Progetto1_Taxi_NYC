import pandas as pd


def max_month_average(source: pd.DataFrame) -> str:
    """
    funzione che prende in input il dataframe ottenuto dall'analisi e restiuisce
    il mese in cui c'è stato il maggiore numero di corse, ovvero quello in cui la average
    è più alta.
    :param source:
    :return:
    """
    dict_tmp = {}

    for i in range(len(source)):
        if source.iloc[i][1] not in dict_tmp.keys():
            dict_tmp[source.iloc[i][1]] = source.iloc[i][3]
        else:
            dict_tmp[source.iloc[i][1]] += source.iloc[i][3]

    max_average = max(dict_tmp.items())
    return max_average[0]
