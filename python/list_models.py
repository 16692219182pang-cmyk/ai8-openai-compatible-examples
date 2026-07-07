import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AI8_API_KEY"],
    base_url=os.environ.get("AI8_BASE_URL", "https://ai8.my/v1"),
)

models = client.models.list()
for model in models.data:
    print(model.id)
