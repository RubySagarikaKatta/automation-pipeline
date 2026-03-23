import streamlit as st
import pandas as pd

from modules.cleaner import clean_data
from modules.validator import validate_data
from modules.processor import calculate_rolling_avg
from modules.health import apply_health

st.title("📊 Financial Data Health Monitoring System")

uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    
    df.columns = df.columns.str.strip()
    
    st.subheader("Raw Data")
    st.write(df)
    
    # Run pipeline
    data = validate_data(df)
    processed = calculate_rolling_avg(data)
    final = apply_health(processed)
    
    st.subheader("Processed Data")
    st.write(final)

st.download_button(
    label="Download Output CSV",
    data=final.to_csv(index=False),
    file_name="output.csv",
    mime="text/csv"
)