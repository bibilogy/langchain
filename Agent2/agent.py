from typing import TypedDict, Annotated, Sequence
from langchain_core.messages import BaseMessage, SystemMessage, HumanMessage
from langgraph.graph.message import add_messages
from langchain_core.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode
from dotenv import load_dotenv

load_dotenv()

class AgentState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], add_messages]

@tool
def add(a: int, b: int):
    """This is an addition function that adds two numbers together"""
    return a + b

@tool
def subtract(a: int, b: int):
    """This is a subtraction function that subtracts two numbers"""
    return a - b

tools = [add, subtract]

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash").bind_tools(tools)

def model_call(state: AgentState) -> AgentState:
    messages = state["messages"]
    if not messages or not isinstance(messages[0], SystemMessage):
        system_prompt = SystemMessage(
            content="You are my AI assistant. When you use tools, provide a final answer based on the tool results."
        )
        messages = [system_prompt] + messages

    response = llm.invoke(messages)
    return {"messages": [response]}


def should_continue(state: AgentState):
    messages = state["messages"]
    last_message = messages[-1]

    if hasattr(last_message, 'tool_calls') and last_message.tool_calls:
        return "continue"
    else:
        return "end"


# Create the graph
graph = StateGraph(AgentState)
graph.add_node("agent", model_call)
tool_node = ToolNode(tools=tools)
graph.add_node("tools", tool_node)

# Add edges
graph.add_edge(START, "agent")
graph.add_conditional_edges(
    "agent",
    should_continue,
    {"end": END, "continue": "tools"}
)
graph.add_edge("tools", "agent")

# Compile the graph
agent = graph.compile()


def print_stream(stream):
    for s in stream:
        if "messages" in s and s["messages"]:
            message = s["messages"][-1]
            message.pretty_print()


# Run the agent
inputs = {"messages": [HumanMessage(content="Add 40 + 12 and then subtract 10 from the result. And also tell me a joke.")]}
print_stream(agent.stream(inputs, stream_mode="values"))