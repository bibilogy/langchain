from .state import AgentState

def greeting_node(state: AgentState) -> AgentState:
    """Simple node what adds a greeter function"""
    state["message"] = state["message"] + ", you're doing an amazing job learning LangGraph!"
    return state