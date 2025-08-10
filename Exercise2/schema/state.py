from typing import TypedDict, List

class AgentState(TypedDict):
    name: str
    values: List[int]
    operator: str
    result: str