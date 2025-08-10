from typing import TypedDict, List

class AgentState(TypedDict):
    numbers: List[int]
    result: int