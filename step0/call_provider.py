import json, urllib.request

MODEL = "qwen3.5:9b"
URL = "http://localhost:11434/api/generate"

def generate(prompt):
    body = {"model": MODEL, "prompt": prompt, "raw": False, "stream": False}
    req = urllib.request.Request(URL,
                                 data=json.dumps(body).encode(),
                                 headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req) as r:
        return json.loads(r.read())["response"]

print(generate("What is the capital of France?"))
