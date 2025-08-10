from langgraph.graph import StateGraph
from schema.nodes import greeting_node
from schema.state import AgentState

graph = StateGraph(AgentState)
graph.add_node("greeter", greeting_node)
graph.set_entry_point("greeter")
graph.set_finish_point("greeter")

app = graph.compile()