def validate_data(df):
    if 'value' not in df.columns:
        raise ValueError("Missing 'value' column")
    return df