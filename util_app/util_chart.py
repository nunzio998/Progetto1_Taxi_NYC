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
            alt.Chart(data, title="NY taxi")
            .mark_line()
            .encode(
                x="year-month",
                y="average",
                color="borough",
            )
        )

        # Draw points on the line, and highlight based on selection
        points = lines.transform_filter(hover).mark_circle(size=65)

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
                    alt.Tooltip("average", title="Average"),
                ],
            )
            .add_selection(hover)
        )
        return (lines + points + tooltips).interactive()

    chart = get_chart(source)

    st.altair_chart(
        chart.interactive(),
        use_container_width=True
    )
