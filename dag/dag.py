class DAGNode:
    def __init__(self, name, run):
        self.name = name
        self.run = run
        self.next = []

    def add_next(self, node):
        self.next.append(node)
