class Dispatcher:
    def get_runnable_nodes(self, plan):
        runnable = []
        for node in plan.nodes.values():
            if node.status == "pending":
                if all(plan.nodes[d].status == "done" for d in node.deps):
                    runnable.append(node)
        return runnable
