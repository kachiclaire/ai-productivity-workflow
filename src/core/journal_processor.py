import openai
import os
import logging
from dotenv import load_dotenv

load_dotenv()

# Configure basic logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def extract_summary_and_tasks(journal_text: str) -> str:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        logger.error("OPENAI_API_KEY not set in environment.")
        raise ValueError("Missing OPENAI_API_KEY in environment. See README.")

    openai.api_key = api_key

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

    try:
        logger.info("Sending prompt to OpenAI...")
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
        )
        content = response.choices[0].message["content"]
        logger.info("Response received successfully.")
        return content

    except Exception as e:
        logger.exception("Error communicating with OpenAI")
        raise e

