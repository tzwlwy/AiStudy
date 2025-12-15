from openai import OpenAI

from llm.client import LLMClient
from planner.planner import Planner
from executor.executor import Executor
from dispatcher.dispatcher import Dispatcher
from tools.search import search

# DeepSeekLLM = DeepSeekLLMClient(
#     api_key="sk-a999cb8c34f54262aee03239cba7c826",
#     model="deepseek-chat"
# )
#
# # ====== 初始化 ======
# llm = LLMClient(
#     client=DeepSeekLLM,  # ← 你自己的
#     model="deepseek-chat"
# )

client = OpenAI(
    api_key="sk-a999cb8c34f54262aee03239cba7c826",
    base_url="https://api.deepseek.com/v1"
)

llm = LLMClient(
    client=client,
    model="deepseek-chat"   # ✅ model 在你自己的 LLMClient 里
)


planner = Planner()
executor = Executor(llm)

dispatcher = Dispatcher({
    "search": search
})

# ====== 运行 ======
user_input = "帮我搜索 LangGraph 是什么"

plan = planner.plan(
    user_input=user_input,
    tools=[
        {
            "type": "function",
            "function": {
                "name": "search",
                "description": "搜索信息",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query": {"type": "string"}
                    },
                    "required": ["query"]
                }
            }
        }
    ]
)

exec_result = executor.run(plan)

if exec_result.status == "tool_called":
    tool_results = dispatcher.dispatch(exec_result.tool_calls)
    print(tool_results)
else:
    print(exec_result)
