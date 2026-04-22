from src.llm_explain import get_llm_response

prompt = """
Signal Strength: -95 dBm
Latency: 120 ms
Jitter: 15 ms
Congestion: High
Dropped Connection: True

Explain issue and suggest fix.
"""

response = get_llm_response(prompt)
print(response)