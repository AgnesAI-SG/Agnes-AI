"""Text-to-video task creation and polling example for Agnes AI."""

import os
import time
from typing import Any

import requests


API_KEY = os.environ["AGNES_API_KEY"]
API_ROOT = "https://apihub.agnes-ai.com"


def request_json(method: str, url: str, **kwargs: Any) -> dict[str, Any]:
    headers = kwargs.pop("headers", {})
    headers["Authorization"] = f"Bearer {API_KEY}"
    headers["Content-Type"] = "application/json"

    response = requests.request(method, url, headers=headers, timeout=60, **kwargs)
    response.raise_for_status()
    return response.json()


def create_video() -> str:
    payload = {
        "model": "agnes-video-v2.0",
        "prompt": (
            "A cinematic product shot of a glowing AI model catalog interface, "
            "smooth camera movement, realistic lighting"
        ),
        "height": 768,
        "width": 1152,
        "num_frames": 121,
        "frame_rate": 24,
    }

    data = request_json("POST", f"{API_ROOT}/v1/videos", json=payload)
    video_id = data.get("video_id") or data.get("id")
    if not video_id:
        raise RuntimeError(f"Video response did not include video_id: {data}")
    return video_id


def poll_video(video_id: str) -> dict[str, Any]:
    for _ in range(60):
        data = request_json("GET", f"{API_ROOT}/agnesapi", params={"video_id": video_id})
        status = str(data.get("status", "")).lower()
        if status in {"succeeded", "success", "completed", "done"}:
            return data
        if status in {"failed", "error", "cancelled"}:
            raise RuntimeError(f"Video generation failed: {data}")
        time.sleep(5)

    raise TimeoutError(f"Timed out waiting for video_id={video_id}")


def main() -> None:
    video_id = create_video()
    print(f"Created video task: {video_id}")
    result = poll_video(video_id)
    print(result)


if __name__ == "__main__":
    main()
