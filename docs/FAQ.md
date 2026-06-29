# Agnes AI FAQ

Last updated: `2026-06-28 00:00 Asia/Singapore`

## What is the API base URL?

Use:

```text
https://apihub.agnes-ai.com/v1
```

## Is the API OpenAI-compatible?

Agnes AI is designed for OpenAI-compatible integrations. Chat workflows use:

```text
POST /v1/chat/completions
```

## Which model should I use?

| Workflow | Recommended Model |
| --- | --- |
| Coding, reasoning, tool calling, and agent workflows | `agnes-2.0-flash` |
| Text-to-image and image editing | `agnes-image-2.1-flash` |
| Fast image generation | `agnes-image-2.0-flash` |
| Text-to-video and image-to-video | `agnes-video-v2.0` |

## What are the current limits?

See [`MODEL_CATALOG.md`](../MODEL_CATALOG.md) for the current reference RPM and subscription quota tables. See [`TOKEN_PLAN_FAQ.md`](./TOKEN_PLAN_FAQ.md) for access types, Token Plan quotas, and API key limit-pool behavior.

Limits may change over time. Always confirm production-critical values in the official Agnes AI platform console.

## What changed in the 2026-06-28 limit update?

The public reference video RPM values were updated:

| User type | Public request RPM | Actual executable RPM |
| --- | ---: | ---: |
| Free / default | 2 | 1 |
| Enterprise | 2 | 2 |
| Token Plan | 6 | 5 |

Token Plan video subscription quota remains `500 seconds per day`.

## What is the current `agnes-2.0-flash` context window?

The current public reference value is `512K` context and `64K` max output. 

## How do I query video results?

Use the returned `video_id`:

```text
GET https://apihub.agnes-ai.com/agnesapi?video_id=<VIDEO_ID>
```

Do not use `task_id` for current video result polling unless a legacy integration specifically documents that workflow.

## What should I include in an issue?

Include the model, endpoint, SDK or client, sanitized request body, error code, expected behavior, actual behavior, and whether the issue is reproducible.

Do not include API keys, bearer tokens, private logs, or customer data.
