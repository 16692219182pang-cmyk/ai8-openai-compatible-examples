import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.AI8_API_KEY,
  baseURL: process.env.AI8_BASE_URL || "https://ai8.my/v1",
});

const model = process.env.AI8_MODEL || "gpt-5.5";

const response = await client.chat.completions.create({
  model,
  messages: [
    { role: "system", content: "You are a concise assistant." },
    { role: "user", content: "Say hello in one sentence." },
  ],
});

console.log(response.choices[0].message.content);
