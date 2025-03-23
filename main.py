import streamlit as st
import pandas as pd
import numpy as np

@st.cache_data
def load_data(csv_file):
    data = pd.read_csv(csv_file)
    return data


def main():
    st.title("Uber pickups in NYC")
    data_load_state = st.text("Loading data...")
    csv_file = "data/2023.csv"
    data = load_data(csv_file=csv_file)
    data_load_state.text("Loading data...done!")
    # data_load_state.text("Done! (using st.cache_data)")
    st.subheader('Raw data')
    st.write(data)

    hist_values = np.histogram(
    data["1학년 학생수"].dt.hour, bins=24, range=(0,24))[0]

if __name__ == "__main__":
    main()
