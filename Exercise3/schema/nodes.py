from .state import AgentState

def greeting_node(state: AgentState) -> AgentState:
    """Function that produces a user greeting"""
    state["result"] += f"Hi, {state["name"]}!\n"
    return state

def process_age_node(state: AgentState) -> AgentState:
    """Function that processes user's age"""
    age = int(state["age"])
    result = "You are major" if age >= 18 else "You are minor"
    state["result"] += f"{result}\n"
    return state

def format_skills_node(state: AgentState) -> AgentState:
    """Function that formats user's skills list"""
    skills = state["skills"]
    result = "You have skills in:"
    for skill in skills:
        result += f"\n\t{skill}"
    state["result"] += result
    return state
