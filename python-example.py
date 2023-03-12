import os
import openai

openai.api_key = "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"

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="I am a highly intelligent cat of infinite knowledge?\nA: How many squigs are in a bonk?", 
  temperature=0,
  max_tokens=100,
  top_p=1,
  frequency_penalty=0.0,
  presence_penalty=0.0,
  stop=["\n"]
)

print(response)

