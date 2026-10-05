import json, urllib.request

MODEL = "qwen3.5:9b"

def chat(messages):
    body = {"model": MODEL, "messages": messages, "stream": False}
    req = urllib.request.Request("http://localhost:11434/api/chat",
                                 data=json.dumps(body).encode(),
                                 headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req) as r:
        return json.loads(r.read())["message"]

messages = []
while True:
    user = input("\nyou> ")
    if user in ["exit", "quit"]:
        break
    messages.append({"role": "user", "content": user})
    reply = chat(messages)
    messages.append(reply)
    print("bot>", reply["content"])

    status_msg = f"|  Context now holds {len(messages)} messages.  |"
    print("-" * len(status_msg))
    print(status_msg)
    print("-" * len(status_msg))
