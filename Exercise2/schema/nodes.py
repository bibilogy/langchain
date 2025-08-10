from math import prod

from .state import AgentState

def process_values(state: AgentState) -> AgentState:
    """Function that processes values depending on the state operator"""
    op = state["operator"]
    values = state["values"]
    result = sum(values) if op == "+" else prod(values) if op == "*" else 0
    state["result"] = f"Hi {state["name"]}, your answer is: ${result}" if result != 0 else "Operator not valid"
    return state
