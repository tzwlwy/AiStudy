# llm/client.py
import time
from openai import OpenAI


class MockLLMClient:
    def generate(self, prompt: str) -> str:
        time.sleep(0.1)

        if "订单" in prompt:
            return '{"order_id": 1001, "amount": 99.9}'

        return '{"id": 1, "name": "Alice"}'

class DeepSeekLLMClient:
    print('DeepSeekLLMClient')
    def __init__(
        self,
        api_key: str,
        model: str = "deepseek-chat",
        base_url: str = "https://api.deepseek.com/v1"
    ):
        self.client = OpenAI(
            api_key=api_key,
            base_url=base_url
        )
        self.model = model

    def generate(self, prompt: str) -> str:
        start = time.time()

        resp = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": "你是一个后端 API，只允许输出 JSON，不要任何解释说明。"
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0,
        )

        return resp.choices[0].message.content.strip()


class OpenAILLMClient:
    def __init__(self, api_key: str, model: str = "gpt-4o-mini"):
        self.client = OpenAI(api_key=api_key)
        self.model = model

    def generate(self, prompt: str) -> str:
        start = time.time()

        resp = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "你是一个严格输出 JSON 的 API"},
                {"role": "user", "content": prompt},
            ],
            temperature=0,
        )

        return resp.choices[0].message.content.strip()
