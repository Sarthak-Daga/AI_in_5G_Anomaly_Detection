from src.preprocess import preprocess_pipeline
from src.model import anomaly_pipeline
from src.explain import add_explanations
from src.llm_explain import add_llm_explanations
import joblib


def main():
    print("🚀 Starting AI 5G Network Analysis...")

    # Step 1: Preprocess
    df, X, scaler = preprocess_pipeline("data/5g_network_data.csv")
    print("✅ Data preprocessed")

    # Step 2: Model
    df, model = anomaly_pipeline(X, df)
    print("✅ Anomaly detection completed")

    # Step 3: Explanation
    df = add_explanations(df)
    print("✅ Root cause analysis added")
    df=add_llm_explanations(df)
    # Step 4: Save results
    df.to_csv("outputs/results.csv", index=False)
    print("📁 Results saved to outputs/results.csv")

    # Show sample anomalies
    print("\n🔥 Sample anomalies:")
    print(df[df["Anomaly"] == -1].head())
    joblib.dump(model, "outputs/model.pkl")


if __name__ == "__main__":
    main()