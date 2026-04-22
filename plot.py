import pandas as pd 
import matplotlib.pyplot as plt

df = pd.read_csv("outputs/results.csv")
plt.figure()

normal = df[df["Anomaly"] == 1]
anomaly = df[df["Anomaly"] == -1]

plt.scatter(normal.index, normal["Latency (ms)"], label="Normal")
plt.scatter(anomaly.index, anomaly["Latency (ms)"], label="Anomaly")

plt.legend()
plt.title("Latency with Anomalies")

plt.savefig("latency_plot.png")
plt.show()