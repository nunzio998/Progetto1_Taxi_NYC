import streamlit as st
import pandas as pd
import altair as alt


def line_chart(source):
    def get_chart(data):
        """
        Funzione che grafica un line-chart interattivo (tooltips) sulla base del dataframe filtrato sui parametri
        selezioanti
        :param data: dataframe filtrato del quale viene effettuato il line-chart
        :return:
        """
        hover = alt.selection_single(
            fields=["year-month"],
            nearest=True,
            on="mouseover",
            empty="none",
        )

        lines = (
            alt.Chart(data, title="NYC Average Taxi Trip")
            .mark_line()
            .encode(
                x="year-month",
                y="average",
                color="borough",
                strokeDash=alt.condition(
                    alt.datum.borough == 'Boroughs Average',
                    alt.value([5, 5]),  # dashed line: 5 pixels  dash + 5 pixels space
                    alt.value([0]),  # solid line
                )
            )
        )

        # Draw points on the line, and highlight based on selection
        points = lines.transform_filter(hover).mark_circle(size=100)

        pointsDot = alt.Chart(data).mark_point(filled=True, opacity=1).encode(
            x="year-month",
            y="average",
            color="borough",
        )

        # Draw a rule at the location of the selection
        tooltips = (
            alt.Chart(data)
            .mark_rule()
            .encode(
                x="year-month",
                y="average",
                opacity=alt.condition(hover, alt.value(0.3), alt.value(0)),
                tooltip=[
                    alt.Tooltip("year-month", title="Date"),
                    alt.Tooltip("borough", title="Borough"),
                    alt.Tooltip("average", title="Average Trip")
                ],
            )
            .add_selection(hover)
        )
        return (lines + points + pointsDot + tooltips).interactive()

    # serve per avere l'asse x del grafico responsive in base all'ampiezza dell'intervallo temporale selezionato
    source['year-month'] = pd.to_datetime(source['year-month'])

    chart = get_chart(source)

    annotation_layer_min, annotation_layer_max = chartMinMax(source)

    st.altair_chart(
        (chart + annotation_layer_min + annotation_layer_max).interactive(),
        use_container_width=True
    )


def chartMinMax(dataFrame: pd.DataFrame):
    """
    Funzione che grafica tanti Red-dot e tanto Green-dot quanti sono i massimi e minimi assoluti del linechart che si
    sta visualizzando
    :param dataFrame:
    :return:
    """
    # Genero un dataframe con 2 rows, una con il minimo e una con il massimo
    # considerando i parametri selzionati
    dfFiltered = dataFrame[~(dataFrame['borough'] != f'Boroughs Average')].reset_index(drop=True)
    dfMax = dfFiltered[~(dfFiltered['average'] != dfFiltered['average'].max())].reset_index(drop=True)
    dfMin = dfFiltered[~(dfFiltered['average'] != dfFiltered['average'].min())].reset_index(drop=True)

    # Input annotations
    ANNOTATIONS_min = []
    for i in range(len(dfMin)):
        ANNOTATIONS_min.append(
            (f"{dfMin['year-month'][i]}", "Minimum based on selected parameters", f"{dfMin['average'][i]}"))

    ANNOTATIONS_max = []
    for i in range(len(dfMax)):
        ANNOTATIONS_max.append(
            (f"{dfMax['year-month'][i]}", "Maximum based on selected parameters", f"{dfMin['average'][i]}"))

    # Create a chart with annotations
    annotations_df_min = pd.DataFrame(ANNOTATIONS_min, columns=["year-month", "info", "value"])
    annotations_df_min["y"] = dfMin['average']

    annotations_df_max = pd.DataFrame(ANNOTATIONS_max, columns=["year-month", "info", "value"])
    annotations_df_max["y"] = dfMax['average']

    annotation_layer_min = (
        alt.Chart(annotations_df_min)
        .mark_text(size=9, text="🔴")
        .encode(
            x="year-month:T",
            y=alt.Y("y:Q"),
            tooltip=["info", "value"],
        )
        .interactive()
    )

    annotation_layer_max = (
        alt.Chart(annotations_df_max)
        .mark_text(size=9, text="🟢")
        .encode(
            x="year-month:T",
            y=alt.Y("y:Q"),
            tooltip=["info", "value"],
        )
        .interactive()
    )

    return annotation_layer_min, annotation_layer_max
