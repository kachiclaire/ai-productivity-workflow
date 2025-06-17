# src/core/journal_processor.py

import os
from dotenv import load_dotenv
import openai

# Load variables from .env into os.environ
load_dotenv()

# Ensure the API key is set
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("Missing OPENAI_API_KEY in environment. See README.")

openai.api_key = OPENAI_API_KEY


def extract_summary_and_tasks(journal_text: str) -> str:
    """
    Send the journal entry to OpenAI and return:
      1. A 3-bullet summary
      2. A list of action items
      3. A motivational statement
    """
    prompt = f"""
    Here is my journal entry for today:
    ---
    {journal_text}
    ---
    Please:
    1. Summarize this entry in 3 bullet points.
    2. List any clear action items I need to follow up on.
    3. End with a short motivational statement.
    """
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
    )
    # Extract and return the assistant’s message content
    return response.choices[0].message["content"]
