import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AI8_API_KEY"],
    base_url=os.environ.get("AI8_BASE_URL", "https://ai8.my/v1"),
)

model = os.environ.get("AI8_MODEL", "gpt-5.5")

stream = client.chat.completions.create(
    model=model,
    messages=[{"role": "user", "content": "Write a short haiku about APIs."}],
    stream=True,
)

for chunk in stream:
    delta = chunk.choices[0].delta.content
    if delta:
        print(delta, end="", flush=True)
print()
