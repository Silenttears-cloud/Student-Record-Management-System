"""Action history and undo service."""

from datetime import datetime

from config import HISTORY_FILE
from utils.file_handler import load_json, save_json


def _load_history() -> list:
    data = load_json(HISTORY_FILE)
    return data.get("actions", [])


def _save_history(actions: list) -> None:
    save_json(HISTORY_FILE, {"actions": actions})


def log_action(action_type: str, description: str, snapshot: dict = None) -> None:
    """Log an action to history."""
    actions = _load_history()
    actions.append({
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "type": action_type,
        "description": description,
        "snapshot": snapshot or {},
    })
    _save_history(actions[-50:])


def view_history() -> None:
    """Display action history."""
    actions = _load_history()

    if not actions:
        print("📭 No history recorded.\n")
        return

    print(f"\n  📜 Action History (last {len(actions)} actions):")
    print(f"  {'#':<4} {'Timestamp':<22} {'Type':<10} {'Description'}")
    print(f"  {'─' * 65}")

    for i, action in enumerate(reversed(actions), 1):
        print(f"  {i:<4} {action['timestamp']:<22} {action['type']:<10} {action['description']}")
    print()


def undo_last_delete(students: dict) -> dict:
    """Undo the last DELETE action by restoring the student."""
    actions = _load_history()

    for i in range(len(actions) - 1, -1, -1):
        if actions[i]["type"] == "DELETE":
            snapshot = actions[i]["snapshot"]
            roll = snapshot.get("roll")
            data = snapshot.get("data")

            if roll and data:
                if roll in students:
                    print(f"  ⚠ Roll {roll} already exists. Cannot restore.\n")
                    return students

                students[roll] = data
                actions.pop(i)
                _save_history(actions)
                print(f"  ✅ Restored student '{data['name']}' (Roll: {roll}).\n")
                return students

    print("  ❌ No delete action found to undo.\n")
    return students
