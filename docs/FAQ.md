# Agnes AI FAQ

Last updated: `2026-06-22 00:00 Asia/Shanghai`

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
| General chat and content generation | `agnes-1.5-flash` |
| Coding, reasoning, tool calling, and agent workflows | `agnes-2.0-flash` |
| Text-to-image and image editing | `agnes-image-2.1-flash` |
| Fast image generation | `agnes-image-2.0-flash` |
| Text-to-video and image-to-video | `agnes-video-v2.0` |

## What are the current limits?

See `MODEL_CATALOG.md` for the current reference RPM and subscription quota tables.

Limits may change over time. Always confirm production-critical values in the official Agnes AI platform console.

## What is the current `agnes-2.0-flash` context window?

The current public reference value is `256K` context and `64K` max output. The temporary `1M` context window was rolled back in June 2026 for stability.

## How do I query video results?

Use the returned `video_id`:

```text
GET https://apihub.agnes-ai.com/agnesapi?video_id=<VIDEO_ID>
```

Do not use `task_id` for current video result polling unless a legacy integration specifically documents that workflow.

## What should I include in an issue?

Include the model, endpoint, SDK or client, sanitized request body, error code, expected behavior, actual behavior, and whether the issue is reproducible.

Do not include API keys, bearer tokens, private logs, or customer data.

