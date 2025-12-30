import json, datetime, os

def log_event(state, node, data):
    os.makedirs("logs", exist_ok=True)

    record = {
        "timestamp": datetime.datetime.utcnow().isoformat(),
        "node": node,
        "round": state.get("current_round"),
        "data": data
    }

    with open(state["log_path"], "a", encoding="utf-8") as f:
        f.write(json.dumps(record) + "\n")
