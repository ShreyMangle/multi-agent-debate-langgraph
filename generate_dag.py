from graphviz import Digraph


def generate_dag():
    dot = Digraph(
        comment="LangGraph Multi-Agent Debate DAG",
        format="png"
    )

    # Nodes
    dot.node("UserInput", "UserInputNode")
    dot.node("Coordinator", "Coordinator")
    dot.node("AgentA", "AgentA (Scientist)")
    dot.node("AgentB", "AgentB (Philosopher)")
    dot.node("Memory", "MemoryNode")
    dot.node("Judge", "JudgeNode")

    # Edges
    dot.edge("UserInput", "Coordinator")
    dot.edge("Coordinator", "AgentA", label="even rounds")
    dot.edge("Coordinator", "AgentB", label="odd rounds")
    dot.edge("AgentA", "Memory")
    dot.edge("AgentB", "Memory")
    dot.edge("Memory", "Coordinator")
    dot.edge("Coordinator", "Judge", label="after 8 rounds")

    # Render
    dot.render("dag")
    print("✅ DAG diagram saved as dag.png")


if __name__ == "__main__":
    generate_dag()
