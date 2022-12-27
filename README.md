## Bozza dei punti:
- vengono considerate le corse che PARTONO da un determinato borough
- per la verifica consideriamo soltanto le PULocationID e DOocationID, devono appartenere al file dei borough
- c'è possibilità di visualizzare il borough unknown, nel senso che vengono considerate le corse che partono da borough unknown
- output (file,grafico): nel file in formato csv viene salvato un dataframe così composto: mese,borough,media-giornaliera
- se non si specifica l'anno si utilizza l'anno corrente, se non si specifica il mese si prende il mese corrente, se non si specificano i borough si considera tutto New York considerando anche le corse con unknown
- se viene specificato più di un mese per un anno, nel grafico viene evidenziato il mese con media giornaliera più alta
. per l'input dell'anno: gli output (file e grafico) riguardano un singolo anno; se in input ci sono più anni, vengono restituiti tanti output (file, grafico) quanti sono gli anni

```
  data
    trip
      ...
      2021
        yellow_tripdata_2021-01.parquet
        yellow_tripdata_2021-02.parquet
        ...
      2022
        yellow_tripdata_2022-01.parquet
        ...
    zone
      taxi+_zone_lookup.csv
  Analisi
    __init__.py
    DataAnalyses.py
  File
    __init__.py
    TaxiTripFile.py
    TaxiZoneFile.py
  FileMaker
    __init__.py
    AverageFileMaker.py
  output
    average.csv
  utils_app
    __init__.py
    util_analyses.py
    util_barChart.py
    util_chart.py
    util_dataset.py
    util_filter.py
    util_mean.py
  .gitignore
  README.md
  app.py
  delete.py
  requirements.txt
```

