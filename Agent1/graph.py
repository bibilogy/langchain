from langgraph.graph import StateGraph, START, END
from schema.state import AgentState
from schema.nodes import process, compose, should_continue, setup

graph = StateGraph(AgentState)
graph.add_node("process", process)
graph.add_node("message", compose)
graph.add_node("setup", setup)
graph.add_edge(START, "setup")
graph.add_edge("setup", "message")
graph.add_edge("process", "message")
graph.add_conditional_edges("message", should_continue, {"quit": END, "continue": "process"})

agent = graph.compile()


