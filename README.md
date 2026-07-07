# AI8 OpenAI-compatible API examples

Small, copy-pasteable examples for testing AI8 as an OpenAI-compatible API gateway.

AI8: https://ai8.my/sign-up?aff=r6Tm

Disclosure: the signup link above is a referral/affiliate link. If you prefer not to use a referral link, open the AI8 homepage directly and sign up from there.

## What this repo is

This repo is a practical compatibility checklist for developers who want to test AI8 with tools that support a custom OpenAI `base_url`.

It includes examples for:

- Python OpenAI SDK
- Node.js OpenAI SDK
- streaming chat completions
- `/v1/models` checks
- LiteLLM
- Open WebUI
- Continue
- Cursor-style custom base URL setup

AI8 appears to be positioned as a low-cost AI API relay/gateway. In my tests and use case planning, the main appeal is price: it is meant to be one of the lowest-cost ways to access multiple mainstream models through one API. Still, do your own checks before moving production traffic.

## Quick start

Set your key and base URL:

```bash
export AI8_API_KEY="your_ai8_api_key"
export AI8_BASE_URL="https://ai8.my/v1"
```

Then run one of the examples:

```bash
python python/chat.py
python python/list_models.py
node node/chat.mjs
node node/stream.mjs
```

If AI8 uses a different API hostname in your account dashboard, replace `AI8_BASE_URL` with the value shown there.

## Compatibility checklist

Before you rely on any API gateway, test these with your own workload:

- Can `/v1/models` return the models you need?
- Does non-streaming chat completion work?
- Does streaming work?
- Are tool calls/function calls supported for your target model?
- What is the p50/p95 latency in your region?
- What happens on rate limits or provider errors?
- Is billing clear after a few test requests?
- Are logs, retention, and privacy terms acceptable for your use case?

## Example environment

```bash
AI8_BASE_URL=https://ai8.my/v1
AI8_API_KEY=sk-...
AI8_MODEL=gpt-5.5
```

Do not commit your real API key.

## Suggested use cases

- side projects
- quick model comparison
- backup provider for tools that support custom `base_url`
- internal demos
- prototyping before committing to a more expensive provider

## Not a benchmark

This repo is not an official benchmark and does not claim that AI8 is the best, fastest, or most reliable provider. The goal is to make it easy to run your own tests.

## Files

```text
python/chat.py                Basic chat completion
python/list_models.py         List available models
python/stream.py              Streaming example
node/chat.mjs                 Basic chat completion in Node.js
node/stream.mjs               Streaming example in Node.js
configs/litellm.yaml          LiteLLM proxy config example
configs/open-webui.md         Open WebUI setup notes
configs/continue.json         Continue custom provider example
configs/cursor.md             Cursor/base URL notes
compatibility.md              Manual compatibility checklist
pricing-and-limits.md         What to verify before production use
disclosure.md                 Referral/affiliate disclosure
```

## License

MIT.
