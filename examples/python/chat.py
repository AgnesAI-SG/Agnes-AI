"""Streaming chat completion example for Agnes AI."""

import os

from openai import OpenAI


client = OpenAI(
    api_key=os.environ["AGNES_API_KEY"],
    base_url="https://apihub.agnes-ai.com/v1",
)

stream = client.chat.completions.create(
    model="agnes-2.0-flash",
    messages=[
        {
            "role": "user",
            "content": "Write a short intro to Agnes AI for developers.",
        }
    ],
    stream=True,
)

for chunk in stream:
    delta = chunk.choices[0].delta.content
    if delta:
        print(delta, end="")

print()
