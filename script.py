import requests
import json

url = "http://localhost:11434/api/generate"
payload = {
    "model": "friend-2.0",  # or another model you've pulled
    "prompt": "hello",
    "stream": True,    # or True if you want to stream the response
}

def run_streaming_model():
    response = requests.post(url, json=payload, stream=True)
    for line in response.iter_lines():
        if line:
            data = json.loads(line.decode('utf-8'))
            print(data['response'], end="", flush=True)

run_streaming_model()
    

