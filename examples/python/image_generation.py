"""Text-to-image generation example for Agnes AI."""

import os

from openai import OpenAI


def main() -> None:
    client = OpenAI(
        api_key=os.environ["AGNES_API_KEY"],
        base_url="https://apihub.agnes-ai.com/v1",
    )

    response = client.images.generate(
        model="agnes-image-2.1-flash",
        prompt=(
            "A clean product-style image of an AI API gateway dashboard, "
            "modern interface, bright studio lighting"
        ),
        size="1024x1024",
    )

    image = response.data[0]
    print(getattr(image, "url", None) or getattr(image, "b64_json", None))


if __name__ == "__main__":
    main()
