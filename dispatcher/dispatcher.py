class Dispatcher:
    def __init__(self, tool_registry):
        self.tool_registry = tool_registry

    def dispatch(self, tool_calls):
        results = []

        for call in tool_calls:
            name = call.function.name
            args = eval(call.function.arguments)

            if name not in self.tool_registry:
                raise RuntimeError(f"Tool not found: {name}")

            result = self.tool_registry[name](**args)
            results.append({
                "tool": name,
                "args": args,
                "result": result
            })

        return results
