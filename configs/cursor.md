# Cursor / custom OpenAI-compatible base URL

If your tool supports a custom OpenAI-compatible endpoint, use:

```text
Base URL: https://ai8.my/v1
API Key: your_ai8_api_key
Model: gpt-5.5 or another model listed in your AI8 dashboard
```

Some apps require the base URL without `/v1`, while others require `/v1`. If requests fail, test both forms and check the app logs.
