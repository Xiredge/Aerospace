import json
import os

def store_data(data, filename="json.json"):
    def save_json_to_file(data, filename="data.json"):
        """Saves a dictionary as a JSON file."""
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)
    print(f"JSON data saved to {filename}")

def read_data(filename="json.json"):
    """Reads a JSON file and returns its content as a dictionary."""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error: {filename} is not a valid JSON file.")
        return None
