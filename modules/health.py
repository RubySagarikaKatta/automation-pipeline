def assign_health(row):
    value = row['value']
    avg = row['rolling_avg']
    trend = row['trend']
    
    if avg is None or avg != avg:  # handle NaN
        return "Unknown"
    
    # percentage difference
    diff_pct = abs(value - avg) / avg
    
    # classification logic
    if diff_pct <= 0.1:
        return "Green"
    
    elif diff_pct <= 0.25:
        # use trend for context
        if trend > 0:
            return "Amber (Upward spike)"
        else:
            return "Amber (Drop)"
    
    else:
        if trend > 0:
            return "Red (High spike)"
        else:
            return "Red (Sharp drop)"


def apply_health(df):
    df['health'] = df.apply(assign_health, axis=1)
    return df