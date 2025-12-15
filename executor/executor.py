from types import SimpleNamespace

class Executor:
    def __init__(self, llm_client):
        self.llm = llm_client

    def run(self, plan):
        if plan.missing_args:
            return SimpleNamespace(
                status="need_more_info",
                missing_args=plan.missing_args
            )

        resp = self.llm.chat(
            messages=plan.messages,
            tools=plan.tools,
            tool_choice=plan.tool_choice
        )

        message = resp.choices[0].message

        if not message.tool_calls:
            return SimpleNamespace(
                status="no_tool_call",
                raw_message=message
            )

        return SimpleNamespace(
            status="tool_called",
            tool_calls=message.tool_calls
        )
