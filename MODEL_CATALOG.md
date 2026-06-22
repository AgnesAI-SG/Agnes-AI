# Agnes AI Model Catalog

This catalog summarizes the public Agnes AI model families and the recommended API entry points.

## Catalog Status

| Field | Value |
| --- | --- |
| Catalog version | `2026.06.22` |
| Last updated | `2026-06-22 00:00 Asia/Shanghai` |
| Scope | Public model, endpoint, quota, and troubleshooting reference |
| Change notice | Rate limits, subscription quotas, model parameters, and availability may change. Treat the values in this catalog as current reference values, not permanent contractual limits. |

## API Base URLs

| Use Case | Base URL |
| --- | --- |
| OpenAI-compatible APIs | `https://apihub.agnes-ai.com/v1` |
| Image API root | `https://apihub.agnes-ai.com` |

Authentication:

```text
Authorization: Bearer YOUR_API_KEY
```

## Text and Agent Models

| Model | Endpoint | Capabilities | Suggested Use Cases |
| --- | --- | --- | --- |
| `agnes-1.5-flash` | `POST /v1/chat/completions` | Fast chat completions, text generation, image URL input, low-latency inference | Realtime assistants, content generation, summarization, simple multimodal tasks |
| `agnes-2.0-flash` | `POST /v1/chat/completions` | Chat, streaming, tool calling, coding, reasoning, image understanding, agent workflows | Developer agents, customer support, coding tasks, workflow automation, multimodal assistants |

### Text Model Notes

| Model | Current Reference Specs | Notes |
| --- | --- | --- |
| `agnes-1.5-flash` | `256K` context, `64K` max output reference limit | Recommended for high-throughput chat and low-latency content workflows. |
| `agnes-2.0-flash` | `256K` context, `64K` max output reference limit | The temporary `1M` context window was rolled back in June 2026 for stability. Use this model for coding, reasoning, agents, vision input, streaming, and tool calling. |

## Image Models

| Model | Endpoint | Capabilities | Suggested Use Cases |
| --- | --- | --- | --- |
| `agnes-image-2.0-flash` | `POST /v1/images/generations` | Text-to-image, image-to-image, URL output, Base64 output | Creative images, product visuals, posters, image transformation |
| `agnes-image-2.1-flash` | `POST /v1/images/generations` | High-density image generation, image editing, URL or Data URI input, flexible image sizes | Detailed compositions, marketing assets, character visuals, social media content |

## Video Models

| Model | Endpoint | Capabilities | Suggested Use Cases |
| --- | --- | --- | --- |
| `agnes-video-v2.0` | `POST /v1/videos` | Text-to-video, image-to-video, multi-image video, keyframe animation, async generation | Storytelling, marketing videos, product demos, social video, app motion assets |

Video result query:

```text
GET https://apihub.agnes-ai.com/agnesapi?video_id=<VIDEO_ID>
```

Current guidance:

- Use the returned `video_id` to poll video results.
- Do not use `task_id` for current result polling unless a legacy integration specifically documents that workflow.
- If a video task stays queued for more than a few minutes, verify that the polling request is using `video_id`.

Legacy task query format:

```text
GET https://apihub.agnes-ai.com/v1/videos/{task_id}
```

## Current Rate Limits

These values are current public reference values as of `2026-06-22`. Use the official platform console as the final source of truth for production traffic planning.

### Text Model RPM

| Model Type | User Type | Public Request RPM | Actual Executable RPM |
| --- | --- | ---: | ---: |
| Text models | Free / default | 30 | 20 |
| Text models | Enterprise | 60 | 40 |
| Text models | Token Plan | 1,000 | 1,000 |

### Image Model RPM

| Model Type | User Type | Resolution | Public Request RPM | Actual Executable RPM |
| --- | --- | --- | ---: | ---: |
| Image models | Free / default | 1K | 30 | 20 |
| Image models | Free / default | 2K | 20 | 10 |
| Image models | Free / default | 3K | 2 | 1 |
| Image models | Free / default | 4K | 1 | 1 |
| Image models | Enterprise | 1K | 60 | 40 |
| Image models | Enterprise | 2K | 40 | 20 |
| Image models | Enterprise | 3K | 2 | 1 |
| Image models | Enterprise | 4K | 2 | 1 |
| Image models | Token Plan | 1K | 120 | 100 |
| Image models | Token Plan | 2K | 120 | 80 |
| Image models | Token Plan | 3K | 2 | 1 |
| Image models | Token Plan | 4K | 2 | 1 |

### Video Model RPM

| Model Type | User Type | Public Request RPM | Actual Executable RPM |
| --- | --- | ---: | ---: |
| Video models | Free / default | 30 | 20 |
| Video models | Enterprise | 60 | 40 |
| Video models | Token Plan | 100 | 100 |

### RPM Field Definitions

| Field | Meaning |
| --- | --- |
| Public Request RPM | Number of requests a user is allowed to initiate per minute. |
| Actual Executable RPM | Number of requests that can actually be executed per minute after service-side scheduling and capacity constraints. |

## Current Subscription Quotas

These quota values are current public reference values as of `2026-06-22` and may be adjusted in later pricing or capacity updates.

| Plan | Price | `agnes-2.0-flash` | `agnes-image-2.0/2.1-flash` | `agnes-video-v2.0` |
| --- | ---: | --- | --- | --- |
| Starter | `$4` | 1,500 requests per 5 hours; 15,000 requests per week | 4,000 images per day | 500 seconds per day |
| Plus | `$10` | 7,500 requests per 5 hours; 75,000 requests per week | 4,000 images per day | 500 seconds per day |
| Pro | `$50` | 30,000 requests per 5 hours; 300,000 requests per week | 4,000 images per day | 500 seconds per day |

## Compatibility Notes

Agnes AI is designed for OpenAI-compatible integrations. For agent clients and coding tools, configure:

```text
Base URL: https://apihub.agnes-ai.com/v1
API Key: YOUR_API_KEY
Chat endpoint: /v1/chat/completions
```

Recommended model selection:

| Workflow | Recommended Model |
| --- | --- |
| General chat and content generation | `agnes-1.5-flash` |
| Coding, reasoning, tool calling, and agent workflows | `agnes-2.0-flash` |
| Text-to-image and image editing | `agnes-image-2.1-flash` |
| Fast image generation | `agnes-image-2.0-flash` |
| Text-to-video and image-to-video | `agnes-video-v2.0` |

## Troubleshooting Reference

| Status | Meaning | What to Check |
| --- | --- | --- |
| `400` | Invalid request | Required fields, parameter types, image URL accessibility, response format placement, model-specific parameter support. |
| `401` | Authentication failed | API key value, `Authorization: Bearer ...` format, environment variable loading, account status. |
| `404` | Endpoint or resource not found | Base URL, endpoint path, model name, and whether a generated resource ID exists. |
| `429` | Rate limit exceeded | Current user plan, RPM limits, concurrent requests, retry and backoff behavior. |
| `500` | Server error | Retry with backoff, reduce payload complexity, verify whether the issue reproduces with a minimal request. |
| `502` | Upstream gateway error | Retry with backoff and check service status if available. |
| `503` | Service busy or unavailable | Retry later, reduce concurrency, and avoid immediate repeated polling. |
| `520` | Unknown upstream error | Retry with backoff and capture request metadata for support investigation. |

## Documentation Links

| Model | Docs |
| --- | --- |
| `agnes-1.5-flash` | https://agnes-ai.com/doc/agnes-15-flash |
| `agnes-2.0-flash` | https://agnes-ai.com/doc/agnes-20-flash |
| `agnes-image-2.0-flash` | https://agnes-ai.com/doc/agnes-image-20-flash |
| `agnes-image-2.1-flash` | https://agnes-ai.com/doc/agnes-image-21-flash |
| `agnes-video-v2.0` | https://agnes-ai.com/doc/agnes-video-v20 |
