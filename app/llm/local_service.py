from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

def get_local_response(prompt: str):
    api_key = os.getenv("LOCAL_API_KEY")
    base_url = os.getenv("LOCAL_BASE_URL")
    model = os.getenv("LOCAL_MODEL")

    if not api_key:
        raise ValueError("LOCAL_API_KEY is not found in the environment")

    if not base_url:
        raise ValueError("LOCAL_BASE_URL is not found in the environment")

    if not model:
        raise ValueError("LOCAL_MODEL is not found in the environment")

    client = OpenAI(
        base_url=base_url,
        api_key=api_key
    )

    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
