import pandas as pd

def get_opportunities():
    df = pd.read_csv("data/opportunities.csv")
    df.dropna(subset=["titre", "city", "summary"], inplace=True)
    return df
