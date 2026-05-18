import json
import os


def save_report(domain, report):
    os.makedirs("output", exist_ok=True)

    filename = f"output/{domain}_report.json"

    with open(filename, "w") as f:
        json.dump(report, f, indent=4)

    print(f"Report saved: {filename}")