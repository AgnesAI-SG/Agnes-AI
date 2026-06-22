# Agnes AI Model Catalog

This catalog summarizes the public Agnes AI model families and the recommended API entry points.

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

Legacy task query:

```text
GET https://apihub.agnes-ai.com/v1/videos/{task_id}
```

## Documentation Links

| Model | Docs |
| --- | --- |
| `agnes-1.5-flash` | https://agnes-ai.com/doc/agnes-15-flash |
| `agnes-2.0-flash` | https://agnes-ai.com/doc/agnes-20-flash |
| `agnes-image-2.0-flash` | https://agnes-ai.com/doc/agnes-image-20-flash |
| `agnes-image-2.1-flash` | https://agnes-ai.com/doc/agnes-image-21-flash |
| `agnes-video-v2.0` | https://agnes-ai.com/doc/agnes-video-v20 |

