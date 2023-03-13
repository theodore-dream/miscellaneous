import os
import openai

openai.api_key = "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"

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="You are a highly creative poet. Make a poem",
  temperature=0.7,
  max_tokens=400,
  # top_p=1,
  # frequency_penalty=0.0,
  # presence_penalty=0.0,
  # stop=["\n"]
)

print(response)
print("printed the response above, below is the completion")
print(response.choices[0].text)
