from calendar import monthrange
import pandas as pd
import streamlit as st
import altair as alt


def bar_chart(dataFrame: pd.DataFrame, monthDict: dict):
    """
    Riceve il Dataframe dei dati e grafica un bar chart:
    :param monthDict:
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
    dfFiltered = dfFiltered.groupby(['year-month', 'borough']).mean('average').reset_index()
    dfFiltered['average'] = round(dfFiltered['average']).astype(int)

    barPlot = (
        alt.Chart(dfFiltered)
        .transform_fold(["year-month", "average"], as_=["key", "value"])
        .mark_bar()
        .encode(
            alt.X('borough:N', axis=None),
            alt.Y("average:Q"),
            alt.Color("borough:N", legend=alt.Legend(title=None, orient='bottom')),
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
