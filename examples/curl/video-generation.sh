#!/usr/bin/env bash
set -euo pipefail

: "${AGNES_API_KEY:?Set AGNES_API_KEY before running this example.}"

curl -X POST https://apihub.agnes-ai.com/v1/videos \
  -H "Authorization: Bearer ${AGNES_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "agnes-video-v2.0",
    "prompt": "A cinematic product shot of an AI dashboard loading on a laptop, smooth camera motion",
    "height": 768,
    "width": 1152,
    "num_frames": 121,
    "frame_rate": 24
  }'

