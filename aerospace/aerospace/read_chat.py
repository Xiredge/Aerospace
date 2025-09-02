import json
import time

import json
import time

def read_chat(file_path="chat.json"):
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    extracted_data = []
    stack = [data]  # Start with the top-level data

    while stack:
        current = stack.pop()

        if isinstance(current, dict):

            # Handle message object
            if all(key in current for key in ["id", "body"]):
                extracted_data.append({
                    "id": current["id"],
                    "body": current["body"],
                })
        elif isinstance(current, list):
            # Push all list items to stack for further inspection
            stack.extend(current)

    return extracted_data

if __name__ == "__main__":
    chat = read_chat()
    print(chat)