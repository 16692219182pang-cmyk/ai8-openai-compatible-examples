import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AI8_API_KEY"],
    base_url=os.environ.get("AI8_BASE_URL", "https://ai8.my/v1"),
)

model = os.environ.get("AI8_MODEL", "gpt-5.5")

response = client.chat.completions.create(
    model=model,
    messages=[
        {"role": "system", "content": "You are a concise assistant."},
        {"role": "user", "content": "Say hello in one sentence."},
    ],
)

print(response.choices[0].message.content)
