# prompts/prompt_builder.py

from schemas.user import UserSchema


class PromptBuilder:
    def build(self, user_input: str) -> str:
        return f"""
请严格以 JSON 格式返回，不要包含多余文本。
JSON schema:
{{
  "id": int,
  "name": string
}}

用户需求：
{user_input}
""".strip()

    def build_retry(self, user_input: str, errors) -> str:
        error_text = "\n".join(
            f"- {e.code}: {e.message}" for e in errors
        )

        return f"""
上一次输出不符合要求，错误如下：
{error_text}

请修正并【只输出 JSON】。

用户需求：
{user_input}
""".strip()
