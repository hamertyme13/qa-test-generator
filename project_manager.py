import json
import os

def save_project(filename, application, feature, fields):
    data = {
        "application": application,
        "feature": feature,
        "fields": fields
    }

    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

def load_project(filename):
    with open(filename, "r", encoding="utf-8") as file:
        data = json.load(file)
        return data