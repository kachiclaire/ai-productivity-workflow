import argparse
from core.journal_processor import extract_summary_and_tasks


def main():
    parser = argparse.ArgumentParser(description="Process a journal entry.")
    parser.add_argument("entry", help="The journal entry to summarize", type=str)

    args = parser.parse_args()
    result = extract_summary_and_tasks(args.entry)
    print("\n=== AI Productivity Summary ===")
    print(result)


if __name__ == "__main__":
    main()
