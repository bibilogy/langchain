from typing import TypedDict, List

class AgentState(TypedDict):
    name: str
    age: str
    skills: List[str]
    result: str