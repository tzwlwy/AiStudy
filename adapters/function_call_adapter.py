import json
from typing import Dict, Any


def extract_function_args(raw_output) -> Dict[str, Any]:
    """
    把 function call / tool call 输出
    解析成标准 dict
    """

    # ⚠️ 示例：不同 LLM SDK 不一样
    if hasattr(raw_output, "tool_calls"):
        tool_call = raw_output.tool_calls[0]
        return json.loads(tool_call["arguments"])

    # fallback（调试用）
    if isinstance(raw_output, str):
        return json.loads(raw_output)

    raise ValueError("Unsupported function call format")
