import time
import argparse
import random
from langgraph.graph import StateGraph

from nodes.user_input import user_input_node
from nodes.coordinator import coordinator_node
from nodes.agent import agent_node
from nodes.memory import memory_node
from nodes.judge import judge_node


def main():
    parser = argparse.ArgumentParser(description="LangGraph Multi-Agent Debate")
    parser.add_argument("--seed", type=int, default=None, help="Random seed for determinism")
    parser.add_argument("--log-path", type=str, default=None, help="Path to log file")
    parser.add_argument("--persona-dir", type=str, default="personas", help="Persona directory")

    args = parser.parse_args()

    if args.seed is not None:
        random.seed(args.seed)

    log_path = args.log_path or f"logs/debate_log_{int(time.time())}.json"

    state = {
        "log_path": log_path,
        "persona_dir": args.persona_dir
    }

    graph = StateGraph(dict)

    # Nodes
    graph.add_node("UserInput", user_input_node)
    graph.add_node("Coordinator", coordinator_node)
    graph.add_node(
        "AgentA",
        lambda s: agent_node(
            s, f"{args.persona_dir}/scientist.txt", "AgentA"
        ),
    )
    graph.add_node(
        "AgentB",
        lambda s: agent_node(
            s, f"{args.persona_dir}/philosopher.txt", "AgentB"
        ),
    )
    graph.add_node("Memory", memory_node)
    graph.add_node("Judge", judge_node)

    # Edges
    graph.set_entry_point("UserInput")
    graph.add_edge("UserInput", "Coordinator")

    graph.add_conditional_edges(
        "Coordinator",
        lambda s: s["current_agent"],
        {
            "AgentA": "AgentA",
            "AgentB": "AgentB",
            "Judge": "Judge",
        },
    )

    graph.add_edge("AgentA", "Memory")
    graph.add_edge("AgentB", "Memory")
    graph.add_edge("Memory", "Coordinator")

    # Compile & run
    app = graph.compile()
    final_state = app.invoke(state)

    # Output
    print("\n=========== FINAL JUDGE ===========\n")
    print(final_state["summary"])
    print("\nWinner:", final_state["winner"])
    print(f"\nLog file saved at: {log_path}")


if __name__ == "__main__":
    main()
