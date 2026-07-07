# Compatibility checklist

Run these checks before using AI8 for anything important.

## Basic API

- [ ] `/v1/models` returns model IDs
- [ ] chat completions work
- [ ] streaming chat completions work
- [ ] errors are readable
- [ ] billing changes match expected usage

## SDKs and tools

- [ ] Python OpenAI SDK
- [ ] Node.js OpenAI SDK
- [ ] LiteLLM
- [ ] Open WebUI
- [ ] Continue
- [ ] Cursor or another custom-base-url tool

## Operational checks

- [ ] p50 latency measured
- [ ] p95 latency measured
- [ ] rate limits understood
- [ ] fallback behavior understood
- [ ] privacy/data retention terms reviewed
