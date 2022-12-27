from FileMaker.AverageFileMaker import AverageFileMaker


def check_analyses(yearsList: list, monthsList: list, monthsDict: dict):
    """
    Funzione che dati in ingresso una lista di mesi e una lista di anni, per ogni coppia anno-mese esegue l'analisi e
    archivia i dati analizzati.
    :param yearsList: lista di anni sui quali si vuole eseguire l'analisi
    :param monthsList: lista di mesi sui quali si vuole eseguire l'analisi
    :param monthsDict: dizionario per la conversione della lista di mesi (Jan, Feb, Mar...) in (01, 02, 03,...)
    :return:
    """
    months_number = []

    for month in monthsList:
        if month in monthsDict:
            months_number.append(f'{monthsDict[month]:02d}')
    analisi = AverageFileMaker(yearsList, months_number)
    analisi.writeFiles()
