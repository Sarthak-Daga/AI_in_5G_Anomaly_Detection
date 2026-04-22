def explain_anomaly(row):
    reasons = []

    # Signal issues
    if row["Signal Strength (dBm)"] < -90:
        reasons.append("Weak signal strength")

    # Latency issues
    if row["Latency (ms)"] > 100:
        reasons.append("High latency")

    # Jitter issues
    if row["Jitter (ms)"] > 10:
        reasons.append("High jitter")

    # Congestion
    if row["Network Congestion Level"] == 2:
        reasons.append("High network congestion")

    # Dropped connection
    if row["Dropped Connection"] == 1:
        reasons.append("Connection drop detected")

    # Final explanation
    if len(reasons) == 0:
        return "Unknown anomaly"
    
    return ", ".join(reasons)


def add_explanations(df):
    df["Explanation"] = df.apply(explain_anomaly, axis=1)
    return df