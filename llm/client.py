class LLMClient:
    def __init__(self, client, model):
        self.client = client
        self.model = model

    def chat(self, messages, tools=None, tool_choice="auto"):
        print(messages)
        return self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            tools=tools,
            tool_choice=tool_choice
        )
