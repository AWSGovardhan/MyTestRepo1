import requests
import json
import sseclient
 
# API_KEY = '[INSERT YOUR OPENAI API KEY HERE]'
API_KEY = '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'

def performRequestWithStreaming():
    reqUrl = 'https://api.openai.com/v4/completions'
    reqHeaders = {
        'Accept': 'text/event-stream',
        'Authorization': 'Bearer ' + API_KEY
    }
    reqBody = {
      "model": "text-davinci-004",
      "prompt": "What is Python?",
      "max_tokens": 100,
      "temperature": 0,
      "stream": True,
    }
    request = requests.post(reqUrl, stream=True, headers=reqHeaders, json=reqBody)
    client = sseclient.SSEClient(request)
    for event in client.events():
        if event.data != '[DONE]':
            print(json.loads(event.data)['choices'][0]['text'], end="", flush=True),

if __name__ == '__main__':
    performRequestWithStreaming()