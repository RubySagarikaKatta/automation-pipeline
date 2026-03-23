import pandas as pd

def detect_outliers(df):
    
    # calculate mean and standard deviation
    mean = df['value'].mean()
    std = df['value'].std()
    
    # avoid division by zero
    if std == 0:
        df['z_score'] = 0
        df['outlier'] = "No"
        return df
    
    # calculate z-score
    df['z_score'] = (df['value'] - mean) / std
    
    # classify outliers
    df['outlier'] = df['z_score'].apply(
        lambda x: "Yes" if abs(x) > 2 else "No"
    )
    
    return df

