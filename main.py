import streamlit as st
import pandas as pd
import numpy as np


def load_data(csv_file):
    data = pd.read_csv(csv_file)
    return data


def main():
    st.title("Uber pickups in NYC")
    data_load_state = st.text("Loading data...")
    csv_file = "data/2024.csv"
    data = load_data(csv_file=csv_file)
    data_load_state.text("Loading data...done!")
    # data_load_state.text("Done! (using st.cache_data)")


if __name__ == "__main__":
    main()
