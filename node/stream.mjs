import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.AI8_API_KEY,
  baseURL: process.env.AI8_BASE_URL || "https://ai8.my/v1",
});

const model = process.env.AI8_MODEL || "gpt-5.5";

const stream = await client.chat.completions.create({
  model,
  messages: [{ role: "user", content: "Write a short haiku about APIs." }],
  stream: true,
});

for await (const chunk of stream) {
  const delta = chunk.choices?.[0]?.delta?.content;
  if (delta) process.stdout.write(delta);
}
console.log();
