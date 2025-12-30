from langchain_ollama import ChatOllama
from nodes.logger import log_event

llm = ChatOllama(model="llama3")

def judge_node(state):
    transcript = "\n".join(
        f"{t['agent']}: {t['text']}" for t in state["turns"]
    )

    prompt = f"""
Review this debate.

{transcript}

Provide:
1. Summary
2. Winner (AgentA or AgentB)
3. Justification
"""

    result = llm.invoke(prompt).content.strip()

    winner = "AgentA" if "AgentA" in result else "AgentB"

    state["summary"] = result
    state["winner"] = winner

    log_event(state, "JudgeNode", {
        "winner": winner,
        "summary": result
    })

    return state
