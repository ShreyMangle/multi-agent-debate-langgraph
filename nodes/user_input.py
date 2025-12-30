from nodes.logger import log_event

def user_input_node(state):
    topic = input("Enter topic for debate: ").strip()

    if len(topic) < 10:
        raise ValueError("Topic too short")

    state.update({
        "topic": topic,
        "current_round": 0,
        "current_agent": "AgentA",
        "turns": [],
        "used_arguments": set(),
        "coherence_flags": []
    })

    log_event(state, "UserInputNode", {"topic": topic})
    return state
