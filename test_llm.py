import os
from http.client import responses

from openai import OpenAI
from pyexpat.errors import messages

client = OpenAI(
    api_key = os.getenv("DEEPSEEK_API_KEY"),
    base_url = "https://api.deepseek.com"
)

response = client.chat.completions.create(
    model = "deepseek-v4-flash",
    messages =  [
        {"role" : "user", "content" : "用一句话说明你能做简历诊断。"}
    ]
)

print(response.choices[0].message.content)