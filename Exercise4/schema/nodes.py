from .state import AgentState
from functools import reduce

def get_valid_op() -> str:
    while (op := input("Math operator: ")) not in ["+","-", "*", "/"]:
        print("Invalid operator. Please enter +, -, *, or /\n")
    return op

def get_valid_exp() -> str:
    while (op := input("Exponent: ")) not in ["2", "3"]:
        print("Invalid exponent. Please enter 2, or 3\n")
    return op

def adder(state: AgentState) -> AgentState:
    numbers = state["numbers"]
    state["result"] = reduce(lambda x, y: x + y, numbers)
    print(f"Sum: {state["result"]}")
    return state

def subtractor(state: AgentState) -> AgentState:
    numbers = state["numbers"]
    state["result"] = reduce(lambda x, y: x - y, numbers)
    print(f"Subtraction: {state["result"]}")
    return state

def multiplicator(state: AgentState) -> AgentState:
    numbers = state["numbers"]
    state["result"] = reduce(lambda x, y: x * y, numbers)
    print(f"Multiplication: {state["result"]}")
    return state

def divider(state: AgentState) -> AgentState:
    numbers = state["numbers"]
    state["result"] = reduce(lambda x, y: x /y, numbers)
    print(f"Division: {state["result"]}")
    return state

def square(state: AgentState) -> AgentState:
    result = state["result"]
    result **= 2
    state["result"] = result
    return state

def cube(state: AgentState) -> AgentState:
    result = state["result"]
    result **= 3
    state["result"] = result
    return state

def math_op_selector(state: AgentState) -> AgentState:
    op = get_valid_op()
    if op == "+":
        return "add"
    elif op == "-":
        return "subtract"
    elif op == "*":
        return "multiply"
    else:
        return "divide"

def exp_op_selector(state: AgentState) -> AgentState:
    op = get_valid_exp()
    if op == "2":
        return "square"
    else:
        return "cube"
