import re

LOG_PATTERN = r"(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2}) (\w+) (.+)"

def parse_log_line(line):
    match = re.match(LOG_PATTERN, line)

    if match:
        return {
            "date": match.group(1),
            "time": match.group(2),
            "level": match.group(3),
            "message": match.group(4)
        }
    return None

from collections import Counter

def analyze_logs(parsed_logs):
    level_counts = Counter()
    message_counts = Counter()

    for log in parsed_logs:
        level_counts[log["level"]] += 1
        message_counts[log["message"]] += 1

    return level_counts, message_counts


def filter_logs(logs, level=None, date=None, keyword=None):
    filtered = []

    for log in logs:
        if level and log["level"] != level:
            continue

        if date and log["date"] != date:
            continue

        if keyword and keyword.lower() not in log["message"].lower():
            continue

        filtered.append(log)

    return filtered

def save_report(filename, levels, messages):
    with open(filename, "w") as file:
        file.write("=== Log Report ===\n\n")

        file.write("Levels:\n")
        for level, count in levels.items():
            file.write(f"{level}: {count}\n")

        file.write("\nTop Messages:\n")
        for msg, count in messages.most_common(5):
            file.write(f"{msg} ({count})\n")


import argparse
from parser import parse_log_line
from analyzer import analyze_logs
from utils import filter_logs, save_report

def load_logs(file_path):
    logs = []

    with open(file_path, "r") as file:
        for line in file:
            parsed = parse_log_line(line.strip())

            if parsed:
                logs.append(parsed)

    return logs


def main():
    parser = argparse.ArgumentParser(description="Log Analyzer")

    parser.add_argument("file", help="Log file path")
    parser.add_argument("--level", help="Filter by level")
    parser.add_argument("--date", help="Filter by date")
    parser.add_argument("--keyword", help="Search keyword")
    parser.add_argument("--export", help="Export report")

    args = parser.parse_args()

    logs = load_logs(args.file)

    filtered_logs = filter_logs(
        logs,
        level=args.level,
        date=args.date,
        keyword=args.keyword
    )

    levels, messages = analyze_logs(filtered_logs)

    print("\n=== Summary ===")
    for level, count in levels.items():
        print(f"{level}: {count}")

    print("\nTop Messages:")
    for msg, count in messages.most_common(5):
        print(f"{msg} ({count})")

    if args.export:
        save_report(args.export, levels, messages)
        print(f"\nReport saved to {args.export}")


if __name__ == "__main__":
    main()
              
