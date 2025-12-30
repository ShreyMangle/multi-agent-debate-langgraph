# Multi-Agent Debate System (LangGraph)

## Overview
This project implements a **LangGraph-based multi-agent debate workflow** that simulates a structured debate between two AI agents:

- **AgentA (Scientist)**
- **AgentB (Philosopher)**

The system enforces strict turn control, preserves debate memory with controlled visibility, performs lightweight state validation, logs all node executions, and concludes with a Judge node that summarizes the debate and declares a winner with justification.

The application runs **entirely via a clean CLI** and uses a **local LLM powered by Ollama**.

---

## Key Features

- ✅ LangGraph DAG-based workflow
- ✅ Exactly **8 rounds** (4 turns per agent), strictly alternating
- ✅ Dedicated **Coordinator** node for turn enforcement
- ✅ Explicit **MemoryNode** with controlled memory slicing
- ✅ Duplicate argument detection (string similarity)
- ✅ Basic logical coherence checks
- ✅ Final **JudgeNode** with summary, winner, and justification
- ✅ Persistent logging of **every node execution and state transition**
- ✅ Fully CLI-based (no UI, no web server)
- ✅ Deterministic execution via optional random seed

---

## Project Structure

multi_agent_debate/
│
├── run_debate.py
├── generate_dag.py
├── requirements.txt
│
├── nodes/
│ ├── user_input.py
│ ├── coordinator.py
│ ├── agent.py
│ ├── memory.py
│ ├── judge.py
│ └── logger.py
│
├── personas/
│ ├── scientist.txt
│ └── philosopher.txt
│
├── logs/
│ └── debate_log_<timestamp>.json
│
└── dag.dot