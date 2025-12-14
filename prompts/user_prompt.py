from schemas.user import UserSchema

SYSTEM_RULES = """
你是一个后端 API 服务，请遵守以下规则：
1. 只允许输出 JSON
2. 不要任何解释说明
3. 不要使用 markdown
4. 不要使用 ```json
5. 输出必须能被 json.loads 解析
""".strip()


def build_user_prompt(text: str) -> str:
    return f"""
{SYSTEM_RULES}

JSON schema:
{UserSchema.schema_json(indent=2)}

用户需求:
{text}
""".strip()
