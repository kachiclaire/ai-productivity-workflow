from unittest.mock import patch
from src.core.journal_processor import extract_summary_and_tasks

def test_process_sample_entry():
    sample = "I cleaned the inbox and prepped slides. Still need to buy groceries."

    fake_response = "✅ Summary: ...\n📝 Tasks: ...\n💡 Motivation: ..."
    
    with patch("src.core.journal_processor.get_openai_response", return_value=fake_response):
        result = extract_summary_and_tasks(sample)
        assert "Summary" in result
