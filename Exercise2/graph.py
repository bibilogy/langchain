from langgraph.graph import StateGraph
from schema.state import AgentState
from schema.nodes import process_values

graph = StateGraph(AgentState)
graph.add_node("process_values", process_values)
graph.set_entry_point("process_values")
graph.set_finish_point("process_values")

app = graph.compile()