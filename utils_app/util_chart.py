import time
import streamlit as st
import pandas as pd
import altair as alt


def line_chart(source):
    def get_chart(data):
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

    st.altair_chart(
        chart.interactive(),
        use_container_width=True
    )

