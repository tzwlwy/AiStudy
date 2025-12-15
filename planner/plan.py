class ExecutionPlan:
    def __init__(self, messages, tools, tool_choice="auto", missing_args=None):
        self.messages = messages
        self.tools = tools
        self.tool_choice = tool_choice
        self.missing_args = missing_args or []
