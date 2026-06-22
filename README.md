# Agnes AI

Official gateway and model catalog for Agnes AI.

Agnes AI gives developers OpenAI-compatible access to multimodal models for text, image, video, and agent workflows through a unified API gateway.

## Documentation Status

| Field | Value |
| --- | --- |
| Public documentation version | `2026.06.22` |
| Last updated | `2026-06-22 00:00 Asia/Shanghai` |
| Source of truth | Official website and API platform |
| Change notice | Model availability, rate limits, pricing, and quota rules may change over time. Always confirm production-critical values in the official docs or platform console. |

## Quick Links

| Resource | URL |
| --- | --- |
| Website | https://agnes-ai.com/ |
| Developer Docs | https://agnes-ai.com/doc/overview |
| API Platform | https://platform.agnes-ai.com/ |
| API Base URL | `https://apihub.agnes-ai.com/v1` |

## Models

| Model | Type | Endpoint | Highlights |
| --- | --- | --- | --- |
| `agnes-1.5-flash` | Text and vision-language | `/v1/chat/completions` | Low-latency chat, text generation, image URL input, high-throughput production use |
| `agnes-2.0-flash` | Text and vision-language | `/v1/chat/completions` | Reasoning, coding, tool calling, streaming, image understanding, agent workflows |
| `agnes-image-2.0-flash` | Image generation and editing | `/v1/images/generations` | Text-to-image, image-to-image, URL or Base64 output |
| `agnes-image-2.1-flash` | Image generation and editing | `/v1/images/generations` | High-density visual generation, image editing, flexible sizes, URL or Base64 output |
| `agnes-video-v2.0` | Video generation | `/v1/videos` | Text-to-video, image-to-video, multi-image video, keyframe animation, async task API |

## Current Access and Limits

The values below are current public reference values as of `2026-06-22`. They are operational limits, not permanent guarantees.

### User Plans

| User plan | Text model RPM | Image model quota | Video model quota |
| --- | ---: | --- | --- |
| Free / default | 20 actual RPM | Resolution-specific RPM limits apply | 20 actual RPM |
| Enterprise | 40 actual RPM | Higher resolution-specific RPM limits apply | 40 actual RPM |
| Token Plan | 1,000 actual RPM for text models | Higher 1K and 2K image RPM limits apply | 100 actual RPM |

### Subscription Quotas

| Plan | `agnes-2.0-flash` | `agnes-image-2.0/2.1-flash` | `agnes-video-v2.0` |
| --- | --- | --- | --- |
| Starter `$4` | 1,500 requests per 5 hours; 15,000 requests per week | 4,000 images per day | 500 seconds per day |
| Plus `$10` | 7,500 requests per 5 hours; 75,000 requests per week | 4,000 images per day | 500 seconds per day |
| Pro `$50` | 30,000 requests per 5 hours; 300,000 requests per week | 4,000 images per day | 500 seconds per day |

For detailed per-model RPM tables, see [`MODEL_CATALOG.md`](./MODEL_CATALOG.md).

## Chat Example

```bash
curl https://apihub.agnes-ai.com/v1/chat/completions \
  -H "Authorization: Bearer $AGNES_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "agnes-2.0-flash",
    "messages": [
      {
        "role": "user",
        "content": "Explain how to integrate an OpenAI-compatible API gateway."
      }
    ],
    "stream": true
  }'
```

## Image Example

```bash
curl https://apihub.agnes-ai.com/v1/images/generations \
  -H "Authorization: Bearer $AGNES_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "agnes-image-2.1-flash",
    "prompt": "A luminous floating city above a misty canyon at sunrise, cinematic realism",
    "size": "1024x768"
  }'
```

## Video Example

```bash
curl -X POST https://apihub.agnes-ai.com/v1/videos \
  -H "Authorization: Bearer $AGNES_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "agnes-video-v2.0",
    "prompt": "A cinematic shot of a cat walking on the beach at sunset, soft ocean waves, warm golden lighting, realistic motion",
    "height": 768,
    "width": 1152,
    "num_frames": 121,
    "frame_rate": 24
  }'
```

Video generation is asynchronous. Create a task first, then query the result with the returned `video_id`.

```text
GET https://apihub.agnes-ai.com/agnesapi?video_id=<VIDEO_ID>
```

Use `video_id` for video result polling. Do not use `task_id` for current video result queries unless a specific legacy workflow explicitly requires it.

## Common Integration Notes

- Use `Authorization: Bearer YOUR_API_KEY` for every request.
- Keep API keys in server-side environment variables. Never expose keys in client-side code or public repositories.
- `agnes-2.0-flash` currently supports a `256K` context window and `64K` max output reference limit after the June 2026 rollback from the temporary `1M` context window.
- Thinking mode, streaming, tool calling, and vision inputs are supported on compatible chat workflows. Check the model-specific docs before enabling advanced parameters in production.
- For `400` responses, verify required parameters, request body shape, image URL accessibility, and response format placement.
- For `401` responses, verify the API key, bearer token format, account status, and environment variable loading.
- For `429` responses, reduce concurrency, add retry with backoff, and check the current plan-level RPM limit.
- For `500`, `502`, `503`, or `520` responses, retry with exponential backoff and inspect whether the request payload can be simplified.

## Security

Never commit API keys, tokens, `.env` files, screenshots containing secrets, or private customer data.

Use environment variables for local development:

```bash
export AGNES_API_KEY="your_api_key_here"
```

## Documentation

See the official docs for model-specific parameters, response formats, pricing, limits, and troubleshooting:

- https://agnes-ai.com/doc/overview
- https://agnes-ai.com/doc/agnes-15-flash
- https://agnes-ai.com/doc/agnes-20-flash
- https://agnes-ai.com/doc/agnes-image-20-flash
- https://agnes-ai.com/doc/agnes-image-21-flash
- https://agnes-ai.com/doc/agnes-video-v20
