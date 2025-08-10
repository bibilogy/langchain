from typing import TypedDict, List

class AgentState(TypedDict):
    name: str
    guesses: List[int]
    attempts: int
    l_bound: int
    u_bound: int
    number: int
    max_attempts: int
    result: str

