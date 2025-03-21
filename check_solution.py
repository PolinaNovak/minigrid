import json
import sys
from pathlib import Path

def load_config(filename="config.json"):
    with open(filename, "r") as file:
        return json.load(file)


if __name__ == "__main__":
    config = load_config()
    project_root = Path(__file__).parent

    task_directory = project_root / "lab_tasks" / config["task"]
    if task_directory not in sys.path:
        sys.path.append(str(task_directory))

    try:
        from main import start
    except ImportError as e:
        print(f"Ошибка при импорте функции start: {e}")
        sys.exit(1)

    start(config)
