from openai import OpenAI
from .data_storage import *

def get_all_bodies(data, separator="\n\n"):
    bodies = [item["body"] for item in data if "body" in item]
    return separator.join(bodies)

def nlp(datainput):
    client = OpenAI(api_key="sk-f9011889ebdb4531a879127842afe5ae", base_url="https://api.deepseek.com")

    system_prompt = """
    Read this and extract the prices, follow these rules: 1. if the body contains the word selling or sell, 
    2. if price is negative dont extract that, 3. if it says mp the numbers beside it is not the price, 4. Get wether the price was for SEP, LUX, BFR, SAT, JUM or SOR,
    5. Sometimes no label are said rather they use the re-xx format. SOR is re-91, BFR is re-94, JUM is re-95, LUX is re-96, SEP is re-97, SAT is re-99, 6. Get the quality as well they are Q0-Q12
    7. Dont store re-xx format rather store them by proper name(i.e SOR, JUM, etc.) 9. Dont output it if you cant tell what is the type, and dont output it if you cant find the price for the product or even if the price is 0
    EXAMPLE JSON OUTPUT:
    {
        "Q1 SOR": 99000
    }
    """

    # Assuming chat.json contains the message you want to process
    user_prompt = get_all_bodies(read_data("chat.json"), separator="\n\n")

    # If read_data() returns a dictionary, convert it to a string
    if isinstance(user_prompt, dict):
        user_prompt = json.dumps(user_prompt)

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=messages,
        response_format={
            'type': 'json_object'
        }
    )

    return json.loads(response.choices[0].message.content)

if __name__ == "__main__":
    nlp(read_chat("chat.json"))