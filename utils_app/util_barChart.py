import altair as alt
import pandas as pd
import streamlit as st


def bar_chart(dataFrame: pd.DataFrame, monthDict: dict):
    """
    Riceve il Dataframe dei dati e grafica un bar dinamico in base ai parametri selezionati
    :param monthDict: dizionario per la conversione della lista di mesi (Jan, Feb, Mar...) in (01, 02, 03,...)
    :param dataFrame: input dataframe
    :return:
    """
    dfFiltered = dataFrame
    numMonths = []
    for date in dfFiltered['year-month']:
        numMonths.append(date.month)
    ZoneDict = dict(zip(dfFiltered['year-month'], numMonths))
    dfFiltered['year-month'] = dfFiltered['year-month'].replace(ZoneDict)
    reversedMonthDict = dict(map(lambda key: (monthDict[key], key), monthDict.keys()))
    dfFiltered['year-month'] = dfFiltered['year-month'].replace(reversedMonthDict)
    dfFiltered = dfFiltered.groupby(['year-month', 'borough']).mean().reset_index()
    dfFiltered['average'] = round(dfFiltered['average']).astype(int)

    dfDatetime = dfFiltered['year-month'].drop_duplicates(keep='first').reset_index(drop=True)

    dfBorough = pd.DataFrame(dfFiltered, columns=['borough', 'average'])
    categories = list(dfBorough['borough'].drop_duplicates(keep='first'))
    c = dfBorough.groupby('borough').cumcount()
    dfBorough = pd.crosstab(c, dfBorough.borough, dfBorough.average, aggfunc='first').reindex(categories, axis=1)

    dfFiltered = pd.concat([dfDatetime, dfBorough], axis=1)

    barPlot = (
        alt.Chart(dfFiltered)
        .transform_fold(categories, as_=["key", "value"])
        .mark_bar()
        .encode(
            alt.X('key:N', axis=None),
            alt.Y("value:Q"),
            alt.Color("key:N", legend=alt.Legend(title=None, orient='bottom')),
            alt.Column("year-month",
                       sort=list(monthDict.keys()),
                       header=alt.Header(labelOrient="bottom", title=None)
                       )
        )
    )
    st.altair_chart(
        barPlot.interactive()
    )

    return None
