import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def load_data(path):
    df = pd.read_csv(path)
    return df


def clean_data(df):
    # Drop unnecessary columns
    drop_cols = ["Timestamp", "Location", "Device Model", "Carrier","Band"]
    df = df.drop(columns=drop_cols, errors='ignore')

    # Convert boolean to int
    df["VoNR Enabled"] = df["VoNR Enabled"].astype(int)
    df["Dropped Connection"] = df["Dropped Connection"].astype(int)

    # Map categorical values
    df["Network Congestion Level"] = df["Network Congestion Level"].map({
        "Low": 0,
        "Medium": 1,
        "High": 2
    })

    df["Network Type"] = df["Network Type"].map({
        "4G": 0,
        "5G NSA": 1,
        "5G SA": 2
    })

    df["Video Streaming Quality"] = df["Video Streaming Quality"]

    return df


def scale_data(df):
    scaler = MinMaxScaler()
    scaled = scaler.fit_transform(df)
    return scaled, scaler


def preprocess_pipeline(path):
    df = load_data(path)
    df = clean_data(df)
    X, scaler = scale_data(df)

    return df, X, scaler