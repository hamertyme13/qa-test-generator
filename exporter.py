import csv
import os
from datetime import datetime

def export_to_csv(test_cases):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"output/test_cases_{timestamp}.csv"
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Test ID", "Scenario", "Expected Result", "Priority"])
        for test_case in test_cases:
            writer.writerow(test_case.to_list())
    return filename