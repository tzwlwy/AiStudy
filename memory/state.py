class AgentState:
    def __init__(self):
        self.history = []
        self.variables = {}

    def record(self, node):
        self.history.append({
            "id": node.id,
            "task": node.task,
            "result": node.result
        })
