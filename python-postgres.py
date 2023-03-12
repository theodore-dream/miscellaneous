import os
import requests
import json
import sseclient
import openai
import psycopg2

API_KEY = "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"

# here we setup the Postgres connection
conn = psycopg2.connection(dsn)


def apicall():
    reqUrl = 'https://api.openai.com/v1/completions'
    reqHeaders = {
        'Accept': 'text/event-stream',
        'Authorization': 'Bearer ' + API_KEY
    }
    reqBody = {
      "model": "text-davinci-003",
      "prompt": "Write a poem about social media",
      "max_tokens": 100,
      "temperature": 0,
      "stream": True,
    }
    request = requests.post(reqUrl, stream=True, headers=reqHeaders, json=reqBody)
    client = sseclient.SSEClient(request)
    for event in client.events():
        if event.data != '[DONE]':
        # setup cursor here
            cur = conn.cursor()
            #print(json.loads(event.data)['choices'][0]['text'], end="", flush=True)
            load = print(json.loads(event.data)['choices'][0]['text'], end="", flush=True),
            cur.execute(sql, load)
            print(load)

if __name__ == '__main__':
    performRequestWithStreaming()
