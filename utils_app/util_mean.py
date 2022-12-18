import pandas as pd
import streamlit as st


def meanPeriodBoroughSelected(dataFrame: pd.DataFrame):
    """
    :param dataFrame:
    :return:
    """
    st.write(dataFrame)
    st.write(2)
    Average = 2
    return st.write(f"Media sul periodo e borough selezionato: {Average}")
