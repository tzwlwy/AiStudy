# cases/prompt_cases.py
from schemas.user import UserSchema


PROMPT_CASES = [
    {
        "id": 1,
        "task": "user_generate",
        "schema": UserSchema,

        "input": {
            "text": "生成一个用户信息，id 是 1，name 是 Alice"
        }
    },
    {
        "id": 2,
        "task": "order_generate",
        "schema": UserSchema,

        "input": {
            "text": "生成一个订单，订单号是 1001，金额是 99.9"
        }
    }
]
