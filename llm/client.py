from openai import OpenAI
from config.settings import *

class LLMClient:
    def __init__(self):
        self.client = OpenAI(
            api_key=DEEPSEEK_API_KEY,
            base_url=DEEPSEEK_BASE_URL
        )

    def chat(self, messages, temperature=0):
        resp = self.client.chat.completions.create(
            model=MODEL,
            messages=messages,
            temperature=temperature
        )
        return resp.choices[0].message.content
