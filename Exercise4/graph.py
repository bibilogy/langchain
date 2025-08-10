from langgraph.graph import StateGraph, START, END
from schema.state import AgentState
import schema.nodes as nodes

graph = StateGraph(AgentState)
graph.add_node("add", nodes.adder)
graph.add_node("subtract", nodes.subtractor)
graph.add_node("multiply", nodes.multiplicator)
graph.add_node("divide", nodes.divider)
graph.add_node("square", nodes.square)
graph.add_node("cube", nodes.cube)
graph.add_node("math_op_select", lambda state: state)
graph.add_node("exp_op_select", lambda state: state)
graph.add_edge(START, "math_op_select")
graph.add_edge("add", "exp_op_select")
graph.add_edge("subtract", "exp_op_select")
graph.add_edge("multiply", "exp_op_select")
graph.add_edge("divide", "exp_op_select")
graph.add_edge("square", END)
graph.add_edge("cube", END)

graph.add_conditional_edges("math_op_select", nodes.math_op_selector, {"add": "add", "subtract": "subtract", "multiply": "multiply", "divide": "divide"})
graph.add_conditional_edges("exp_op_select", nodes.exp_op_selector, {"square": "square", "cube": "cube"})

app = graph.compile()