import json, urllib.request

MODEL = "qwen3.5:9b"

def chat(messages):
    body = {"model": MODEL, "messages": messages, "stream": False}
    req = urllib.request.Request("http://localhost:11434/api/chat",
                                 data=json.dumps(body).encode(),
                                 headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req) as r:
        return json.loads(r.read())["message"]

while True:
    user = input("\nyou> ")
    if user in ["exit", "quit"]:
        break
    reply = chat([{"role": "user", "content": user}]) # notice that only one message is passed at a time, so it's amnesic
    print("bot>", reply["content"])
