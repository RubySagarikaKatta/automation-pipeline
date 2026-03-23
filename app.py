import streamlit as st
import pandas as pd

from modules.cleaner import clean_data
from modules.validator import validate_data
from modules.processor import calculate_rolling_avg
from modules.anomaly import detect_outliers
from modules.health import apply_health

st.title("📊 Financial Data Health Monitoring System")

uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    df = clean_data(df=df)
    
    # df.columns = df.columns.str.strip()
    
    # st.subheader("Raw Data")
    # st.write(df)
    st.subheader("Cleaned Data")
    st.write(df)
    
    # Run pipeline

    data = validate_data(df)
    processed = calculate_rolling_avg(data)
    processed = detect_outliers(processed)
    final = apply_health(processed)
    
    # st.subheader("Processed Data")
    # st.write(final)

    st.subheader("⚠️ Detected Outliers")

    outliers = final[final['outlier'] == "Yes"]

    if not outliers.empty:
        st.write(outliers)
    else:
        st.write("No outliers detected")

    st.subheader("Processed Data")
    st.write(final[['date', 'value', 'rolling_avg', 'trend_display', 'health']])


    st.subheader("📈 Summary")

    total_rows = len(final)
    outliers_count = len(final[final['outlier'] == "Yes"])
    red_count = len(final[final['health'].str.contains("Red")])

    st.write(f"Total Records: {total_rows}")
    st.write(f"Outliers Detected: {outliers_count}")
    st.write(f"Critical (Red) Cases: {red_count}")


    st.download_button(
        label="📥 Download Processed Data",
        data=final.to_csv(index=False),
        file_name="output.csv",
        mime="text/csv"
    )