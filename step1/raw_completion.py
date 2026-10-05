import json, urllib.request

MODEL = "qwen3.5:9b"

def generate(prompt, raw):
    body = {"model": MODEL, "prompt": prompt, "raw": raw, "stream": False,
            "thinking": False, "options": {"num_predict": 500}}  # cap output length
    req = urllib.request.Request("http://localhost:11434/api/generate",
                                 data=json.dumps(body).encode(),
                                 headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req) as r:
        return json.loads(r.read())["response"]

q = "What is 2 + 2?"
print("--- RAW (no chat template) ---\n", generate(q, raw=True))
print("-"*25)
print("\n--- WITH CHAT TEMPLATE ---\n", generate(q, raw=False))
print("-"*25)
