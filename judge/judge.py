from llm.client import LLMClient

class GoalJudge:
    def __init__(self):
        self.llm = LLMClient()

    def is_done(self, goal, memory):
        prompt = f"""
目标：
{goal}

执行结果：
{memory.history}

请判断目标是否完成，只回答 yes 或 no
"""
        resp = self.llm.chat([
            {"role": "user", "content": prompt}
        ])
        return "yes" in resp.lower()
