import json
from llm.client import LLMClient
from schema.dag import DAGNode, DAGPlan

class DAGPlanner:
    def __init__(self):
        self.llm = LLMClient()

    def plan(self, user_goal: str) -> DAGPlan:
        prompt_base = '''你是一个高级 Agent Planner。
请把用户目标拆解为 DAG 任务。如果目标无法拆解，也要返回 JSON。

⚠️ 你必须【只输出合法 JSON】，禁止任何解释性文本。不要包含 ```json 字样
⚠️ JSON 顶层必须是一个对象，且只包含一个字段：nodes
JSON 格式如下：
{{
  "nodes": [
    {{
      "id": "node1",
      "task": "任务描述",
      "deps": []
    }}
  ]
}}
        '''
        prompt=prompt_base+ f'''用户目标：
{user_goal}'''

        print(prompt)



        resp = self.llm.chat([
            {"role": "system", "content": "你是 DAG Planner"},
            {"role": "user", "content": prompt}
        ])

        print("LLM RAW RESP:\n", resp)

        data = json.loads(resp)

        nodes = {
            n["id"]: DAGNode(
                id=n["id"],
                task=n["task"],
                deps=n.get("deps", [])
            )
            for n in data["nodes"]
        }

        print(nodes)

        return DAGPlan(goal=user_goal, nodes=nodes)

    def plan_from_outline(self, outline: dict) -> DAGPlan:
        nodes = []

        prev_id = None
        for chapter in outline["chapters"]:
            node = DAGNode(
                id=chapter["id"],
                type="chapter_generate",
                description=chapter["summary"],
                depends_on=[prev_id] if prev_id else [],
                payload={
                    "title": chapter["title"],
                    "summary": chapter["summary"]
                }
            )
            nodes.append(node)
            prev_id = chapter["id"]

        return DAGPlan(nodes=nodes)