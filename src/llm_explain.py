from tqdm import tqdm
import requests

def generate_prompt(row):
    return f"""
You are a telecom network expert.

Analyze the following 5G network metrics:

Signal Strength: {row['Signal Strength (dBm)']} dBm
Latency: {row['Latency (ms)']} ms
Jitter: {row['Jitter (ms)']} ms
Congestion Level: {row['Network Congestion Level']}
Dropped Connection: {row['Dropped Connection']}

Explain:
1. Root cause of issue
2. Severity
3. Suggested fix
"""


def get_llm_response(prompt):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3:8b",
            "prompt": prompt,
            "stream": False
        }
    )

    data = response.json()

    # DEBUG (optional but useful)
    # print("DEBUG:", data)

    # Safe handling
    if "response" in data:
        return data["response"]
    elif "message" in data:
        return data["message"]
    elif "error" in data:
        return f"Error: {data['error']}"
    else:
        return "No valid response from LLM"

def add_llm_explanations(df):
    explanations = []

    anomaly_df = df[df["Anomaly"] == -1].head(20)


    for _, row in tqdm(anomaly_df.iterrows(), total=len(anomaly_df), desc="LLM Processing"):
        prompt = generate_prompt(row)
        explanation = get_llm_response(prompt)
        explanations.append(explanation)

    # Fill rest with blank
    df["LLM Explanation"] = ""

    df.loc[anomaly_df.index, "LLM Explanation"] = explanations

    return df