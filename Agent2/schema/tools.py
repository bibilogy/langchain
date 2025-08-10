from langchain_core.tools import tool

@tool
def add(a: int, b: int):
    """This is an addition function that adds two numbers together"""
    return a + b

tools = [add]

