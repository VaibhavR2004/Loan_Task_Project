import json
import json

import json

def load_json(path):
    try:
        with open(path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("File not found")
        return []
    except json.JSONDecodeError:
        print("Invalid or empty JSON file")
        return []

def create_json(file_path, data):
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)