from src.preprocess import preprocess_pipeline
from src.model import anomaly_pipeline
from src.explain import add_explanations

df, X, scaler = preprocess_pipeline("data/5g_network_data.csv")

df, model = anomaly_pipeline(X, df)

df = add_explanations(df)

print(df[df["Anomaly"] == -1][["Latency (ms)", "Signal Strength (dBm)", "Explanation"]].head())