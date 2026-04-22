import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="5G AI Monitor", layout="wide")

st.title("📡 AI-Based 5G Network Monitoring System")

# Check if results exist
if not os.path.exists("outputs/results.csv"):
    st.warning("Results not found. Please run main.py first.")
    st.stop()

# Load data
df = pd.read_csv("outputs/results.csv")
df_small = df.sample(2000 ,random_state=42)
# Sidebar
st.sidebar.header("Filters")
show_anomalies = st.sidebar.checkbox("Show only anomalies")

if show_anomalies:
    df_small = df[df["Anomaly"] == -1]
# Metrics
col1, col2 = st.columns(2)
col1.metric("Total Records", len(df))
col2.metric("Anomalies", (df["Anomaly"] == -1).sum())

# Chart
st.subheader("Latency Trend")
st.line_chart(df_small["Latency (ms)"])

# Table
st.subheader("Detected Anomalies")
st.dataframe(df[df["Anomaly"] == -1][[
    "Latency (ms)",
    "Signal Strength (dBm)",
    "Explanation",
    "LLM Explanation"
]].head(20))
