import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

def get_cloud_response(prompt: str):
    api_key = os.getenv("GEMINI_API_KEY")
    base_url = os.getenv("GEMINI_BASE_URL")
    model = os.getenv("GEMINI_MODEL")

    if not api_key:
        raise ValueError("GEMINI_API_KEY is not found in the environment")

    if not base_url:
        raise ValueError("GEMINI_BASE_URL is not found in the environment")

    if not model:
        raise ValueError("GEMINI_MODEL is not found in the environment")

    client = OpenAI(
        api_key=os.getenv("GEMINI_API_KEY"),
        base_url=os.getenv("GEMINI_BASE_URL")
    )

    response = client.chat.completions.create(
        model=os.getenv("GEMINI_MODEL"),
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content


def stream_cloud_response(prompt: str):
    client = OpenAI(
        api_key=os.getenv("GEMINI_API_KEY"),
        base_url=os.getenv("GEMINI_BASE_URL")
    )

    stream = client.chat.completions.create(
        model=os.getenv("GEMINI_MODEL"),
        messages=[{"role": "user", "content": prompt}],
        stream=True
    )

    for chunk in stream:
        if chunk.choices[0].delta.content:
            yield chunk.choices[0].delta.content
