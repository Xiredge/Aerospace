import json
import time

def read_chat(file_path="chat.json"):
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    extracted_data = []
    stack = [data]  # Start with the top-level data

    while stack:
        current = stack.pop()
        print(stack)
        print("stack")
        time.sleep(5)
        if isinstance(current, dict):

            # Handle message object
            if all(key in current for key in ["id", "sender", "body", "datetime"]):
                extracted_data.append({
                    "id": current["id"],
                    "sender_company": current["sender"]["company"],
                    "body": current["body"],
                    "datetime": current["datetime"]
                })
        elif isinstance(current, list):
            # Push all list items to stack for further inspection
            stack.extend(current)

    return extracted_data

if __name__ == "__main__":
    chat = read_chat()
    #print(chat)