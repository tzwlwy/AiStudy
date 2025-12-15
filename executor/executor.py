from llm.client import LLMClient

class Executor:
    def __init__(self, max_retry=2):
        self.llm = LLMClient()
        self.max_retry = max_retry

    def run_node(self, node):
        for attempt in range(self.max_retry + 1):
            try:
                resp = self.llm.chat([
                    {"role": "system", "content": "你是一个任务执行 Agent"},
                    {"role": "user", "content": node.task}
                ])
                node.result = resp
                node.status = "done"
                return
            except Exception as e:
                if attempt == self.max_retry:
                    node.status = "failed"
                    node.result = str(e)
