import os
import openai
openai.api_key = os.getenv(OPENAI_API_KEY)
openai.Embedding.create(
  model=text-embedding-ada-002,
  input=The food was delicious and the waiter...
)
