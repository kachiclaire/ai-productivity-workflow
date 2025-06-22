import streamlit as st
from core.journal_processor import extract_summary_and_tasks

st.title("🧠 AI Productivity Journal")

entry = st.text_area("Write your journal entry below:", height=200)

if st.button("Summarize and Suggest"):
    if entry.strip():
        result = extract_summary_and_tasks(entry)
        st.markdown("### ✨ Output")
        st.code(result)
    else:
        st.warning("Please enter a journal entry.")
