import pandas as pd

def calculate_rolling_avg(df):
    df['rolling_avg'] = df['value'].rolling(window=4).mean()
    return df