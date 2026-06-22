# Agnes AI

Official gateway and model catalog for Agnes AI.

Agnes AI gives developers OpenAI-compatible access to multimodal models for text, image, video, and agent workflows through a unified API gateway.

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

