from unittest.mock import patch, MagicMock
from src.core.journal_processor import extract_summary_and_tasks


def test_process_sample_entry():
    sample = "Today I cleaned my inbox, followed up on the project email, and called my dentist. I still need to buy groceries and prepare slides for tomorrow."

    # Fake message content
    fake_message_content = """
    ✅ Summary:
    - Cleaned inbox and followed up on work
    - Made dentist appointment
    - Pending tasks: groceries and slide prep

    📝 Action Items:
    1. Buy groceries
    2. Prepare slides

    💡 Motivation:
    You're making progress! Small wins add up.
    """

    # Create a mock response object
    mock_response = MagicMock()
    mock_response.choices = [MagicMock(message={"content": fake_message_content})]

    # Patch the OpenAI call
    with patch(
        "src.core.journal_processor.openai.ChatCompletion.create",
        return_value=mock_response,
    ):
        result = extract_summary_and_tasks(sample)
        assert "Summary" in result or "Action" in result or "Motivation" in result
