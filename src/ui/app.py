# src/ui/app.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from core.journal_processor import extract_summary_and_tasks
from utils.sanitize_text import sanitize_smart_characters  # ✅ NEW

st.set_page_config(page_title="AI Productivity Journal", layout="centered")
st.title("📝 AI-Powered Productivity Journal")
st.markdown("Write your daily entry below and get an instant summary, tasks, and motivation.")

journal_text = st.text_area(
    "Journal Entry",
    height=200,
    placeholder="e.g. I followed up on emails, called mum, and prepared tomorrow's slides..."  # ✅ Use straight quote
)

if st.button("Process Entry"):
    if not journal_text.strip():
        st.warning("Please enter some text.")
    else:
        with st.spinner("Processing..."):
            try:
                clean_text = sanitize_smart_characters(journal_text)  # ✅ Apply sanitizer
                result = extract_summary_and_tasks(clean_text)
                st.success("Here's your summary:")
                st.markdown(result)
            except Exception as e:
                st.error(f"Error: {e}")
