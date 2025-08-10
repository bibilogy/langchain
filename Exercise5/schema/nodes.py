from .state import AgentState
from random import randint

def setup_node(state: AgentState) -> AgentState:
    state["name"] = input("Your name: ")
    state["attempts"] = 0
    state["guesses"] = []
    state["l_bound"] = 0
    state["u_bound"] = 20
    state["number"] = randint(state["l_bound"], state["u_bound"])
    state["max_attempts"] = 7
    return state

def greet_node(state: AgentState) -> AgentState:
    print(f"Hello, {state["name"]}")
    return state

def guess_node(state: AgentState) -> AgentState:
    guess = randint(state["l_bound"], state["u_bound"])
    state["guesses"].append(guess)
    state["attempts"] += 1
    return state

def success_node(state: AgentState) -> AgentState:
    state["result"] = "success"
    return state

def failure_node(state: AgentState) -> AgentState:
    state["result"] = "failure"
    return state


def hint_node(state: AgentState) -> AgentState:
    """Process the guess and update bounds for next iteration"""
    number = state["number"]
    guess = state["guesses"][-1]

    if number == guess:
        print(f"Correct! The number was {number}")
        state["result"] = "success"
    elif state["attempts"] >= state["max_attempts"]:
        print(f"Out of attempts! The number was {number}")
        state["result"] = "failure"
    else:
        # Update bounds for next guess
        if number > guess:
            print(f"Too low! The number is higher than {guess}")
            state["l_bound"] = guess + 1
        elif number < guess:
            print(f"Too high! The number is lower than {guess}")
            state["u_bound"] = guess - 1
        state["result"] = "continue"

    return state

def route_after_hint(state: AgentState) -> str:
    """Conditional edge function that only returns routing decision"""
    return state["result"]
