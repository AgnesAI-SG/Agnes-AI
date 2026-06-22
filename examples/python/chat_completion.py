import os

from openai import OpenAI


client = OpenAI(
    api_key=os.environ["AGNES_API_KEY"],
    base_url="https://apihub.agnes-ai.com/v1",
)

response = client.chat.completions.create(
    model="agnes-2.0-flash",
    messages=[
        {
            "role": "user",
            "content": "Write a short checklist for testing an API integration.",
        }
    ],
)

print(response.choices[0].message.content)

