import pandas as pd

def calculate_rolling_avg(df):
    df['rolling_avg'] = df['value'].rolling(window=4).mean()
    return df

import pandas as pd
import numpy as np

def calculate_rolling_avg(df):
    
    #  1. Rolling average (no NaN for early rows)
    df['rolling_avg'] = df['value'].rolling(window=4, min_periods=1).mean()
    
    #  2. Trend (difference from rolling average)
    # df['trend'] = df['value'] - df['rolling_avg']
    df['trend'] = df['value'] - df['rolling_avg']

    # format with + or -
    df['trend_display'] = df['trend'].apply(lambda x: f"{x:+.2f}")

    return df