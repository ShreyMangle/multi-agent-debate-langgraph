def generate_dag():
    dot_content = """
digraph LangGraphDebate {
    UserInput -> Coordinator;
    Coordinator -> AgentA [label="even rounds"];
    Coordinator -> AgentB [label="odd rounds"];
    AgentA -> Memory;
    AgentB -> Memory;
    Memory -> Coordinator;
    Coordinator -> Judge [label="after 8 rounds"];
}
"""
    with open("dag.dot", "w", encoding="utf-8") as f:
        f.write(dot_content)

    print("DAG definition saved as dag.dot")


if __name__ == "__main__":
    generate_dag()
