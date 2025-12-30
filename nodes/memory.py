from nodes.logger import log_event

def memory_node(state):
    state["turns"].append(state["pending_turn"])
    state["current_round"] += 1

    state["current_agent"] = (
        "AgentB" if state["current_agent"] == "AgentA" else "AgentA"
    )

    log_event(state, "MemoryNode", {
        "stored_turn": state["pending_turn"]
    })

    state.pop("pending_turn")
    return state
