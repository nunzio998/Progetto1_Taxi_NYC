# Progetto1 Taxi NYC
#### Per la realizzazione di questo progetto sono prese le seguenti scelte: 
- Nel conteggio della media vengono considerate le corse che PARTONO da un determinato borough.
- Una prima verifica considera soltanto se le PULocationID appartengono al file taxi+_zone_lookup.csv.
- C'è possibilità di visualizzare il borough Unknown, nel senso che vengono considerate le corse che partono da borough Unknown.

### Input
- Se non si specifica l'anno si visualizzano gli ultimi 2 anni a partire dall'anno corrente, se non si specifica il mese si visualizzaon i primi 4 mesi dell'anno, se non si specificano i borough si considera tutta New York.
- Se viene specificato più di un mese per un anno, nel line-chart vengono evidenziati i mese con media giornaliera più bassa e più alta attraverso i seguenti simboli: 🔴 , 🟢.

### Output
- Nel file in formato csv viene salvato un dataframe così composto: ||year-month||borough||average||

### Structure
```
.
├── data
│   ├── trip
│   │   ├── ...
│   │   ├── 2021
│   │   │   ├── yellow_tripdata_2021-01.parquet
│   │   │   ├── yellow_tripdata_2021-02.parquet
│   │   │   └── ...
│   │   └── 2022
│   │       ├── yellow_tripdata_2022-01.parquet
│   │       └── ...
│   └── zone
│       └── taxi+_zone_lookup.csv
├── Analisi
│   ├── __init__.py
│   └── DataAnalyses.py
├── File
│   ├── __init__.py
│   ├── TaxiTripFile.py
│   └── TaxiZoneFile.py
├── FileMaker
│   ├── __init__.py
│   └── AverageFileMaker.py
├── output
│   └── average.csv
├── utils_app
│   ├── __init__.py
│   ├── util_analyses.py
│   ├── util_barChart.py
│   ├── util_chart.py
│   ├── util_dataset.py
│   ├── util_filter.py
│   └── util_mean.py
├── .gitignore
├── README.md
├── app.py
├── delete.py
└── requirements.txt
```