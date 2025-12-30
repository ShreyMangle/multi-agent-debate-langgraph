from difflib import SequenceMatcher
from langchain_ollama import ChatOllama
from nodes.logger import log_event

llm = ChatOllama(model="llama3")

def is_duplicate(new, past):
    for p in past:
        if SequenceMatcher(None, new, p).ratio() > 0.85:
            return True
    return False

def agent_node(state, persona_file, agent_name):
    with open(persona_file, encoding="utf-8") as f:
        persona = f.read()

    memory_slice = state["turns"][-2:]

    prompt = f"""
{persona}

Topic: {state['topic']}
Relevant memory:
{memory_slice}

Give one concise, non-repetitive argument.
"""

    response = llm.invoke(prompt).content.strip()

    if is_duplicate(response, state["used_arguments"]):
        response += " (reframed)"
        state["coherence_flags"].append("duplicate_detected")

    state["used_arguments"].add(response)

    turn = {
        "round": state["current_round"] + 1,
        "agent": agent_name,
        "text": response
    }

    log_event(state, agent_name, turn)

    state["pending_turn"] = turn
    return state
