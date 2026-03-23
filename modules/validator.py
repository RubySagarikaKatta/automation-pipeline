def validate_data(df):
    if 'value' not in df.columns:
        raise ValueError("Missing 'value' column")
    
    if df.empty:
        raise ValueError("Data is empty after cleaning")
    
    return df