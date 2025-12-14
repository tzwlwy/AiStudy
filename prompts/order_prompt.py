# prompts/order_prompt.py
from schemas.order import OrderSchema


def build_order_prompt(text: str) -> str:
    return f"""
你是一个 API 服务，请严格返回 JSON，不要包含多余文本。

JSON schema:
{OrderSchema.schema_json(indent=2)}

订单需求:
{text}
""".strip()
