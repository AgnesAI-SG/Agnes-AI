# Troubleshooting Agnes AI API Integrations

Last updated: `2026-06-22 00:00 Asia/Singapore`

Use this guide when an Agnes AI API integration fails or behaves differently than expected.

For a bilingual Chinese and English status-code reference, see [`ERROR_CODES.md`](./ERROR_CODES.md).

## Quick Checklist

1. Confirm the base URL is `https://apihub.agnes-ai.com/v1`.
2. Confirm the request uses `Authorization: Bearer YOUR_API_KEY`.
3. Confirm the model name is spelled exactly as documented.
4. Confirm the endpoint matches the model family.
5. Remove private data and reduce the request to a minimal reproducible example.
6. Check the current RPM and quota values in `MODEL_CATALOG.md`.
7. Add retry with exponential backoff for transient server or gateway errors.

## Endpoint Checklist

| Workflow | Endpoint |
| --- | --- |
| Chat, coding, reasoning, tools, streaming, and vision-language input | `POST /v1/chat/completions` |
| Image generation and editing | `POST /v1/images/generations` |
| Video generation | `POST /v1/videos` |
| Video result polling | `GET https://apihub.agnes-ai.com/agnesapi?video_id=<VIDEO_ID>` |

## Common Status Codes

| Status | Meaning | Common Checks |
| --- | --- | --- |
| `400` | Invalid request | Required fields, JSON shape, parameter types, model-specific parameter support, image URL accessibility, response format placement. |
| `401` | Authentication failed | API key value, bearer token format, account status, environment variable loading, accidental whitespace. |
| `404` | Endpoint or resource not found | Base URL, endpoint path, model name, `video_id`, and whether the resource still exists. |
| `429` | Rate limit exceeded | Current plan, RPM limits, concurrency, retry behavior, polling frequency. |
| `500` | Server error | Retry with backoff, reduce request complexity, test a minimal request. |
| `502` | Gateway or upstream error | Retry with backoff and check whether the issue is transient. |
| `503` | Service busy or unavailable | Retry later, reduce concurrency, and avoid tight polling loops. |
| `520` | Unknown upstream error | Retry with backoff and capture request metadata for support investigation. |

## Authentication Problems

For `401` responses:

- Use the exact header format: `Authorization: Bearer YOUR_API_KEY`.
- Confirm the API key is loaded from the expected environment variable.
- Confirm the key was not copied with a trailing space or newline.
- Do not expose API keys in browser-side JavaScript, public repositories, screenshots, or issue reports.

## Rate Limit Problems

For `429` responses:

- Check the current plan-level RPM in `MODEL_CATALOG.md`.
- Reduce concurrent requests.
- Add exponential backoff.
- Avoid polling video tasks too frequently.
- Treat the published limits as current reference values, not permanent guarantees.

## Video Polling Problems

Current video workflows should poll with `video_id`:

```text
GET https://apihub.agnes-ai.com/agnesapi?video_id=<VIDEO_ID>
```

If a video task appears stuck:

- Confirm the create request returned a `video_id`.
- Confirm result polling uses `video_id`, not `task_id`.
- Reduce polling frequency.
- Capture the model, request timestamp, and sanitized response body before opening an issue.

## Opening a Good Issue

Include:

- Model
- Endpoint
- SDK or client
- Minimal request body with secrets removed
- Error code and message
- Expected behavior
- Actual behavior
- Whether the issue is reproducible

Do not include API keys, private account data, or customer content.
