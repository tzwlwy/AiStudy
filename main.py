from planner.planner import DAGPlanner
from dispatcher.dispatcher import Dispatcher
from executor.executor import Executor
from memory.state import AgentState
from judge.judge import GoalJudge

def main():
    # goal = input("请输入目标：")

    goal={
        "title": "第一卷",
        "chapters": [
            {
                "id": "ch1",
                "title": "少年出村",
                "summary": "主角第一次离开家乡"
            },
            {
                "id": "ch2",
                "title": "初入江湖",
                "summary": "主角遭遇第一次冲突"
            }
        ]
    }

    planner = DAGPlanner()
    dispatcher = Dispatcher()
    executor = Executor()
    memory = AgentState()
    judge = GoalJudge()

    # plan = planner.plan_from_outline(goal)
    plan = planner.plan(goal)

    while True:
        runnable = dispatcher.get_runnable_nodes(plan)
        if not runnable:
            break

        for node in runnable:
            executor.run_node(node)
            memory.record(node)

    done = judge.is_done(goal, memory)
    print("目标是否完成：", done)
    print(memory.history)

if __name__ == "__main__":
    main()
