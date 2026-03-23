import pandas as pd

def clean_data(file_path=None, df=None):
    
    if file_path:
        df = pd.read_csv(file_path)
    
    # remove spaces
    df.columns = df.columns.str.strip()
    
    # convert to numeric (invalid → NaN)
    df['value'] = pd.to_numeric(df['value'], errors='coerce')
    
    # drop invalid
    # drop missing values
    df = df.dropna()
    # remove negative values
    df = df[df['value'] >= 0]
    
    return df