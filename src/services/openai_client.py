# services/openai_client.py
import openai
import os


def get_openai_response(prompt: str, model="gpt-3.5-turbo") -> str:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("Missing OPENAI_API_KEY in environment. See README.")
    openai.api_key = api_key

    response = openai.ChatCompletion.create(
        model=model, messages=[{"role": "user", "content": prompt}], temperature=0.7
    )

    return response.choices[0].message["content"]
