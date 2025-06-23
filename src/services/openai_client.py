# services/openai_client.py
# from dotenv import load_dotenv
# import openai
# import os

# load_dotenv()

# def get_openai_response(prompt: str, model="gpt-3.5-turbo") -> str:
#     api_key = os.getenv("OPENAI_API_KEY")
#     if not api_key:
#         raise ValueError("Missing OPENAI_API_KEY in environment. See README.")

#     client = openai(api_key=api_key)

#     response = client.chat.completions.create(
#         model=model, messages=[{"role": "user", "content": prompt}], temperature=0.7
#     )

#     return response.choices[0].message["content"]

# from openai import OpenAI
# from dotenv import load_dotenv
# import os

# load_dotenv()

# def get_openai_response(prompt: str, model="gpt-3.5-turbo") -> str:
#     api_key = os.getenv("OPENAI_API_KEY")
#     if not api_key:
#         raise ValueError("Missing OPENAI_API_KEY in environment. See README.")

#     client = OpenAI(api_key=api_key)

#     response = client.chat.completions.create(
#         model=model,
#         messages=[{"role": "user", "content": prompt}],
#         temperature=0.7,
#     )

#     return response.choices[0].message.content

# src/services/openai_client.py

import os
from dotenv import load_dotenv
from typing import Literal

load_dotenv()

USE_MOCK = os.getenv("USE_MOCK", "False").lower() == "true"


def get_openai_response(
    prompt: str, model: Literal["gpt-3.5-turbo"] = "gpt-3.5-turbo"
) -> str:
    if USE_MOCK:
        # Return mock response for testing or CI
        return """
✅ Summary:
- Cleaned inbox and followed up on tasks
- Scheduled doctor’s appointment
- Staying on top of responsibilities

📝 Action Items:
1. Prepare tomorrow’s slides
2. Review email follow-ups

💡 Motivation:
Small steps daily = big wins long-term.
"""
    # Real OpenAI call
    from openai import OpenAI

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("Missing OPENAI_API_KEY in environment. See README.")

    client = OpenAI(api_key=api_key)

    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
    )

    return response.choices[0].message.content
