from sklearn.ensemble import IsolationForest


def train_model(X):
    model = IsolationForest(
        n_estimators=100,
        contamination=0.05,
        random_state=42
    )
    
    model.fit(X)
    return model


def predict_anomalies(model, X):
    preds = model.predict(X)
    return preds


def add_anomaly_column(df, preds):
    df["Anomaly"] = preds
    return df


def anomaly_pipeline(X, df):
    model = train_model(X)
    preds = predict_anomalies(model, X)
    df = add_anomaly_column(df, preds)

    return df, model