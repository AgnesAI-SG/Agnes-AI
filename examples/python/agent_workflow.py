"""Tool-calling style agent workflow example for Agnes AI."""

import json
import os
from typing import Any

from openai import OpenAI


client = OpenAI(
    api_key=os.environ["AGNES_API_KEY"],
    base_url="https://apihub.agnes-ai.com/v1",
)


def get_model_status(model: str) -> dict[str, str]:
    return {
        "model": model,
        "status": "available",
        "base_url": "https://apihub.agnes-ai.com/v1",
    }


TOOLS: list[dict[str, Any]] = [
    {
        "type": "function",
        "function": {
            "name": "get_model_status",
            "description": "Return public status information for an Agnes AI model.",
            "parameters": {
                "type": "object",
                "properties": {
                    "model": {
                        "type": "string",
                        "description": "Agnes AI model name.",
                    }
                },
                "required": ["model"],
            },
        },
    }
]


def main() -> None:
    messages: list[dict[str, Any]] = [
        {
            "role": "user",
            "content": "Check whether agnes-2.0-flash is available, then summarize how to call it.",
        }
    ]

    first = client.chat.completions.create(
        model="agnes-2.0-flash",
        messages=messages,
        tools=TOOLS,
        tool_choice="auto",
    )

    assistant_message = first.choices[0].message
    messages.append(assistant_message.model_dump(exclude_none=True))

    if assistant_message.tool_calls:
        for tool_call in assistant_message.tool_calls:
            if tool_call.function.name != "get_model_status":
                continue

            args = json.loads(tool_call.function.arguments)
            result = get_model_status(args["model"])
            messages.append(
                {
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": json.dumps(result),
                }
            )

        final = client.chat.completions.create(
            model="agnes-2.0-flash",
            messages=messages,
        )
        print(final.choices[0].message.content)
    else:
        print(assistant_message.content)


if __name__ == "__main__":
    main()
