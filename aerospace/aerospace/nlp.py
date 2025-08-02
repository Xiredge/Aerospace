from openai import OpenAI
from data_storage import *

client = OpenAI(api_key="sk-f9011889ebdb4531a879127842afe5ae", base_url="https://api.deepseek.com")

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": f"Read this and extract the prices, follow these rules: 1. if the body contains the word selling or sell , "
                                    f"2. if price is negative dont extract that, 3. if it says mp the numbers beside it is not the price, {read_data("chat.json")}"},
    ],
    stream=False
)

print(response.choices[0].message.content)