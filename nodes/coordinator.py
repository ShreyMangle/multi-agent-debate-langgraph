from nodes.logger import log_event

MAX_ROUNDS = 8

def coordinator_node(state):
    if state["current_round"] >= MAX_ROUNDS:
        state["current_agent"] = "Judge"
        log_event(state, "Coordinator", {"status": "routing_to_judge"})
        return state

    expected = "AgentA" if state["current_round"] % 2 == 0 else "AgentB"

    if state["current_agent"] != expected:
        raise ValueError("Out-of-turn execution detected")

    log_event(state, "Coordinator", {
        "allowed_agent": expected,
        "round": state["current_round"] + 1
    })

    return state
