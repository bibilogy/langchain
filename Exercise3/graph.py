from langgraph.graph import StateGraph
from schema.state import AgentState
from schema.nodes import greeting_node, process_age_node, format_skills_node

graph = StateGraph(AgentState)
graph.add_node("process_greeting", greeting_node)
graph.add_node("process_age", process_age_node)
graph.add_node("process_skills", format_skills_node)
graph.add_edge("process_greeting", "process_age")
graph.add_edge("process_age", "process_skills")
graph.set_entry_point("process_greeting")
graph.set_finish_point("process_skills")

app = graph.compile()