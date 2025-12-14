# prompts/registry.py

from prompts.user_prompt import build_user_prompt
from prompts.order_prompt import build_order_prompt

PROMPT_BUILDERS = {
    "user_generate": build_user_prompt,
    "order_generate": build_order_prompt,
}
