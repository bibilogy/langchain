from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage
from .state import AgentState
from .tools import tools
import logging

# Add logging to debug
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash").bind_tools(tools)


def model_call(state: AgentState) -> AgentState:
    logger.info(f"Model call with {len(state['messages'])} messages")
    system_prompt = SystemMessage(
        content="You are my AI assistant, please answer my query to the best of your ability.")

    try:
        response = llm.invoke([system_prompt] + state["messages"])
        logger.info(
            f"Model response: {type(response)}, tool_calls: {hasattr(response, 'tool_calls') and len(response.tool_calls) if hasattr(response, 'tool_calls') else 'None'}")
        return {"messages": [response]}
    except Exception as e:
        logger.error(f"Error in model_call: {e}")
        raise


def should_continue(state: AgentState):
    messages = state["messages"]
    last_message = messages[-1]

    logger.info(f"Should continue check - message type: {type(last_message)}")
    logger.info(f"Has tool_calls attr: {hasattr(last_message, 'tool_calls')}")

    if hasattr(last_message, 'tool_calls') and last_message.tool_calls:
        logger.info(f"Tool calls found: {len(last_message.tool_calls)}")
        return "continue"
    else:
        logger.info("No tool calls, ending")
        return "end"