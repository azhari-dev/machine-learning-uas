# src/preprocessing.py

import pandas as pd

def load_and_clean_data(path):
    df = pd.read_csv(path)
    df.rename(columns={"Date-Hour(NMT)": "datetime"}, inplace=True)
    df["datetime"] = pd.to_datetime(df["datetime"], format="%d.%m.%Y-%H:%M")
    df.set_index("datetime", inplace=True)
    df.fillna(df.median(), inplace=True)
    return df
