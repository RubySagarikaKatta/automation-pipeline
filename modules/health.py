def assign_health(row):
    value = row['value']
    avg = row['rolling_avg']
    
    if avg is None or avg != avg:  # handles NaN
        return "Unknown"
    
    diff = abs(value - avg) / avg
    
    if diff <= 0.1:
        return "Green"
    elif diff <= 0.25:
        return "Amber"
    else:
        return "Red"


def apply_health(df):
    df['health'] = df.apply(assign_health, axis=1)
    return df