from langgraph.graph import StateGraph, START, END
from schema.state import AgentState
from schema.nodes import setup_node, greet_node, guess_node, hint_node, success_node, failure_node, route_after_hint

graph = StateGraph(AgentState)
graph.add_node("setup", setup_node)
graph.add_node("greet", greet_node)
graph.add_node("guess", guess_node)
graph.add_node("hint", hint_node)  # Added hint as a proper node
graph.add_node("success", success_node)
graph.add_node("failure", failure_node)

graph.add_edge(START, "setup")
graph.add_edge("setup", "greet")
graph.add_edge("greet", "guess")
graph.add_edge("guess", "hint")  # Always go to hint after guess
graph.add_conditional_edges("hint", route_after_hint, {
    "success": "success",
    "continue": "guess",
    "failure": "failure"
})
graph.add_edge("success", END)
graph.add_edge("failure", END)

app = graph.compile()