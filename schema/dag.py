from dataclasses import dataclass, field
from typing import List, Dict

@dataclass
class DAGNode:
    id: str
    task: str
    deps: List[str] = field(default_factory=list)
    status: str = "pending"
    result: str = ""

@dataclass
class DAGPlan:
    goal: str
    nodes: Dict[str, DAGNode]
