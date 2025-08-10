from .state import AgentState
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage

load_dotenv()
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

def setup(state: AgentState) -> AgentState:
    state["messages"].append(SystemMessage(content="You are a helpful assistant!"))
    return state

def compose(state: AgentState) -> AgentState:
    message = input("You (enter quit to leave): ")
    state["messages"].append(HumanMessage(content=message))
    return state

def process(state: AgentState) -> AgentState:
    response = llm.invoke(state["messages"])
    state["messages"].append(response)
    print(f"AI: {response.content}\n")
    return state

def should_continue(state: AgentState) -> AgentState:
    message = state["messages"][-1].content
    if message == "quit":
        return "quit"
    else:
        return "continue"



