from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode
from schema.nodes import model_call, should_continue
from schema.state import AgentState
from schema.tools import tools
from dotenv import load_dotenv
import logging

logger = logging.getLogger(__name__)
load_dotenv()

# Create graph
graph = StateGraph(AgentState)
graph.add_node("agent", model_call)

tool_node = ToolNode(tools=tools)
graph.add_node("tools", tool_node)

# Add edges
graph.add_edge(START, "agent")
graph.add_conditional_edges(
    "agent",
    should_continue,
    {"end": END, "continue": "tools"}  # Make sure mapping is correct
)
graph.add_edge("tools", "agent")

# Compile with interrupts for debugging (optional)
agent = graph.compile()

# agent.py - Improved version with better error handling
from graph import agent
import logging

logger = logging.getLogger(__name__)

def print_stream(stream):
    try:
        for s in stream:
            logger.info(f"Stream step: {list(s.keys())}")
            if "messages" in s and s["messages"]:
                message = s["messages"][-1]
                if isinstance(message, tuple):
                    print(message)
                else:
                    message.pretty_print()
    except Exception as e:
        logger.error(f"Error in stream processing: {e}")
        raise

# Test with timeout to prevent hanging
import signal
import sys

def timeout_handler(signum, frame):
    print("Operation timed out!")
    sys.exit(1)

# Set timeout (30 seconds)
signal.signal(signal.SIGALRM, timeout_handler)
signal.alarm(30)

try:
    inputs = {"messages": [("user", "Add 40 + 12.")]}
    print("Starting agent execution...")
    print_stream(agent.stream(inputs, stream_mode="values"))
except Exception as e:
    print(f"Error during execution: {e}")
finally:
    signal.alarm(0)  # Cancel the alarm