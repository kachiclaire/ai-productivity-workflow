# core/journal_processor.py
from services.openai_client import get_openai_response

def extract_summary_and_tasks(journal_text: str) -> str:
    prompt = f"""
    Here is my journal entry for today:
    ---
    {journal_text}
    ---
    Please:
    1. Summarize this entry in 3 bullet points.
    2. List any action items I need to follow up on.
    3. End with a short motivational statement.
    """
    return get_openai_response(prompt)
