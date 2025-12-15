from planner.plan import ExecutionPlan

class Planner:
    def plan(self, user_input, tools):
        # ⚠️ 简化版 Planner（先别优雅）
        messages = [
            {"role": "system", "content": "你是一个智能助手，会使用工具解决问题"},
            {"role": "user", "content": user_input}
        ]

        return ExecutionPlan(
            messages=messages,
            tools=tools
        )
